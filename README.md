# FastMCP Style Enforcer

코드 스타일을 자동으로 검토하고 개선 사항을 제안하는 FastMCP 서버입니다.

## 기능

- **일반 코드 스타일 검토**: 다양한 프로그래밍 언어의 기본 스타일 규칙 검토
- **Flutter/Dart 스타일 검토**: Flutter 프로젝트에 특화된 스타일 가이드 적용
- **자동화된 검토**: 코드 분석을 통한 자동 스타일 이슈 감지
- **개선 제안**: 구체적인 개선 방안 제시

## 설치

```bash
# 의존성 설치
pip install -r requirements.txt
```

## 사용법

### 서버 실행

```bash
cd fastmcp-style-enforcer
python src/server.py
```

### 테스트 실행

```bash
# 일반 스타일 테스트
python tests/test_general.py

# Flutter 스타일 테스트
python tests/test_flutter.py
```

## 프로젝트 구조

```
fastmcp-style-enforcer/
├── CODE_STYLE.md          # 일반 코드 스타일 가이드
├── flutter_style.md       # Flutter 스타일 가이드
├── src/
│   ├── server.py          # FastMCP 서버 진입점
│   ├── resources/         # 스타일 가이드 리소스
│   ├── prompts/           # 프롬프트 생성 모듈
│   └── tools/             # 스타일 검토 도구
├── tests/                 # 테스트 파일
├── requirements.txt       # 의존성 목록
└── README.md             # 프로젝트 문서
```

## 지원하는 스타일 규칙

### 일반 코드 스타일
- 명명 규칙 (camelCase, PascalCase, UPPER_SNAKE_CASE)
- 들여쓰기 (탭 대신 스페이스 사용)
- 주석 및 문서화
- 함수 길이 및 구조
- 에러 처리

### Flutter/Dart 스타일
- Dart 명명 규칙
- 위젯 구조 및 const 생성자
- GetX 컨트롤러 패턴
- 상태 관리 및 반응형 변수
- Material Design 가이드라인
- 성능 최적화

## 기여하기

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 