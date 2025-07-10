from fastmcp import Context


async def enforce_flutter_struct(code: str, ctx: Context, langage = "enforce_flutter_struct") -> str:
    msg = await ctx.run_prompt("flutter_struct", {})
    res = await ctx.sample(msg)
    return res.text