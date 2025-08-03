import 'package:flutter_template/app/controllers/home_controller.dart';
import 'package:flutter_template/app/views/screens/home/home_screen.dart';
import 'package:get/get.dart';

class AppPages {
  static final routes = [
    GetPage(
      name: '/',
      page: () => Home_Screen(),
      binding: BindingsBuilder(() {
        // 인라인 바인딩 예제
        Get.lazyPut<HomeController>(() => HomeController());
      }), // Binding 적용
    ),
  ];
}
