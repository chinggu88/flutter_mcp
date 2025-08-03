import 'package:flutter/material.dart';
import 'package:flutter_template/app/controllers/home_controller.dart';
import 'package:get/get.dart';

class Home_Screen extends GetView<HomeController> {
  const Home_Screen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: const Text('Home'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text('You have pushed the button this many times:'),
            Obx(
              () => Text(
                '${controller.count}',
                style: Theme.of(context).textTheme.headlineMedium,
              ),
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () => controller.count++,
        tooltip: 'Increment',
        child: const Icon(Icons.add),
      ),
    );
  }
}
