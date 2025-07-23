import unittest
import sys
import os

# src 디렉토리를 Python 경로에 추가
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from tools.enforce_general import enforce_general_style

class TestGeneralStyle(unittest.TestCase):
    
    def test_tab_usage_detection(self):
        """탭 사용 감지 테스트"""
        code_with_tabs = """
def test_function():
\tprint("This uses tabs")
\treturn True
"""
        result = enforce_general_style(code_with_tabs, "python")
        self.assertTrue(result["has_issues"])
        self.assertIn("탭 대신 스페이스를 사용하세요", result["issues"])
    
    def test_function_length_detection(self):
        """함수 길이 감지 테스트"""
        long_function = """
def very_long_function():
    print("line 1")
    print("line 2")
    print("line 3")
    print("line 4")
    print("line 5")
    print("line 6")
    print("line 7")
    print("line 8")
    print("line 9")
    print("line 10")
    print("line 11")
    print("line 12")
    print("line 13")
    print("line 14")
    print("line 15")
    print("line 16")
    print("line 17")
    print("line 18")
    print("line 19")
    print("line 20")
    print("line 21")
    print("line 22")
    print("line 23")
    print("line 24")
    print("line 25")
    print("line 26")
    print("line 27")
    print("line 28")
    print("line 29")
    print("line 30")
    print("line 31")
    return True
"""
        result = enforce_general_style(long_function, "python")
        self.assertTrue(any("함수가 너무 깁니다" in issue for issue in result["issues"]))
    
    def test_comment_suggestion(self):
        """주석 제안 테스트"""
        code_without_comments = """
def complex_function():
    result = 0
    for i in range(100):
        result += i * 2
    return result
"""
        result = enforce_general_style(code_without_comments, "python")
        self.assertIn("복잡한 로직에 주석을 추가하세요", result["suggestions"])

if __name__ == '__main__':
    unittest.main() 