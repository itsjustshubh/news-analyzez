import json


def load_selectors():
    """
    Loads the JSON file containing the CSS selectors for different news sites.

    Returns:
        dict: A dictionary where keys are domain names and values are dictionaries of CSS selectors.
    """
    with open('../presets/selectors.json', 'r') as file:
        return json.load(file)


def sample_urls():
    """
    Returns a list of sample URLs for testing purposes.

    Returns:
        list: A list of sample URLs.
    """
    urls = [
        "https://www.ndtv.com/india-news/out-on-bail-nuh-violence-accused-bittu-bajrangi-thrashes-man-cop-looks-on-5362562#pfrom=home-ndtv_topscroll",
        "https://www.hindustantimes.com/india-news/there-was-a-time-when-jawaharlal-nehru-talked-about-china-first-s-jaishankar-101712104970832.html",
        "https://www.reuters.com/markets/deals/indias-tata-technologies-bmw-group-form-jv-2024-04-02/",
        "https://www.theregister.com/2024/04/02/meta_facebook_watch_netflix/",
        "https://economictimes.indiatimes.com/markets/expert-view/we-are-getting-ready-to-be-a-global-player-says-jairam-sampath-of-kaynes-technology/articleshow/108191489.cms?from=mdr",
        "https://cointelegraph.com/news/bitcoin-resets-bull-market-btc-price-april-dip",
        "https://www.marketbeat.com/instant-alerts/nyse-vsh-analyst-earnings-estimates-2024-04-02/",
    ]

    return urls