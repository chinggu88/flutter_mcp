
## 1. API 구조

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