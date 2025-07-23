from fastmcp import FastMCP


def register_resources(mcp: FastMCP):
    """MCP 리소스 등록"""
    
    @mcp.resource('resource://flutter_res')
    def flutter_resource():
        return open("flutter_style.md", encoding="utf-8").read()