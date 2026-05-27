import asyncio
import sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def async_input(prompt):
    print(prompt, end="", flush=True)
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, sys.stdin.readline)

async def main():
    server_params = StdioServerParameters(
        command="uv",
        args=["run", "server.py"],
        cwd="D:\\UTD\\MCP_Project\\news-mcp"
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            print("=== News MCP Client ===")
            print("Type a topic to search, or 'quit' to exit.\n")

            while True:
                topic = (await async_input("Search topic: ")).strip()

                if topic.lower() in ("quit", "exit", "q"):
                    print("Bye!")
                    break

                if not topic:
                    continue

                print(f"\nFetching news on '{topic}'...\n")
                result = await session.call_tool("get_news", {"topic": topic})
                print(result.content[0].text)
                print("\n" + "-" * 50 + "\n")

asyncio.run(asyncio.wait_for(main(), timeout=300))