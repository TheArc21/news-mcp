import feedparser
import urllib.parse
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("news-server")

@mcp.tool()
def get_news(topic: str) -> str:
    """Fetch latest news headlines for a given topic from Google News RSS."""
    encoded_topic = urllib.parse.quote(topic)
    url = f"https://news.google.com/rss/search?q={encoded_topic}&hl=en-US&gl=US&ceid=US:en"
    feed = feedparser.parse(url)
    
    if not feed.entries:
        return f"No news found for '{topic}'"
    
    results = []
    for entry in feed.entries[:5]:
        results.append(f"- {entry.title} ({entry.published})\n  {entry.link}")
    
    return f"Latest news on '{topic}':\n\n" + "\n\n".join(results)

if __name__ == "__main__":
    mcp.run()