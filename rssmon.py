import feedparser
import sys
import validators

def fetch_rss_feed(url):
    # Validate the URL
    if not validators.url(url):
        print("Invalid URL provided. Please provide a valid RSS feed URL.")
        sys.exit(1)

    feed = feedparser.parse(url)

    print(f"Title: {feed.feed.title}")
    print(f"Number of Entries: {len(feed.entries)}")
    print("-" * 50)

    for entry in feed.entries:
        print(f"Title: {entry.title}")
        print(f"Link: {entry.link}")
        print(f"Published: {entry.published}")
        print(f"Summary: {entry.summary}")
        print("-" * 50)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python rssmon.py <RSS_FEED_URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_rss_feed(url)
