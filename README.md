# news-mcp

A live news feed MCP (Model Context Protocol) server built in Python. Fetches real-time headlines from Google News RSS and exposes them as a tool that Claude or any MCP client can call.

## What is MCP?

Model Context Protocol is an open standard by Anthropic that connects AI models to external tools and live data sources. This project implements a custom MCP server from scratch and two clients to interact with it — Claude Desktop and a raw Python client.

## Features

- Live news headlines via Google News RSS — no API key required
- Search news by any topic (AI, finance, climate, sports, etc.)
- Works with Claude Desktop (GUI) and a Python MCP client (programmatic)
- Built with FastMCP for clean, decorator-based tool definition

## Project Structure

```
news-mcp/
├── server.py        # MCP server — exposes get_news tool
├── client.py        # Python MCP client — connects and calls tools directly
├── pyproject.toml   # Project dependencies
└── uv.lock          # Dependency lockfile
```

## Stack

| Tool | Purpose |
|------|---------|
| Python 3.10 | Core language |
| uv | Package manager and script runner |
| FastMCP | MCP server framework (Anthropic SDK) |
| feedparser | RSS feed parsing |
| urllib.parse | URL encoding for search queries |

## Setup

**1. Install uv**
```bash
pip install uv
```

**2. Clone and install dependencies**
```bash
git clone https://github.com/TheArc21/news-mcp.git
cd news-mcp
uv sync
```

**3. Run the Python client**
```bash
uv run client.py
```

## Example Output

```
Available tools:
  - get_news: Fetch latest news headlines for a given topic from Google News RSS.

Fetching news on 'artificial intelligence'...
Latest news on 'artificial intelligence':

- Pope Leo Warns Artificial Intelligence Could Be "New Tower Of Babel" (Mon, 25 May 2026)
  https://news.google.com/...

- Artificial Intelligence Floods Court Dockets with Home-Brewed Lawsuits (Mon, 25 May 2026)
  https://news.google.com/...
```

## Claude Desktop Setup

Add the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "news-mcp": {
      "command": "/absolute/path/to/uv",
      "args": ["--directory", "/absolute/path/to/news-mcp", "run", "server.py"]
    }
  }
}
```

On Windows, use the full path to `uv.exe`. Find it with:
```powershell
where.exe uv
```

> **Note for Windows Store version of Claude Desktop:** the config file is located at `AppData\Local\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude\claude_desktop_config.json`, not the standard `AppData\Roaming\Claude` path.

## How It Works

1. Client launches `server.py` as a subprocess via stdio transport
2. MCP handshake initializes the connection
3. Client calls `get_news` with a topic string
4. Server encodes the topic, fetches Google News RSS, parses top 5 entries
5. Results returned as formatted text over stdout

## Next Steps

- Add `get_top_headlines()` tool with no topic filter
- Add category-based search (tech, business, health, sports)
- Integrate Claude API agentic loop — let Claude decide when to call the tool
- Add summarization layer inside the tool using Claude API