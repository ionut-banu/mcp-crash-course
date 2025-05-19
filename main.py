import asyncio
import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.server.fastmcp import FastMCP

load_dotenv()

# Initialize model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

stdio_server_params = StdioServerParameters(
    command="python",
    args=["/Users/ionutbanu/Documents/Personal/Workspace/mcp-crash-course/servers/math_server.py"],
)

def main():
    print("Hello from mcp-crash-course!")


if __name__ == "__main__":
    main()
