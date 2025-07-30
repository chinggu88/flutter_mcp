# 함수 작성 규칙 (Function Rules)

## 1. 함수 크기

### 작은 함수 원칙
- 함수는 20줄 이하로 유지
- 한 화면에 전체가 보이는 크기
- 들여쓰기는 2단계 이하

```dart
// Good - 작고 명확한 함수
double calculateDiscountPrice(double price, double discountRate) {
  validatePrice(price);
  validateDiscountRate(discountRate);
  
  final discount = price * discountRate;
  return price - discount;
}

// Bad - 너무 긴 함수
double processOrder(Order order) {
  // 50줄 이상의 코드...
  // 검증, 계산, 저장, 알림 등 여러 작업 혼재
}
```

## 2. 단일 책임 원칙

### 한 가지 일만 수행
```dart
// Good - 각 함수가 하나의 책임만
void processPayment(Payment payment) {
  validatePayment(payment);
  chargePayment(payment);
  sendReceipt(payment);
}

void validatePayment(Payment payment) {
  if (payment.amount <= 0) {
    throw InvalidPaymentException('Amount must be positive');
  }
  // 검증 로직만
}

void chargePayment(Payment payment) {
  // 결제 처리만
}

// Bad - 여러 책임 혼재
void handlePayment(Payment payment) {
  // 검증도 하고
  if (payment.amount <= 0) {
    throw Exception('Invalid amount');
  }
  
  // 결제도 하고
  gateway.charge(payment);
  
  // 이메일도 보내고
  emailService.sendReceipt(payment);
  
  // 로그도 남기고
  logger.log('Payment processed');
}
```

## 3. 함수 인자

### 인자 개수 제한
```dart
// Good - 3개 이하의 인자
User createUser(String name, String email) {
  return User(name: name, email: email);
}

// Good - 많은 인자는 객체로 그룹화
User createUser(UserCreationRequest request) {
  return User(
    name: request.name,
    email: request.email,
    phone: request.phone,
    address: request.address,
  );
}

// Bad - 너무 많은 인자
User createUser(String name, String email, String phone, 
                String address, String city, String country) {
  // 인자가 너무 많음
}
```

### 플래그 인자 피하기
```dart
// Bad - boolean 플래그
void render(bool isAuthenticated) {
  if (isAuthenticated) {
    renderAuthenticatedView();
  } else {
    renderGuestView();
  }
}

// Good - 명확한 함수 분리
void renderAuthenticatedView() {
  // 인증된 사용자 뷰
}

void renderGuestView() {
  // 게스트 뷰
}
```

## 4. 부수 효과 방지

### 예측 가능한 함수
```dart
// Good - 부수 효과 없음
int add(int a, int b) {
  return a + b;
}

// Bad - 숨겨진 부수 효과
int calculateAndSave(int a, int b) {
  final result = a + b;
  database.save(result);  // 숨겨진 부수 효과
  return result;
}
```

### 명령과 조회 분리
```dart
// Good - 조회와 명령 분리
class UserService {
  // 조회만
  User getUser(String id) {
    return repository.findById(id);
  }
  
  // 명령만
  void updateUser(User user) {
    repository.save(user);
  }
}

// Bad - 조회와 명령 혼재
User getUserAndIncrementLoginCount(String id) {
  final user = repository.findById(id);
  user.loginCount++;
  repository.save(user);
  return user;
}
```

## 5. 에러 처리

### 예외 사용
```dart
// Good - 명확한 예외
User findUser(String id) {
  final user = repository.findById(id);
  if (user == null) {
    throw UserNotFoundException('User not found: $id');
  }
  return user;
}

// Bad - null 반환
User? findUser(String id) {
  return repository.findById(id);  // null 체크를 호출자에게 위임
}
```

### Try-Catch 범위 최소화
```dart
// Good - 최소 범위
Future<void> saveUser(User user) async {
  validateUser(user);
  
  try {
    await repository.save(user);
  } catch (e) {
    throw DatabaseException('Failed to save user: ${e.message}');
  }
}

// Bad - 너무 넓은 범위
Future<void> processUser(User user) async {
  try {
    validateUser(user);
    calculateAge(user);
    await repository.save(user);
    sendEmail(user);
  } catch (e) {
    // 어디서 발생한 에러인지 불명확
  }
}
```

## 6. 함수 추상화 수준

### 일관된 추상화 수준
```dart
// Good - 같은 추상화 수준
void processOrder(Order order) {
  validateOrder(order);
  calculateTotalPrice(order);
  applyDiscounts(order);
  chargePayment(order);
  sendConfirmation(order);
}

// Bad - 혼재된 추상화 수준
void processOrder(Order order) {
  validateOrder(order);
  
  // 갑자기 낮은 수준의 구현
  double total = 0;
  for (var item in order.items) {
    total += item.price * item.quantity;
  }
  
  chargePayment(order);
}
```

## 7. 함수 구조화

### 위에서 아래로 읽기
```dart
// Good - 자연스러운 흐름
class OrderService {
  void processOrder(Order order) {
    validateOrder(order);
    calculatePricing(order);
    executePayment(order);
  }
  
  void validateOrder(Order order) {
    // 검증 로직
  }
  
  void calculatePricing(Order order) {
    // 가격 계산
  }
  
  void executePayment(Order order) {
    // 결제 실행
  }
}
```

### 관련 함수 그룹화
```dart
class UserRepository {
  // 조회 관련
  User findById(String id) {}
  List<User> findAll() {}
  List<User> findByEmail(String email) {}
  
  // 저장 관련
  void save(User user) {}
  void update(User user) {}
  void delete(String id) {}
}
```