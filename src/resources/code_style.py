from server import mcp

@mcp.resource("flutter_struct")
def flutter_struct() -> str:
    print(open("src/guide/flutter_struct.md", encoding="utf-8").read())
    return open("src/guide/flutter_struct.md", encoding="utf-8").read()

@mcp.resource("test_resource")
def test_resource()->str:
    flutter_struct = """
                    lib/
                    ├── controllers/     # 상태 및 로직 제어
                    ├── views/           # UI 코드
                    ├── models/          # 데이터 모델
                    ├── services/        # API 및 DB 관련 서비스
                    ├── bindings/        # GetX 의존성 바인딩
                    """
    return flutter_struct