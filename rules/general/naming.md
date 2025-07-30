# 네이밍 규칙 (Naming Conventions)

## 1. 변수명 규칙

### 기본 원칙
- 의미있고 발음 가능한 이름 사용
- 약어 사용 최소화
- 맥락을 명확히 나타내는 이름

### 변수명 규칙
```dart
// Good
final String customerEmail;
final int itemCount;
final bool isActive;
final DateTime createdAt;

// Bad
final String e;      // 의미 불명확
final int cnt;       // 불필요한 약어
final bool flag;     // 너무 일반적
final DateTime dt;   // 의미 불명확
```

### Boolean 변수명
```dart
// Good - is, has, can으로 시작
bool isLoading = false;
bool hasError = false;
bool canEdit = true;

// Bad
bool loading = false;    // is 접두사 누락
bool error = false;      // has 접두사 누락
```

## 2. 함수명 규칙

### 동사로 시작
```dart
// Good
void calculateTotal();
String getUserName();
Future<void> fetchData();
bool validateEmail(String email);

// Bad
void total();        // 명사
String userName();   // 동작 불명확
```

### 명확한 동작 표현
```dart
// Good
void saveUserToDatabase(User user);
List<Product> filterActiveProducts(List<Product> products);
Future<Response> sendHttpRequest(Request request);

// Bad
void handleUser(User user);      // 모호한 동작
List<Product> process(List<Product> products);  // 불명확
```

## 3. 클래스명 규칙

### 명사 사용, PascalCase
```dart
// Good
class UserController {}
class ProductRepository {}
class AuthenticationService {}
class ShoppingCart {}

// Bad
class ManageUser {}      // 동사 포함
class user_controller {} // snake_case
class UC {}             // 약어
```

## 4. 상수명 규칙

### 대문자와 언더스코어
```dart
// Good
const int MAX_RETRY_COUNT = 3;
const String API_BASE_URL = 'https://api.example.com';
const Duration CACHE_TIMEOUT = Duration(minutes: 5);

// Dart 스타일 (lowerCamelCase도 허용)
const int maxRetryCount = 3;
const String apiBaseUrl = 'https://api.example.com';
```

## 5. 파일명 규칙

### snake_case 사용
```
// Good
user_controller.dart
product_model.dart
auth_service.dart
shopping_cart_screen.dart

// Bad
UserController.dart    // PascalCase
usercontroller.dart   // 구분자 없음
user-controller.dart  // 하이픈 사용
```

## 6. 약어 사용 가이드

### 일반적으로 허용되는 약어
```dart
// 허용되는 약어
id (identifier)
url (uniform resource locator)
api (application programming interface)
dto (data transfer object)
db (database)

// 피해야 할 약어
usr → user
pwd → password
btn → button
msg → message
ctx → context
```

## 7. 네이밍 일관성

### 같은 개념은 같은 단어로
```dart
// Good - 일관된 용어 사용
class UserRepository {
  User getUserById(String userId);
  void deleteUser(String userId);
  List<User> getAllUsers();
}

// Bad - 혼재된 용어
class UserRepository {
  User fetchUserById(String id);      // fetch vs get
  void removeUser(String userId);     // remove vs delete
  List<User> getCustomers();         // customers vs users
}
```

## 8. 컨텍스트 고려

### 불필요한 반복 피하기
```dart
// Good
class User {
  String name;     // User.name
  String email;    // User.email
}

// Bad
class User {
  String userName;   // User.userName (중복)
  String userEmail;  // User.userEmail (중복)
}
```

### 충분한 컨텍스트 제공
```dart
// Good
String phoneNumber;
String homeAddress;
DateTime lastLoginTime;

// Bad
String number;    // 어떤 번호?
String address;   // 어떤 주소?
DateTime time;    // 어떤 시간?
```