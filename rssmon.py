import feedparser
import sys
import validators
import os
from datetime import datetime

def fetch_rss_feed(url):
    if not validators.url(url):
        print("Invalid URL provided. Please provide a valid RSS feed URL.")
        sys.exit(1)

    feed = feedparser.parse(url)

    output_directory = "output"
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_filename = f"{output_directory}/{current_time}.txt"

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with open(output_filename, 'w') as file:
        file.write(f"Title: {feed.feed.title}\n")
        file.write(f"Number of Entries: {len(feed.entries)}\n")
        file.write("-" * 50 + "\n")

        for entry in feed.entries:
            file.write(f"Title: {entry.title}\n")
            file.write(f"Link: {entry.link}\n")
            file.write(f"Published: {entry.published}\n")
            file.write(f"Summary: {entry.summary}\n")
            file.write("-" * 50 + "\n")

    print(f"Feed data written to: {output_filename}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python rssmon.py <RSS_FEED_URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_rss_feed(url)
