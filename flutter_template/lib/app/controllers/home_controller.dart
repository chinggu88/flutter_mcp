import 'dart:developer';

import 'package:flutter_template/app/models/item.dart';
import 'package:get/get.dart';
import '../data/repositories/api_repository.dart';

class HomeController extends GetxController {
  static HomeController to = Get.find();

  // 1. 필수 변수
  final _loading = true.obs;

  /// 로딩 유무
  bool get isLoading => _loading.value;
  set loading(bool value) => _loading.value = value;

  final _count = 0.obs;

  /// 카운터 변수
  int get count => _count.value;
  set count(int value) => _count.value = value;

  final _users = <Item>[].obs;

  /// 아이템 정보
  List<Item> get users => _users;
  set users(List<Item> value) => _users.value = value;

  // 2. 생명주기 메서드
  @override
  void onInit() {
    super.onInit();
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
      loading = true;
      // 사용자 로딩 로직
    } catch (e) {
      log('Failed to load users: ${e.toString()}');
    } finally {
      loading = false;
    }
  }

  Future<void> fetchRootData() async {
    try {
      loading = true;

      List<Item> result = await ApiRepository.fetchItemssData();

      if (result.isNotEmpty) {
        log('API fetchRootData Response: ${result.toList(growable: false)}');
        users.addAll(result);
        Get.snackbar(
          'Success',
          'Data fetched successfully',
          snackPosition: SnackPosition.BOTTOM,
        );
      }
    } catch (e) {
      log('Failed to fetch data: ${e.toString()}');
      Get.snackbar(
        'Error',
        'Failed to fetch data: ${e.toString()}',
        snackPosition: SnackPosition.BOTTOM,
      );
    } finally {
      loading = false;
    }
  }
}
