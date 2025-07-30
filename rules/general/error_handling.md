# 에러 처리 규칙 (Error Handling)

## 1. 예외 vs 에러 코드

### 예외 사용 권장
```dart
// Good - 예외 사용
User getUser(String id) {
  final user = repository.findById(id);
  if (user == null) {
    throw UserNotFoundException('User not found with id: $id');
  }
  return user;
}

// Bad - 에러 코드 반환
Result<User> getUser(String id) {
  final user = repository.findById(id);
  if (user == null) {
    return Result.error(ErrorCode.USER_NOT_FOUND);
  }
  return Result.success(user);
}
```

## 2. 커스텀 예외 정의

### 구체적인 예외 클래스
```dart
// Good - 구체적인 예외
class UserNotFoundException implements Exception {
  final String message;
  final String userId;
  
  UserNotFoundException(this.userId) 
    : message = 'User not found with id: $userId';
}

class InvalidEmailException implements Exception {
  final String message;
  final String email;
  
  InvalidEmailException(this.email)
    : message = 'Invalid email format: $email';
}

// 사용
void updateUserEmail(String userId, String email) {
  if (!isValidEmail(email)) {
    throw InvalidEmailException(email);
  }
  
  final user = getUser(userId);  // UserNotFoundException 가능
  user.email = email;
  saveUser(user);
}
```

## 3. Try-Catch 패턴

### 구체적인 예외 처리
```dart
// Good - 구체적인 예외별 처리
Future<void> processPayment(Payment payment) async {
  try {
    await paymentGateway.charge(payment);
  } on InsufficientFundsException {
    await notifyUser('잔액이 부족합니다.');
    throw PaymentFailedException('Insufficient funds');
  } on NetworkException {
    await retryPayment(payment);
  } on PaymentGatewayException catch (e) {
    logger.error('Payment gateway error: ${e.message}');
    throw PaymentFailedException('Payment processing failed');
  }
}

// Bad - 모든 예외를 한번에 처리
try {
  await paymentGateway.charge(payment);
} catch (e) {
  print('Error: $e');  // 너무 일반적
}
```

### Try 블록 최소화
```dart
// Good - 필요한 부분만 try-catch
Future<User> createUser(UserRequest request) async {
  // 검증은 try 밖에서
  validateUserRequest(request);
  
  final user = User.fromRequest(request);
  
  // DB 작업만 try-catch
  try {
    await database.save(user);
  } on DatabaseException catch (e) {
    throw UserCreationException('Failed to save user: ${e.message}');
  }
  
  // 알림은 별도 처리
  await sendWelcomeEmail(user);
  
  return user;
}
```

## 4. Null 처리

### Null Safety 활용
```dart
// Good - Null safety 활용
class UserService {
  User? findUser(String id) {
    return repository.findById(id);
  }
  
  String getUserName(String id) {
    final user = findUser(id);
    return user?.name ?? 'Unknown User';
  }
}

// Bad - Null 체크 누락
String getUserName(String id) {
  final user = repository.findById(id);
  return user.name;  // NullPointerException 위험
}
```

### Early Return 패턴
```dart
// Good - Early return으로 중첩 감소
void processUser(User? user) {
  if (user == null) {
    logger.info('User is null, skipping processing');
    return;
  }
  
  if (!user.isActive) {
    logger.info('User is inactive: ${user.id}');
    return;
  }
  
  // 메인 로직
  performUserProcessing(user);
}
```

## 5. 에러 메시지

### 구체적이고 유용한 메시지
```dart
// Good - 구체적인 정보 포함
throw ValidationException(
  'Invalid email format. Expected: user@domain.com, Got: $email'
);

throw NotFoundException(
  'User not found. ID: $userId, SearchTime: ${DateTime.now()}'
);

// Bad - 너무 일반적
throw Exception('Error occurred');
throw Exception('Invalid input');
```

### 사용자 친화적 메시지
```dart
class ApiException implements Exception {
  final String technicalMessage;
  final String userMessage;
  final int statusCode;
  
  ApiException({
    required this.technicalMessage,
    required this.userMessage,
    required this.statusCode,
  });
}

// 사용
throw ApiException(
  technicalMessage: 'Database connection timeout after 30s',
  userMessage: '일시적인 오류가 발생했습니다. 잠시 후 다시 시도해주세요.',
  statusCode: 503,
);
```

## 6. 에러 로깅

### 적절한 로그 레벨
```dart
// Good - 레벨별 로깅
class PaymentService {
  Future<void> processPayment(Payment payment) async {
    logger.info('Processing payment: ${payment.id}');
    
    try {
      await gateway.charge(payment);
      logger.info('Payment successful: ${payment.id}');
    } catch (e, stackTrace) {
      logger.error(
        'Payment failed',
        error: e,
        stackTrace: stackTrace,
        extra: {'paymentId': payment.id, 'amount': payment.amount},
      );
      throw PaymentException('Payment processing failed');
    }
  }
}
```

## 7. 복구 전략

### 재시도 로직
```dart
// Good - 지수 백오프로 재시도
Future<T> retryWithBackoff<T>({
  required Future<T> Function() operation,
  int maxAttempts = 3,
  Duration initialDelay = const Duration(seconds: 1),
}) async {
  var attempt = 0;
  var delay = initialDelay;
  
  while (attempt < maxAttempts) {
    try {
      return await operation();
    } on NetworkException catch (e) {
      attempt++;
      if (attempt >= maxAttempts) {
        throw NetworkException(
          'Failed after $maxAttempts attempts: ${e.message}'
        );
      }
      
      logger.warn('Attempt $attempt failed, retrying in $delay');
      await Future.delayed(delay);
      delay *= 2;  // 지수 백오프
    }
  }
  
  throw StateError('Should not reach here');
}
```

### 우아한 실패 (Graceful Degradation)
```dart
// Good - 기본값으로 폴백
class ConfigService {
  final Map<String, dynamic> _config = {};
  
  T getConfig<T>(String key, T defaultValue) {
    try {
      return _config[key] as T;
    } catch (e) {
      logger.warn('Config not found or invalid type: $key, using default');
      return defaultValue;
    }
  }
}

// 사용
final timeout = configService.getConfig('api.timeout', 30);
final retryCount = configService.getConfig('api.retryCount', 3);
```