from fastmcp import FastMCP

mcp = FastMCP("Warm up Server")

@mcp.tool
def greet(name: str) -> str:
    """Greets the user with a welcome message."""
    return f"Hello, {name}! Welcome to MCP"

@mcp.tool
def add(a: int, b: int) -> int:
    """Adds two numbers together."""
    return a + b

if __name__ == "__main__":
    mcp.run()