from typing import Dict, Any
import re

def enforce_flutter_style(code: str) -> Dict[str, Any]:
    """
    Flutter/Dart 코드 스타일을 강제하는 도구입니다.
    
    Args:
        code: 검토할 Flutter/Dart 코드
    
    Returns:
        Flutter 스타일 검토 결과 딕셔너리
    """
    issues = []
    suggestions = []
    
    lines = code.split('\n')
    
    # const 생성자 검사
    widget_pattern = r'class\s+(\w+)\s+extends\s+(StatelessWidget|StatefulWidget)'
    widget_matches = re.findall(widget_pattern, code)
    
    for widget_name, widget_type in widget_matches:
        # const 생성자 패턴 검사
        const_pattern = rf'const\s+{widget_name}\s*\('
        if not re.search(const_pattern, code):
            suggestions.append(f"{widget_name} 클래스에 const 생성자를 추가하세요")
    
    # GetX 컨트롤러 패턴 검사
    if 'GetxController' in code:
        # static getter 패턴 검사
        static_pattern = r'static\s+\w+\s+get\s+to\s*=>\s*Get\.find\(\)'
        if not re.search(static_pattern, code):
            suggestions.append("GetX 컨트롤러에 static getter를 추가하세요")
        
        # 반응형 변수 패턴 검사
        obs_pattern = r'\.obs'
        if not re.search(obs_pattern, code):
            suggestions.append("GetX 컨트롤러에서 반응형 변수를 활용하세요")
    
    # 명명 규칙 검사
    # 클래스명이 PascalCase인지 검사
    class_pattern = r'class\s+([a-z][a-zA-Z0-9]*)'
    class_matches = re.findall(class_pattern, code)
    for class_name in class_matches:
        if not class_name[0].isupper():
            issues.append(f"클래스명 '{class_name}'은 PascalCase를 사용해야 합니다")
    
    # 변수명이 camelCase인지 검사 (간단한 검사)
    var_pattern = r'(\w+)\s*=\s*[^=]'
    var_matches = re.findall(var_pattern, code)
    for var_name in var_matches:
        if var_name and not var_name.startswith('_') and not var_name[0].islower():
            if not var_name.isupper():  # 상수가 아닌 경우
                issues.append(f"변수명 '{var_name}'은 camelCase를 사용해야 합니다")
    
    # 위젯 구조 검사
    if 'StatelessWidget' in code or 'StatefulWidget' in code:
        if 'super.key' not in code:
            suggestions.append("위젯 생성자에 super.key를 추가하세요")
        
        if 'required this.' not in code and 'final ' in code:
            suggestions.append("필수 매개변수에 required 키워드를 사용하세요")
    
    return {
        "language": "dart",
        "issues": issues,
        "suggestions": suggestions,
        "original_code": code,
        "has_issues": len(issues) > 0
    } 