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
## 3. API 구조

### 기본 DIO 패턴
```dart
import 'package:dio/dio.dart';

class ApiService {
  static ApiService? _instance;
  late Dio _dio;

  ApiService._internal() {
    _dio = Dio(
      BaseOptions(
        baseUrl: 'baseurl',
        connectTimeout: const Duration(seconds: 30),
        receiveTimeout: const Duration(seconds: 30),
        headers: {'Content-Type': 'application/json'},
      ),
    );
  }

  static ApiService get instance {
    _instance ??= ApiService._internal();
    return _instance!;
  }

  Future<Response> get(
    String path, {
    Map<String, dynamic>? queryParameters,
    Options? options,
    CancelToken? cancelToken,
    ProgressCallback? onReceiveProgress,
  }) async {
    try {
      final response = await _dio.get(
        path,
        queryParameters: queryParameters,
        options: options,
        cancelToken: cancelToken,
        onReceiveProgress: onReceiveProgress,
      );
      return response;
    } catch (e) {
      rethrow;
    }
  }

  Future<Response> post(
    String path, {
    dynamic data,
    Map<String, dynamic>? queryParameters,
    Options? options,
    CancelToken? cancelToken,
    ProgressCallback? onSendProgress,
    ProgressCallback? onReceiveProgress,
  }) async {
    try {
      final response = await _dio.post(
        path,
        data: data,
        queryParameters: queryParameters,
        options: options,
        cancelToken: cancelToken,
        onSendProgress: onSendProgress,
        onReceiveProgress: onReceiveProgress,
      );
      return response;
    } catch (e) {
      rethrow;
    }
  }

}
```
### 기본 DIO 패턴
```dart
class ApiRepository {
  static final ApiService _apiService = ApiService.instance;
  //리스트 형일때
  static Future<List<Item>> fetchItemssData() async {
    List<Item> temp = [];
    try {
      final response = await _apiService.get('/items');
      response.data.toList().forEach((element) {
        temp.add(Item.fromJson(element));
      });
      return temp;
    } catch (e) {
      return temp;
    }
  }
  //일반모델
  static Future<Item> fetchItemssData() async {
    Item temp = Item();
    try {
      final response = await _apiService.get('/items');
      temp = Item.fromJson(response.data);
      return temp;
    } catch (e) {
      return temp;
    }
  }
  
}
```