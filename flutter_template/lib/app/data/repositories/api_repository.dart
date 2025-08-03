import 'package:flutter_template/app/models/item.dart';

import '../services/api_service.dart';

class ApiRepository {
  static final ApiService _apiService = ApiService.instance;

  static Future<List<Item>> fetchItemssData() async {
    List<Item> temp = [];
    try {
      final response = await _apiService.get('/items');
      response.data;
      return temp;
    } catch (e) {
      return temp;
    }
  }
}
