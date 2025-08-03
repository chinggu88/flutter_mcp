import 'package:flutter/material.dart';
import 'package:get/get.dart';

class AppController extends GetxController {
  static AppController to = Get.find();

  final _bottomindex = 0.obs;

  ///바텀네비게이션 인덱스
  int get bottomIndex => _bottomindex.value;
  set bottomIndex(int value) => _bottomindex.value = value;

  @override
  void onInit() {
    super.onInit();
  }
}
