from fastmcp import FastMCP


def register_prompt(mcp: FastMCP):
    """MCP prompt 등록"""
    
    @mcp.prompt("controller_prompt")
    def controller_prompt(ctx):
        flutter_resource = ctx.call("flutter_res")  # resource 호출
        return f"""
            다음 기준으로 검토해주세요
            1. 해당 파일명과 변수명 네이밍을 ### 1. 명명 규칙 기준으로 생성해주세요
            2. controller 파일은 ### 3. GetX 컨트롤러 패턴 기준으로 생성해주세요
            {flutter_resource}
            """
