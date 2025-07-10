from fastmcp import FastMCP, Context
# FastMCP 서버 인스턴스 생성
mcp = FastMCP("GreeterServer")

# ✅ Tool 정의: 이름에 따라 공식/친근 인사를 반환
@mcp.tool()
def greet_formal(name: str) -> str:
    """Formal greeting message."""
    return f"Good day, {name}. How do you do?"

@mcp.tool()
def greet_casual(name: str) -> str:
    """Casual greeting message."""
    return f"Hey {name}! What's up?"

@mcp.tool()
def create_controller(name: str) -> str:
    """Create a controller for a robot."""
    return f"""
            class {name}_controller extends GetxController {{
                static {name}_controller get to => Get.find();
                @override
                void onInit() {{
                    super.onInit();
                }}
            }}
            """

# ✅ Prompt 정의: LLM에게 ‘양식(greeting style)’ 지시
@mcp.prompt()
def greet_prompt(name: str) -> str:
    """
    Generate a greeting.
    If name is "Alice", use formal style; otherwise, casual.
    """
    return (
        f"Please provide a greeting for {name}.\n"
        "If name == 'Alice', make it formal; else, make it casual."
    )

if __name__ == "__main__":
    mcp.run()