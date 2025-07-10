from fastmcp import Context
import mcp


@mcp.prompt("flutter_struct")
async def flutter_struct_prompt(ctx: Context) -> str:
    rules = await ctx.read_resource("style://flutter_struct")
    return (
        "Apply the following general code style rules:\n\n"
        f"{rules}\n\n"
        "Return ONLY the corrected code."
    )