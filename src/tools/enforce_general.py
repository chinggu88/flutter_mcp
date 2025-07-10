from typing import Dict, Any
import re

def enforce_general_style(code: str, language: str = "general") -> Dict[str, Any]:
    """
    일반적인 코드 스타일을 강제하는 도구입니다.
    
    Args:
        code: 검토할 코드
        language: 프로그래밍 언어
    
    Returns:
        스타일 검토 결과 딕셔너리
    """
    issues = []
    suggestions = []
    
    # 들여쓰기 검사 (탭 사용 여부)
    if '\t' in code:
        issues.append("탭 대신 스페이스를 사용하세요")
        suggestions.append("탭을 스페이스 2개 또는 4개로 변경하세요")
    
    # 함수 길이 검사 (간단한 추정)
    lines = code.split('\n')
    function_lines = 0
    in_function = False
    
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('def ') or stripped.startswith('function ') or stripped.startswith('public ') or stripped.startswith('private '):
            in_function = True
            function_lines = 0
        elif in_function and stripped and not stripped.startswith('#'):
            function_lines += 1
        elif in_function and not stripped:
            # 빈 줄은 건너뛰기
            pass
        elif in_function and stripped.startswith('class ') or stripped.startswith('def ') or stripped.startswith('function '):
            # 새로운 함수/클래스 시작
            if function_lines > 30:
                issues.append(f"함수가 너무 깁니다 ({function_lines}줄)")
                suggestions.append("함수를 더 작은 단위로 분리하세요")
            in_function = True
            function_lines = 0
    
    # 주석 검사
    comment_lines = sum(1 for line in lines if line.strip().startswith('#'))
    code_lines = sum(1 for line in lines if line.strip() and not line.strip().startswith('#'))
    
    if code_lines > 0 and comment_lines / code_lines < 0.1:
        suggestions.append("복잡한 로직에 주석을 추가하세요")
    
    return {
        "language": language,
        "issues": issues,
        "suggestions": suggestions,
        "original_code": code,
        "has_issues": len(issues) > 0
    } 