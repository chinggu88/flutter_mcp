import unittest
import sys
import os

# src 디렉토리를 Python 경로에 추가
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from tools.enforce_flutter import enforce_flutter_style

class TestFlutterStyle(unittest.TestCase):
    
    def test_const_constructor_suggestion(self):
        """const 생성자 제안 테스트"""
        widget_without_const = """
class MyWidget extends StatelessWidget {
  MyWidget({required this.title});
  
  final String title;
  
  @override
  Widget build(BuildContext context) {
    return Container(
      child: Text(title),
    );
  }
}
"""
        result = enforce_flutter_style(widget_without_const)
        self.assertIn("MyWidget 클래스에 const 생성자를 추가하세요", result["suggestions"])
    
    def test_getx_controller_pattern(self):
        """GetX 컨트롤러 패턴 테스트"""
        controller_without_static = """
class UserController extends GetxController {
  final _userName = ''.obs;
  String get userName => _userName.value;
  
  @override
  void onInit() {
    super.onInit();
  }
}
"""
        result = enforce_flutter_style(controller_without_static)
        self.assertIn("GetX 컨트롤러에 static getter를 추가하세요", result["suggestions"])
    
    def test_class_naming_convention(self):
        """클래스 명명 규칙 테스트"""
        class_with_lowercase = """
class myWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container();
  }
}
"""
        result = enforce_flutter_style(class_with_lowercase)
        self.assertIn("클래스명 'myWidget'은 PascalCase를 사용해야 합니다", result["issues"])
    
    def test_widget_structure(self):
        """위젯 구조 테스트"""
        widget_without_super_key = """
class TestWidget extends StatelessWidget {
  TestWidget({required this.title});
  
  final String title;
  
  @override
  Widget build(BuildContext context) {
    return Text(title);
  }
}
"""
        result = enforce_flutter_style(widget_without_super_key)
        self.assertIn("위젯 생성자에 super.key를 추가하세요", result["suggestions"])

if __name__ == '__main__':
    unittest.main() 