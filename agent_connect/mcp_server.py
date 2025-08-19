from mcp.server.fastmcp import FastMCP

mcp_app=FastMCP(
    name="SharedStandAloneMCPServer",
    stateless_http=True,
)

@mcp_app.tool(name="greet_from_shared_server",description="returns a personalized greeting from the shared MCP server")
def greet_from_shared_server(name: str) -> str:
    """A simple function to greet a user."""
    print(f"Hello, {name}! Greetings from the shared MCP server.") 
    response_mesage = f"Hello, {name}! Greetings from the shared MCP server."
    return response_mesage

@mcp_app.tool(name="get_my_mood",description="return a personalized mood from the shared MCP server")
def get_my_mood(name: str) -> str:
    """A simple function to return a user's mood."""
    print(f"tool 'mood' called with name: {name}") 
    return "I am happy"

mcp_app=mcp_app.streamable_http_app()