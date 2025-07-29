# 주석 작성 규칙 (Comment Rules)

## 1. 주석보다 코드로 표현

### 자명한 코드 작성
```dart
// Bad - 주석에 의존
// 사용자의 나이가 18세 이상인지 확인
if (user.age >= 18) {
  // 성인 처리
}

// Good - 코드로 의도 표현
bool isAdult(User user) => user.age >= 18;

if (isAdult(user)) {
  processAdultUser(user);
}
```

## 2. 필요한 주석

### 법적 정보
```dart
// Copyright (c) 2024 Company Name. All rights reserved.
// This source code is licensed under the MIT license found in the
// LICENSE file in the root directory of this source tree.
```

### 복잡한 알고리즘 설명
```dart
// Good - 복잡한 로직 설명
/// Binary search implementation
/// Time complexity: O(log n)
/// Space complexity: O(1)
int binarySearch(List<int> arr, int target) {
  // 이진 탐색은 정렬된 배열에서만 작동
  var left = 0;
  var right = arr.length - 1;
  
  while (left <= right) {
    // 오버플로우 방지: (left + right) / 2 대신 사용
    final mid = left + (right - left) ~/ 2;
    
    if (arr[mid] == target) return mid;
    if (arr[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  
  return -1;
}
```

### 의도 설명
```dart
// Good - 비즈니스 로직 의도
class PriceCalculator {
  double calculatePrice(Product product, User user) {
    var price = product.basePrice;
    
    // 프리미엄 회원은 항상 20% 할인
    // (마케팅팀 요청 - 2024.01.15)
    if (user.isPremium) {
      price *= 0.8;
    }
    
    // 첫 구매 고객 추가 10% 할인
    // 단, 프리미엄 할인과 중복 적용 가능
    if (user.purchaseCount == 0) {
      price *= 0.9;
    }
    
    return price;
  }
}
```

### 경고 및 주의사항
```dart
// WARNING: 이 메서드는 thread-safe하지 않습니다.
// 멀티스레드 환경에서는 동기화 필요
void updateCache(String key, dynamic value) {
  _cache[key] = value;
}

// FIXME: 임시 해결책 - 성능 이슈로 인해 추후 리팩토링 필요
// 현재는 전체 리스트를 순회하고 있음
User? findUserByEmail(String email) {
  return users.firstWhere((u) => u.email == email);
}
```

## 3. 문서화 주석 (Doc Comments)

### 클래스 문서화
```dart
/// 사용자 인증을 처리하는 서비스
/// 
/// JWT 토큰 기반 인증을 제공하며, 
/// 자동 토큰 갱신 기능을 포함합니다.
/// 
/// Example:
/// ```dart
/// final authService = AuthService();
/// final token = await authService.login(email, password);
/// ```
class AuthService {
  // 구현...
}
```

### 메서드 문서화
```dart
/// 이메일과 비밀번호로 사용자 로그인
/// 
/// [email] 사용자 이메일 주소
/// [password] 사용자 비밀번호
/// 
/// Returns: JWT 액세스 토큰
/// 
/// Throws:
/// - [InvalidCredentialsException] 잘못된 인증 정보
/// - [NetworkException] 네트워크 연결 실패
Future<String> login(String email, String password) async {
  // 구현...
}
```

### 복잡한 매개변수 설명
```dart
/// 페이지네이션된 사용자 목록 조회
/// 
/// [page] 페이지 번호 (1부터 시작)
/// [pageSize] 페이지당 항목 수 (기본값: 20, 최대: 100)
/// [sortBy] 정렬 기준 ('name', 'email', 'createdAt')
/// [sortOrder] 정렬 순서 ('asc' 또는 'desc')
/// [filters] 필터 조건 맵
///   - 'status': 'active' | 'inactive' | 'all'
///   - 'role': 'admin' | 'user' | 'guest'
///   - 'search': 이름 또는 이메일 검색어
Future<PagedResult<User>> getUsers({
  int page = 1,
  int pageSize = 20,
  String sortBy = 'createdAt',
  String sortOrder = 'desc',
  Map<String, String>? filters,
}) async {
  // 구현...
}
```

## 4. TODO 주석

### 구체적인 TODO
```dart
// Good - 구체적이고 추적 가능
// TODO(john): 캐시 만료 로직 구현 (JIRA-1234)
// 예상 완료: 2024.02.15
void getCachedData(String key) {
  return _cache[key];  // 현재는 만료 체크 없음
}

// Bad - 너무 모호함
// TODO: 나중에 수정
// TODO: 개선 필요
```

## 5. 피해야 할 주석

### 당연한 내용
```dart
// Bad - 자명한 코드에 불필요한 주석
// 사용자 이름을 반환
String getUserName() {
  return user.name;
}

// i를 1 증가
i++;
```

### 주석으로 감싼 코드
```dart
// Bad - 사용하지 않는 코드는 삭제
void processOrder(Order order) {
  validateOrder(order);
  // calculateShipping(order);  // 삭제하지 말고 제거
  // applyTax(order);          // Git에서 히스토리 확인 가능
  chargePayment(order);
}
```

### 닫는 괄호 표시
```dart
// Bad - IDE가 알려줌
class LongClass {
  void method1() {
    // 많은 코드...
  } // method1 끝  <- 불필요
  
  void method2() {
    // 많은 코드...
  } // method2 끝  <- 불필요
} // LongClass 끝   <- 불필요
```

## 6. 주석 유지보수

### 코드와 동기화
```dart
// Bad - 코드와 주석 불일치
// 3번 재시도
for (int i = 0; i < 5; i++) {  // 실제로는 5번
  tryConnect();
}

// Good - 상수로 의도 표현
const int maxRetryAttempts = 5;
for (int i = 0; i < maxRetryAttempts; i++) {
  tryConnect();
}
```

### 정기적인 주석 검토
```dart
// Good - 날짜와 담당자 명시
// DEPRECATED: 2024.03.01부터 v2 API 사용 권장
// 2024.06.01 완전 제거 예정 (담당: tech-team)
@Deprecated('Use v2 API instead')
Future<Response> oldApiCall() {
  // 구현...
}
```