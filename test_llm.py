import asyncio
from services.chat_service.app.llm.openai_compatible import get_llm_provider
async def main():
    provider = get_llm_provider()
    try:
        e = await provider.embed("hello")
        print("Embed success", len(e))
    except Exception as ex:
        print("Embed error:", ex)
asyncio.run(main())
