## 1. View 구조

### GetView 사용
```dart
// Good - GetView로 Controller 바인딩
class HomeScreen extends GetView<HomeController> {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Home')),
      body: Obx(() {
        if (controller.isLoading) {
          return const Center(child: CircularProgressIndicator());
        }else{
          return Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                //구성위젯1
                Widget1()
                //공백
                Sizedbox(hight:10),
                ElevatedButton(
                  onPressed: controller.refresh,
                  child: const Text('다시 시도'),
                ),
              ],
            ),
          );
          }
      }),
    );
  }

  Obx Widget1(){
    return Obx((){
      return Container(
        child:Text('${controller.index.toString()}')
      );
    });
  }
}
```

## 2. Controller 구조

### 기본 Controller 패턴
```dart
// Good - 표준 GetX Controller 구조
class UserController extends GetxController {
  static UserController to = Get.find();
  // 1. 필수 변수
  final _loading = true.obs;
  /// 로딩 유무
  bool get isLoading => _loading.value;
  set loading(bool value) => _loading.value = value;
  

  final _processstep = 0.obs;
  /// 진행 단계
  int get index => _processstep.value;
  set index(int value) => _processstep.value = value;

  
  // 2. 생명주기 메서드
  @override
  void onInit() {
    super.onInit();
    ever(_processstep, (_) {
      if(_processstep.value == 5){
        ///로딩 종료
        _isLoading = false;
      }
    });

    loadUsers();
  }

  @override
  void onClose() {
    // 리소스 정리
    super.onClose();
  }


  // 3. Public methods 
  Future<void> loadUsers() async {
    try {
      final users = await _userRepository.getUsers();
      _processstep++;
    } catch (e) {
      _setError('Failed to load users: ${e.toString()}');
    }
  }
}
```