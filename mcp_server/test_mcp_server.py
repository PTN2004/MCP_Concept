from mcp import ClientSession
from mcp.client.sse import sse_client

async def check():
    async with sse_client("http://0.0.0.0:8000/sse") as streams:
        async with ClientSession(*streams) as session:
            print("Connecting to MCP server...")
            await session.initialize()
            # tools = await session.list_tools()
            # print(tools)
            
            result = await session.call_tool("get_list_repo")
            print(result)
            
if __name__ == "__main__":
    import asyncio
    asyncio.run(check())