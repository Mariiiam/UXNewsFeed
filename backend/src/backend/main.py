import feedparser

feeds = {
    "Android": "https://blog.google/products-and-platforms/platforms/android/rss/",
    "Android Developers": "https://developer.android.com/static/blog/atom.xml",
    "Material Design": "https://material.io/feed.xml",
    "Figma": "https://www.figma.com/release-notes/feed/atom.xml",
    "Apple": "https://www.apple.com/ca/newsroom/rss-feed.rss",
    "Apple Developers": "https://developer.apple.com/news/rss/news.rss"
}

def fetch_feeds(feed_sources):
    all_entries = []
    for source_name, feed_url in feed_sources.items():
        parsed_feed = feedparser.parse(feed_url)

        for entry in parsed_feed.entries[:2]:
            published_date = (entry.get("updated") or entry.get("pubDate"))
            item = {
                "title": entry.title,
                "tag": source_name,
                "link": entry.link,
                "date": published_date
            }
            print(item)
            all_entries.append(item)
    
    return all_entries

def main():
    fetch_feeds(feeds)

if __name__ == "__main__":
    main()