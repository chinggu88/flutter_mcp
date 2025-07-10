def create_general_style_prompt(code: str, language: str = "general") -> str:
    """
    일반적인 코드 스타일 검토를 위한 프롬프트를 생성합니다.
    
    Args:
        code: 검토할 코드
        language: 프로그래밍 언어 (기본값: "general")
    
    Returns:
        스타일 검토 프롬프트 문자열
    """
    return f"""
다음 {language} 코드를 검토하고 스타일 가이드에 맞게 개선해주세요:

```{language}
{code}
```

다음 기준으로 검토해주세요:
1. 명명 규칙 (camelCase, PascalCase, UPPER_SNAKE_CASE)
2. 들여쓰기와 공백
3. 주석과 문서화
4. 코드 구조와 함수 길이
5. 에러 처리
6. 전반적인 가독성

개선된 코드와 함께 개선 사항을 설명해주세요.
""" 