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