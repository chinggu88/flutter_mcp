from fastmcp import FastMCP
from resources import code_style, flutter_style
from prompts import general_style_prompt, flutter_style_prompt
from tools import enforce_general, enforce_flutter

# FastMCP 서버 인스턴스 생성
mcp = FastMCP("StyleEnforcerServer")

# 리소스 등록
mcp.add_resource("code_style", code_style)
mcp.add_resource("flutter_style", flutter_style)

# 프롬프트 등록
mcp.add_prompt("general_style", general_style_prompt)
mcp.add_prompt("flutter_style", flutter_style_prompt)

# 도구 등록
mcp.add_tool("enforce_general", enforce_general)
mcp.add_tool("enforce_flutter", enforce_flutter)

if __name__ == "__main__":
    mcp.run() 