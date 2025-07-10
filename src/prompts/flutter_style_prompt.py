import mcp

def create_flutter_struct_prompt(code: str) -> str:
    """
    Flutter 프로젝트 폴더 구조 검토를 위한 프롬프트를 생성합니다.
    """
    return f"""
    """

def create_flutter_style_prompt(code: str) -> str:
    """
    Flutter/Dart 코드 스타일 검토를 위한 프롬프트를 생성합니다.
    
    Args:
        code: 검토할 Flutter/Dart 코드
    
    Returns:
        Flutter 스타일 검토 프롬프트 문자열
    """
    return f"""
다음 Flutter/Dart 코드를 검토하고 Flutter 스타일 가이드에 맞게 개선해주세요:

```dart
{code}
```

다음 기준으로 검토해주세요:
1. Dart/Flutter 명명 규칙
   - 변수명: camelCase
   - 클래스명: PascalCase
   - 파일명: snake_case
2. 위젯 구조와 const 생성자 활용
3. GetX 컨트롤러 패턴 (사용 시)
4. 상태 관리와 반응형 변수
5. Material Design 가이드라인
6. 성능 최적화 (불필요한 rebuild 방지)
7. 접근성과 다크모드 지원

개선된 코드와 함께 개선 사항을 설명해주세요.
""" 