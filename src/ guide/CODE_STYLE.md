# 코드 스타일 가이드

## 일반적인 코딩 스타일 규칙

### 1. 명명 규칙
- **변수명**: camelCase 사용 (예: `userName`, `isActive`)
- **함수명**: camelCase 사용 (예: `getUserData`, `validateInput`)
- **클래스명**: PascalCase 사용 (예: `UserController`, `DataService`)
- **상수명**: UPPER_SNAKE_CASE 사용 (예: `MAX_RETRY_COUNT`, `API_BASE_URL`)

### 2. 들여쓰기
- 탭 대신 스페이스 2개 또는 4개 사용
- 일관성 유지

### 3. 주석
- 복잡한 로직에는 반드시 주석 추가
- 함수/클래스 상단에 docstring 작성
- TODO, FIXME 태그 활용

### 4. 코드 구조
- 한 함수는 한 가지 역할만 수행
- 함수 길이는 20-30줄 이내 권장
- 적절한 공백으로 가독성 향상

### 5. 에러 처리
- 예외 상황 고려
- 적절한 에러 메시지 제공
- 로깅 활용

## 언어별 특별 규칙

### Python
- PEP 8 스타일 가이드 준수
- 타입 힌트 사용 권장
- 가상환경 활용

### JavaScript/TypeScript
- ESLint 규칙 준수
- 타입 정의 명확히
- 모듈화된 구조

### Java
- Java Code Conventions 준수
- 접근 제어자 적절히 사용
- 예외 처리 철저히 