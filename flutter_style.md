# Flutter 코드 스타일 가이드

## Dart/Flutter 특별 규칙

### 1. 명명 규칙
- **변수명**: camelCase 사용 (예: `userName`, `isLoading`)
- **함수명**: camelCase 사용 (예: `getUserData`, `onTap`)
- **클래스명**: PascalCase 사용 (예: `UserController`, `HomePage`)
- **상수명**: lowerCamelCase 사용 (예: `maxRetryCount`, `apiBaseUrl`)
- **파일명**: snake_case 사용 (예: `user_controller.dart`, `home_page.dart`)

### 2. 위젯 구조
```dart
class MyWidget extends StatelessWidget {
  const MyWidget({super.key, required this.title});
  
  final String title;
  
  @override
  Widget build(BuildContext context) {
    return Container(
      child: Text(title),
    );
  }
}
```

### 3. GetX 컨트롤러 패턴
```dart
class UserController extends GetxController {
  static UserController get to => Get.find();
  
  final _userName = ''.obs;
  String get userName => _userName.value;
  set userName(String value)_userName.value = value;
  
  @override
  void onInit() {
    super.onInit();
    // 초기화 로직
  }
}
```

### 4. 상태 관리
- GetX 사용 시 반응형 변수 활용
- 적절한 타입 지정
- 메모리 누수 방지

### 5. UI/UX 규칙
- Material Design 가이드라인 준수
- 반응형 디자인 고려
- 접근성 고려
- 다크모드 지원

### 6. 성능 최적화
- const 생성자 활용
- 불필요한 rebuild 방지
- 이미지 캐싱 활용
- 메모리 효율적인 위젯 구조

### 7. 테스트
- 단위 테스트 작성
- 위젯 테스트 활용
- 통합 테스트 고려 