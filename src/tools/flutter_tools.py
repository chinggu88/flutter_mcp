from venv import logger
from fastmcp import FastMCP


def register_tools(mcp: FastMCP):
    """MCP 도구 등록"""
    @mcp.tool()
    def add_controller(ctx, user_question: str = "") -> dict:
        """
        Flutter Controller를 추가하는 도구
        
        Args:
            ctx: FastMCP 컨텍스트
            user_question: 사용자의 질문이나 요구사항
            
        Returns:
            dict: 생성된 코드와 관련 정보
        """
        # 기본 프롬프트 호출
        base_prompt = ctx.call("controller_prompt")
        logger.debug(f"{base_prompt}")

        # 사용자 질문이 있는 경우 프롬프트에 추가
        if user_question.strip():
            enhanced_prompt = f"""
                {base_prompt}

                사용자 요구사항:
                {user_question}

                위 요구사항을 반영하여 Flutter Controller를 생성해주세요.
                """
        else:
            enhanced_prompt = base_prompt
        
        return {
            "prompt": enhanced_prompt,
            "code": f'// Controller generated based on: {user_question if user_question else "기본 패턴"}',
            "user_question": user_question,
            "status": "success"
        }
        