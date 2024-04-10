import requests
import hashlib
from bs4 import BeautifulSoup
import os
import json

from utils import load_selectors


def fetch_articles(urls, selectors):
    """
    Fetches articles from a list of URLs or a single URL, using provided selectors for scraping.

    Args:
        urls (list or str): A list of URLs or a single URL string.
        selectors (dict): A dictionary of CSS selectors for different domains.

    Returns:
        list: A list of tuples, each containing article content. The content now includes the filename where it's saved.
    """
    # Ensure urls is a list for uniform processing
    if isinstance(urls, str):
        urls = [urls]

    results = []
    for url in urls:
        try:
            content = scrape_content(url, selectors)
            if content:
                filename = save_text_to_file(content)
                # Add the filename to the content dictionary
                content['filename'] = filename
                results.append(content)  # Adjusted to append content directly
        except Exception as e:
            print(f"Error fetching article from {url}: {str(e)}")
    return results


def scrape_content(url, selectors):
    """
    Scrapes the content of a webpage given its URL and specific selectors.

    Args:
        url (str): The URL of the webpage to scrape.
        selectors (dict): A dictionary of CSS selectors specific to the domain.

    Returns:
        dict: A dictionary containing the scraped content if successful, None otherwise.
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch the webpage: {response.status_code}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    content = {'url': url}
    domain = url.split('/')[2].replace('www.', '').split('.')[0]

    if domain in selectors:
        # Extract logo path if available
        logo_path = selectors[domain].get("logo", "default_logo_path")
        content['logo'] = logo_path

        for key, selector in selectors[domain].items():
            if key != "logo":  # Skip the "logo" entry
                content[key] = extract_content(soup, selector)
    else:
        print(f"No selectors available for domain: {domain}")
        return None

    return content


def extract_content(soup, selector):
    """
    Extracts content from a BeautifulSoup object using specified selectors.

    Args:
        soup (BeautifulSoup): The BeautifulSoup object.
        selector (dict): A dictionary containing tag and attribute for finding the element.

    Returns:
        str: The extracted content or a placeholder text if not found.
    """
    tag = selector.get('tag')
    attr = {k: v for k, v in selector.items() if k != 'tag'}
    element = soup.find(tag, **attr)
    if element:
        if 'content' in attr.values():
            paragraphs = element.find_all('p')
            return ' '.join(p.get_text(' ').strip() for p in paragraphs)
        else:
            return element.get_text(' ').strip()
    return f"No content found using selector: {selector}"


def generate_filename(url):
    """
    Generates a filename based on the SHA256 hash of the URL.

    Args:
        url (str): The URL to hash.

    Returns:
        str: A string representing the filename.
    """
    hash_object = hashlib.sha256(url.encode())
    hash_hex = hash_object.hexdigest()
    return f"{hash_hex}.json"


def save_text_to_file(content):
    """
    Saves the scraped content to a JSON file named after the content's URL hash.

    Args:
        content (dict): The content to save.

    Returns:
        str: The path to the saved file.
    """
    filename = generate_filename(content['url'])
    filepath = os.path.join('..', 'data', filename)
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(content, file, indent=4, ensure_ascii=False)
    print(f"Saved: {filepath}")
    return filepath


if __name__ == "__main__":
    selectors = load_selectors()
    urls = [
        "https://www.ndtv.com/india-news/out-on-bail-nuh-violence-accused-bittu-bajrangi-thrashes-man-cop-looks-on-5362562#pfrom=home-ndtv_topscroll",
        "https://www.hindustantimes.com/india-news/there-was-a-time-when-jawaharlal-nehru-talked-about-china-first-s-jaishankar-101712104970832.html",
        "https://www.reuters.com/markets/deals/indias-tata-technologies-bmw-group-form-jv-2024-04-02/",
        "https://www.theregister.com/2024/04/02/meta_facebook_watch_netflix/",
        "https://economictimes.indiatimes.com/markets/expert-view/we-are-getting-ready-to-be-a-global-player-says-jairam-sampath-of-kaynes-technology/articleshow/108191489.cms?from=mdr",
        "https://cointelegraph.com/news/bitcoin-resets-bull-market-btc-price-april-dip",
        "https://www.marketbeat.com/instant-alerts/nyse-vsh-analyst-earnings-estimates-2024-04-02/",
    ]

    fetch_articles(urls, selectors)
