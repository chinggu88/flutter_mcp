from fastmcp import FastMCP

from resources.flutter_style import register_resources
from tools.flutter_tools import register_tools
from prompts.general_style_prompt import register_prompt
# FastMCP 서버 인스턴스 생성
mcp = FastMCP("Cuunit_mcp")

register_resources(mcp)
register_prompt(mcp)
register_tools(mcp)


if __name__ == "__main__":
    mcp.run() 
