from fastmcp import FastMCP


def register_tools(mcp: FastMCP):
    """MCP 도구 등록"""
    @mcp.tool()
    def add_controller(ctx) -> str:
        prompt = ctx.call("controller_prompt")  # prompt 호출
        return {
            "code": f'print("{prompt}")'
        }
        