import 'dart:developer';

import 'package:flutter_template/app/models/item.dart';

import '../services/api_service.dart';

class ApiRepository {
  static final ApiService _apiService = ApiService.instance;

  static Future<List<Item>> fetchItemssData() async {
    List<Item> temp = [];
    try {
      final response = await _apiService.get('/items');

      /// 비즈니스 로직 수행
      response.data.toList().forEach((element) {
        temp.add(Item.fromJson(element));
      });
      return temp;
    } catch (e) {
      return temp;
    }
  }
}
