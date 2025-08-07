# scrape_headlines.py

import requests
from bs4 import BeautifulSoup

# Target news website (change if needed)
URL = "https://www.bbc.com/news"

# Output file to store headlines
OUTPUT_FILE = "headlines.txt"

def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print("❌ Error fetching URL:", e)
        return None

def parse_headlines(html):
    soup = BeautifulSoup(html, "html.parser")
    headlines = []

    # Look for all <h2> and <h3> tags (BBC uses both)
    for tag in soup.find_all(["h2", "h3"]):
        text = tag.get_text(strip=True)
        if text and len(text) > 10:  # Avoid short or empty headlines
            headlines.append(text)

    return headlines

def save_headlines(headlines, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for idx, headline in enumerate(headlines, 1):
            f.write(f"{idx}. {headline}\n")
    print(f"✅ Saved {len(headlines)} headlines to '{filename}'")

def main():
    print("🔍 Fetching news headlines...")
    html = fetch_html(URL)
    if html:
        headlines = parse_headlines(html)
        save_headlines(headlines, OUTPUT_FILE)

if __name__ == "__main__":
    main()
