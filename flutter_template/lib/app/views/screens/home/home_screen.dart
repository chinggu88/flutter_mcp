import 'package:flutter/material.dart';
import 'package:flutter_template/app/controllers/home_controller.dart';
import 'package:get/get.dart';

class Home_Screen extends GetView<HomeController> {
  const Home_Screen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(),
      body: Obx(
        () =>
            controller.isLoading
                ? const CircularProgressIndicator()
                : Column(children: [itemslist()]),
      ),
    );
  }

  Obx itemslist() {
    return Obx(() {
      return Column(
        children:
            controller.items.map((item) {
              return ListTile(
                title: Text(item.name ?? ''),
                subtitle: Text(item.description ?? ''),
              );
            }).toList(),
      );
    });
  }
}
