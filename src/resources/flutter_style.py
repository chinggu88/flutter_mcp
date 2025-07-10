# # Flutter 코드 스타일 가이드

# ## Dart/Flutter 특별 규칙

# ### 1. 명명 규칙
# - **변수명**: camelCase 사용 (예: `userName`, `isLoading`)
# - **함수명**: camelCase 사용 (예: `getUserData`, `onTap`)
# - **클래스명**: PascalCase 사용 (예: `UserController`, `HomePage`)
# - **상수명**: lowerCamelCase 사용 (예: `maxRetryCount`, `apiBaseUrl`)
# - **파일명**: snake_case 사용 (예: `user_controller.dart`, `home_page.dart`)

# ### 2. 위젯 구조
# ```dart
# class MyWidget extends StatelessWidget {
#   const MyWidget({super.key, required this.title});
  
#   final String title;
  
#   @override
#   Widget build(BuildContext context) {
#     return Container(
#       child: Text(title),
#     );
#   }
# }
# ```

# ### 3. GetX 컨트롤러 패턴
# ```dart
# class UserController extends GetxController {
#   static UserController get to => Get.find();
  
#   final _userName = ''.obs;
#   String get userName => _userName.value;
  
#   @override
#   void onInit() {
#     super.onInit();
#     // 초기화 로직
#   }
  
#   void updateUserName(String name) {
#     _userName.value = name;
#   }
# }
# ```

# ### 4. 상태 관리
# - GetX 사용 시 반응형 변수 활용
# - 적절한 타입 지정
# - 메모리 누수 방지

# ### 5. UI/UX 규칙
# - Material Design 가이드라인 준수
# - 반응형 디자인 고려
# - 접근성 고려
# - 다크모드 지원 