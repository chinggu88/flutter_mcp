# 코드 포맷팅 규칙 (Code Formatting)

## 1. 들여쓰기

### 2 spaces 사용
```dart
// Good
class User {
  String name;
  int age;
  
  void greet() {
    if (age >= 18) {
      print('Hello, adult $name');
    } else {
      print('Hello, young $name');
    }
  }
}

// Bad - tab 또는 4 spaces
class User {
    String name;  // 4 spaces
    int age;
}
```

## 2. 줄 길이

### 80자 제한 권장
```dart
// Good
final String message = 'This is a reasonably short line that fits well';

final List<String> items = [
  'item1',
  'item2', 
  'item3',
];

// Bad - 너무 긴 줄
final String veryLongMessage = 'This is an extremely long line that extends way beyond the recommended 80 character limit and becomes hard to read';
```

### 긴 줄 분할
```dart
// Good - 파라미터 분할
User createUser({
  required String name,
  required String email,
  required String phone,
  String? address,
}) {
  return User(
    name: name,
    email: email,
    phone: phone,
    address: address,
  );
}

// Good - 메서드 체이닝 분할
final result = users
    .where((user) => user.isActive)
    .map((user) => user.name)
    .toList();
```

## 3. 공백 사용

### 연산자 주위 공백
```dart
// Good
int sum = a + b;
bool isValid = age >= 18 && hasPermission;
String fullName = firstName + ' ' + lastName;

// Bad
int sum=a+b;
bool isValid=age>=18&&hasPermission;
```

### 쉼표 뒤 공백
```dart
// Good
final List<String> fruits = ['apple', 'banana', 'orange'];
void process(String name, int age, bool isActive) {}

// Bad
final List<String> fruits = ['apple','banana','orange'];
void process(String name,int age,bool isActive) {}
```

### 괄호 내부 공백 없음
```dart
// Good
if (isValid) {
  process(name, age);
}

final result = calculate(a, b, c);

// Bad
if ( isValid ) {
  process( name, age );
}
```

## 4. 중괄호 스타일

### K&R 스타일 (same line)
```dart
// Good
if (condition) {
  doSomething();
} else {
  doSomethingElse();
}

class MyClass {
  void method() {
    // 구현
  }
}

// Bad - Allman 스타일
if (condition) 
{
  doSomething();
}
```

## 5. 빈 줄 사용

### 논리적 그룹 분리
```dart
// Good
class UserService {
  final UserRepository repository;
  final EmailService emailService;
  
  UserService(this.repository, this.emailService);
  
  // 조회 메서드 그룹
  User? findById(String id) {
    return repository.findById(id);
  }
  
  List<User> findAll() {
    return repository.findAll();
  }
  
  // 저장 메서드 그룹
  Future<void> save(User user) async {
    await repository.save(user);
    await emailService.sendWelcome(user);
  }
  
  Future<void> delete(String id) async {
    await repository.delete(id);
  }
}
```

### 메서드 간 구분
```dart
// Good
class Calculator {
  int add(int a, int b) {
    return a + b;
  }
  
  int subtract(int a, int b) {
    return a - b;
  }
  
  int multiply(int a, int b) {
    return a * b;
  }
}
```

## 6. 수직 정렬

### 관련 코드 정렬
```dart
// Good - 변수 정렬
final String    firstName = 'John';
final String    lastName  = 'Doe';
final int       age       = 30;
final bool      isActive  = true;

// Good - 함수 인자 정렬
void configureUser({
  required String  name,
  required String  email,
           int?    age,
           bool    isActive = false,
}) {}
```

## 7. Import 정렬

### 그룹별 정렬
```dart
// Good - 그룹별 정렬 및 공백
// Dart SDK
import 'dart:async';
import 'dart:io';

// Flutter
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

// 외부 패키지
import 'package:dio/dio.dart';
import 'package:get/get.dart';

// 프로젝트 내부
import '../models/user.dart';
import '../services/auth_service.dart';
import 'user_controller.dart';
```

## 8. 컬렉션 포맷팅

### 짧은 컬렉션 - 한 줄
```dart
// Good
final List<int> numbers = [1, 2, 3, 4];
final Map<String, String> config = {'host': 'localhost', 'port': '8080'};
```

### 긴 컬렉션 - 여러 줄
```dart
// Good - 각 항목을 새 줄에
final List<String> longList = [
  'first_very_long_item_name',
  'second_very_long_item_name', 
  'third_very_long_item_name',
  'fourth_very_long_item_name',
];

final Map<String, dynamic> userConfig = {
  'name': 'John Doe',
  'email': 'john@example.com',
  'preferences': {
    'theme': 'dark',
    'language': 'ko',
    'notifications': true,
  },
};
```

### 위젯 트리 포맷팅
```dart
// Good - Flutter 위젯 포맷팅
Widget build(BuildContext context) {
  return Scaffold(
    appBar: AppBar(
      title: Text('User Profile'),
      backgroundColor: Colors.blue,
    ),
    body: Column(
      children: [
        Container(
          padding: EdgeInsets.all(16),
          child: Text(
            'Welcome, ${user.name}!',
            style: TextStyle(
              fontSize: 24,
              fontWeight: FontWeight.bold,
            ),
          ),
        ),
        Expanded(
          child: ListView.builder(
            itemCount: items.length,
            itemBuilder: (context, index) {
              return ListTile(
                title: Text(items[index].title),
                subtitle: Text(items[index].description),
                onTap: () => onItemTap(items[index]),
              );
            },
          ),
        ),
      ],
    ),
  );
}
```

## 9. 조건문 포맷팅

### 단순 조건문
```dart
// Good - 한 줄
if (isValid) return result;

// Good - 블록
if (isValid) {
  processResult(result);
  logSuccess();
}
```

### 복잡한 조건문
```dart
// Good - 조건 분할
if (user.isActive &&
    user.hasPermission &&
    user.subscription.isValid) {
  grantAccess();
}

// Good - 중간 변수 사용
final bool canAccess = user.isActive &&
                      user.hasPermission &&
                      user.subscription.isValid;

if (canAccess) {
  grantAccess();
}
```

## 10. 자동 포맷팅 도구

### dart format 사용
```bash
# 프로젝트 전체 포맷팅
dart format .

# 특정 파일 포맷팅
dart format lib/main.dart

# 체크만 (CI에서 사용)
dart format --output=none --set-exit-if-changed .
```

### VS Code 설정
```json
{
  "editor.formatOnSave": true,
  "dart.lineLength": 80,
  "[dart]": {
    "editor.rulers": [80],
    "editor.tabSize": 2,
    "editor.insertSpaces": true
  }
}
```