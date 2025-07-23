fastmcp-style-enforcer/
├── src/
│   ├── server.py                  # 메인 서버 파일
│   ├── tools/                     # 📁 도구 모듈들
│   │   ├── __init__.py
│   │   ├── flutter_tools.py       # Flutter 관련 도구들
│   │   ├── general_tools.py       # 일반적인 도구들
│   │   └── analysis_tools.py      # 코드 분석 도구들
│   ├── resources/                 # 📁 리소스 파일들
│   │   ├── __init__.py
│   │   ├── flutter_resources.py   # Flutter 리소스 등록
│   │   ├── general_resources.py   # 일반 리소스 등록
│   │   └── docs/                  # 📁 문서 파일들
│   │       ├── flutter_style.md
│   │       ├── general_style.md
│   │       └── api_reference.md
│   ├── prompts/                   # 📁 프롬프트 모듈들
│   │   ├── __init__.py
│   │   ├── flutter_prompts.py     # Flutter 관련 프롬프트들
│   │   ├── general_prompts.py     # 일반적인 프롬프트들
│   │   └── analysis_prompts.py    # 분석용 프롬프트들
│   └── utils/                     # 📁 유틸리티 함수들
│       ├── __init__.py
│       ├── logging_utils.py
│       └── validation_utils.py
├── tests/                         # 📁 테스트 파일들
│   ├── test_tools/
│   ├── test_resources/
│   └── test_prompts/
├── docs/                          # 📁 프로젝트 문서
├── requirements.txt
├── README.md
└── .gitignore