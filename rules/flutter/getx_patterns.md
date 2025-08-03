# GetX 패턴 규칙 (GetX Patterns)
```dart
  // 1. 의존성 주입
  static UserController to = Get.find();

  // 2. 상태 변수 (타입별 obs 패턴)
  // Bool 타입
  final _isLoading = false.obs;
  bool get isLoading => _isLoading.value;
  set isLoading(bool value) => _isLoading.value = value;
  
  // String 타입
  final _message = ''.obs;
  String get message => _message.value;
  set message(String value) => _message.value = value;
  
  // int 타입
  final _count = 0.obs;
  int get count => _count.value;
  set count(int value) => _count.value = value;
  
  // double 타입
  final _price = 0.0.obs;
  double get price => _price.value;
  set price(double value) => _price.value = value;
  
  // List 타입
  final _users = <User>[].obs;
  List<User> get users => _users.value;
  set users(List<User> value) => _users.assignAll(value);
  
  
  // Custom Object 타입
  final _user = <User>().obs;
  User get user => _user.value;
  set user(User value) => _user.value = value;
  
  // DateTime 타입
  final _selectedDate = Rx<DateTime?>(null);
  DateTime? get selectedDate => _selectedDate.value;
  set selectedDate(DateTime? value) => _selectedDate.value = value;
```
## 2. Binding 패턴

### 페이지별 바인딩
```dart
// Good - 페이지별 의존성 바인딩
class HomeBinding extends Bindings {
  @override
  void dependencies() {
    // Lazy 초기화 (사용할 때 생성)
    Get.lazyPut<HomeController>(() => HomeController());
    Get.lazyPut<ProductService>(() => ProductService());
    
    // 즉시 생성 (필요한 경우)
    Get.put<NotificationService>(NotificationService());
  }
}

// 라우트에서 바인딩 사용
class AppPages {
  static final routes = [
    GetPage(
      name: Routes.HOME,
      page: () => const HomeScreen(),
      binding: HomeBinding(),
    ),
    GetPage(
      name: Routes.PROFILE,
      page: () => const ProfileScreen(),
      binding: ProfileBinding(),
    ),
  ];
}
```

### 초기 바인딩 (전역)
```dart
// Good - 앱 전체에서 사용할 서비스들
class InitialBinding extends Bindings {
  @override
  void dependencies() {
    // 싱글톤으로 앱 전체에서 사용
    Get.put<AuthController>(AuthController(), permanent: true);
    Get.put<ThemeController>(ThemeController(), permanent: true);
    Get.put<NetworkService>(NetworkService(), permanent: true);
    
    // 레포지토리 계층
    Get.put<ApiClient>(ApiClient());
    Get.put<StorageService>(StorageService());
    Get.put<UserRepository>(UserRepository());
  }
}
```

## 3. Navigation 패턴

### 라우트 관리
```dart
// Good - 체계적인 라우트 관리
class Routes {
  static const home = '/home';
  static const profile = '/profile';
  static const settings = '/settings';
  static const login = '/login';
  
  // 동적 라우트
  static String userDetail(String userId) => '/user/$userId';
  static String productDetail(String productId) => '/product/$productId';
}

// Navigation 패턴
class NavigationService {
  // 기본 네비게이션
  static void toHome() {
    Get.toNamed(Routes.home);
  }
  
  static void toProfile() {
    Get.toNamed(Routes.profile);
  }
  
  // 데이터와 함께 네비게이션
  static void toUserDetail(String userId) {
    Get.toNamed(
      Routes.userDetail(userId),
      arguments: {'userId': userId},
    );
  }
  
  // 결과 받기
  static Future<T?> toSettingsAndWaitResult<T>() {
    return Get.toNamed<T>(Routes.settings);
  }
  
  // 스택 교체
  static void replaceWithLogin() {
    Get.offAllNamed(Routes.login);
  }
}
```

### 대화상자 및 스낵바 패턴
```dart
// Good - 일관된 UI 피드백
class UIService {
  // 로딩 다이얼로그
  static void showLoading([String? message]) {
    Get.dialog(
      AlertDialog(
        content: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            const CircularProgressIndicator(),
            if (message != null) ...[
              const SizedBox(height: 16),
              Text(message),
            ],
          ],
        ),
      ),
      barrierDismissible: false,
    );
  }
  
  static void hideLoading() {
    if (Get.isDialogOpen == true) {
      Get.back();
    }
  }
  
  // 확인 다이얼로그
  static Future<bool> showConfirm({
    required String title,
    required String message,
    String confirmText = '확인',
    String cancelText = '취소',
  }) async {
    final result = await Get.dialog<bool>(
      AlertDialog(
        title: Text(title),
        content: Text(message),
        actions: [
          TextButton(
            onPressed: () => Get.back(result: false),
            child: Text(cancelText),
          ),
          TextButton(
            onPressed: () => Get.back(result: true),
            child: Text(confirmText),
          ),
        ],
      ),
    );
    return result ?? false;
  }
  
  // 스낵바
  static void showSuccess(String message) {
    Get.snackbar(
      '성공',
      message,
      backgroundColor: Colors.green,
      colorText: Colors.white,
      icon: const Icon(Icons.check, color: Colors.white),
    );
  }
  
  static void showError(String message) {
    Get.snackbar(
      '오류',
      message,
      backgroundColor: Colors.red,
      colorText: Colors.white,
      icon: const Icon(Icons.error, color: Colors.white),
    );
  }
}
```

## 5. View 패턴



## 6. 서비스 패턴

### API 서비스 구조
```dart
// Good - Repository + Service 패턴
class UserRepository {
  final ApiClient _apiClient = Get.find<ApiClient>();

  Future<List<User>> getUsers() async {
    try {
      final response = await _apiClient.get('/users');
      return (response.data as List)
          .map((json) => User.fromJson(json))
          .toList();
    } catch (e) {
      throw RepositoryException('Failed to fetch users: $e');
    }
  }

  Future<User> createUser(CreateUserRequest request) async {
    try {
      final response = await _apiClient.post(
        '/users',
        data: request.toJson(),
      );
      return User.fromJson(response.data);
    } catch (e) {
      throw RepositoryException('Failed to create user: $e');
    }
  }
}
```

## 7. 테스트 패턴

### Controller 테스트
```dart
// Good - GetX Controller 테스트

```