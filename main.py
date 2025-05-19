import asyncio
import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

load_dotenv()

# Initialize model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)


async def main():
    async with MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": [
                    "/Users/ionutbanu/Documents/Personal/Workspace/mcp-crash-course/servers/math_server.py"
                ],
            }
        }
    ) as client:
        agent = create_react_agent(llm, client.get_tools())
        result = await agent.ainvoke(
            {"messages": [HumanMessage(content="What is 54 + 2 * 3?")]}
        )
        print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
