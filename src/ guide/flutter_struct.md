# Flutter 프로젝트 폴더 구조
lib/
├── core/                  ← 앱 전역 설정 및 공통 서비스
│   ├── config/            ← 라우팅, 테마, 상수 등
│   ├── services/          ← API 통신, DB 처리 등 공통 로직
│   └── utils/             ← 공용 유틸리티 함수
│
├── data/                  ← 공통 모델 및 리포지토리 계층
│   ├── models/
│   ├── dtos/
│   └── repositories/
│
├── features/              ← 각 기능별 화면 구성
│   └── {feature_name}/
│       ├── view/          ← UI 화면 구성
│       ├── controller/    ← 상태관리 및 MCP 통신
│       ├── model/         ← 전용 모델
│       └── widgets/       ← 해당 기능 내 소형 위젯
│
├── shared/                ← 전역 공용 위젯 및 테마
│   ├── widgets/
│   └── themes/
│
└── main.dart              ← 진입점