MCP Server se Agent ko Connect karna (Streamable HTTP)
🎯 Asal Maqsad (Core Concept)

Is sub-module ka main maqsad OpenAI Agents SDK ka istemal karte hue, ek OpenAI Agent ko ek MCP (Modular Communication Protocol) server se connect karna hai.

Yeh MCP server streamable-http transport use karta hai. Humara goal yeh dikhana hai ke:

Jab Agent initialize hota hai

Ya jab Agent ko MCP tools ki zarurat hoti hai

Toh woh server se connect ho kar list_tools() call karta hai, jisse server ke available tools ki list milti hai.

🧩 Key SDK Concepts
1. MCPServerStreamableHttpParams

MCP server se connect hone ke liye zaroori details (jaise URL) configure karta hai.

2. MCPServerStreamableHttp

SDK ka client class hai jo streamable-http MCP server se baat karta hai.

3. Agent(mcp_servers=[...])

Agent ko initialize karte waqt, is parameter mein MCP client pass karte hain.

4. mcp_server_client.list_tools()

Seedhe MCP server se tools ki list mangta hai.

Agent bhi background mein yeh kaam karta hai.

5. async with MCPServerStreamableHttp(...)

Ek asynchronous context manager.

Client connection ko sahi tarah se start aur close karta hai.

6. Runner.run()

Agent ko run karne ke liye aur ek query dene ke liye use hota hai.

⚙️ Setup: Tayyari Kaise Karein

Is experiment ko chalane ke liye do alag terminals chahiye honge:

1. Shared MCP Server Run Karein

Yeh server agent ke liye target hoga aur kuch tools expose karega.

2. Important Configurations

.env se API key load karna:

load_dotenv(find_dotenv())


MCP server ka URL set karna:

MCP_SERVER_URL = "http://localhost:8001/mcp/"


Gemini API client:

AsyncOpenAI(base_url="https://generativelanguage.googleapis.com/...")

🔄 Code Flow

Client Config

mcp_params = MCPServerStreamableHttpParams(...)
async with MCPServerStreamableHttp(...) as mcp_server_client:


Client ko initialize karta hai.

Iska name ("MySharedMCPServerClient") logs mein useful hota hai.

Agent Initialization

assistant = Agent(
    mcp_servers=[mcp_server_client],
    model=OpenAIChatCompletionsModel(...)
)


List Tools

await mcp_server_client.list_tools()


Tools ki list verify karne ke liye.

Run Agent

await Runner.run(assistant, "What is Sir Zia mood?")


Agent Gemini model ke sath query solve karega.

Agar relevant tool (mood_from_shared_server) ho, toh usay call karega.

MCP server tool ko run karega aur jawab return karega.

✅ Expected Output
1. Agent Terminal (main.py output)

Connection messages (HTTP logs for MCP server & Gemini API).

"MySharedMCPServerClient" creation confirmation.

"Attempting to explicitly list tools..." ke baad tools list (e.g. greet_from_shared_server, mood_from_shared_server).

[AGENT RESPONSE]: OK. Sir Zia is happy.

2. Shared MCP Server Terminal (server.py output)

tools/list request logs when agent connects.

tool/run request logs when mood tool is called.

Example args:

{"name": "Sir Zia"}


Tool run hone ke baad ka response (e.g. "Sir Zia is happy.").
