import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    server_params = StdioServerParameters(
        command="uv",
        args=["run", "server.py"],
        cwd="D:\\UTD\\MCP_Project\\news-mcp"
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            print("Available tools:")
            for tool in tools.tools:
                print(f"  - {tool.name}: {tool.description}")

            print("\nFetching news on 'artificial intelligence'...")
            result = await session.call_tool("get_news", {"topic": "artificial intelligence"})
            print(result.content[0].text)

asyncio.run(asyncio.wait_for(main(), timeout=30))