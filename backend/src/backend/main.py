import feedparser
from datetime import datetime, timedelta, timezone

feeds = {
    "Android": "https://blog.google/rss/",
    "Android Developers": "https://developer.android.com/blog/atom.xml",
    "Google Labs": "https://blog.google/innovation-and-ai/models-and-research/google-labs/rss/",
    "Figma": "https://www.figma.com/release-notes/feed/atom.xml",
    "Apple": "https://www.apple.com/ca/newsroom/rss-feed.rss",
    "Apple Developers": "https://developer.apple.com/news/rss/news.rss",
    "Google Developers Tools": "https://blog.google/innovation-and-ai/technology/developers-tools/rss/"
}

def fetch_feeds(feed_sources: dict[str]) -> list[dict]:
    cutoff = datetime.now(timezone.utc) - timedelta(days=14)
    recent_entries = []
    
    for source_name, feed_url in feed_sources.items():
        parsed_feed = feedparser.parse(feed_url)

        for entry in parsed_feed.entries:
            parsed_date = entry.get("published_parsed") or entry.get("updated_parsed")
            if not parsed_date:
                continue
            
            entry_date = datetime(*parsed_date[:6], tzinfo=timezone.utc)
            if entry_date < cutoff:
                continue
            
            item = {
                "title": entry.get("title", ""),
                "tag": source_name,
                "link": entry.get("link", ""),
                "date": entry_date.isoformat()
            }
            recent_entries.append(item)
    recent_entries.sort(key=lambda x: x["date"], reverse=True)
    return recent_entries

def main():
    fetch_feeds(feeds)

if __name__ == "__main__":
    main()