# Import necessary modules and functions
import json
from transformers import pipeline
import language_tool_python

# Assuming fetch_articles and load_selectors are defined in their respective modules
from fetcher import fetch_articles
from utils import sample_urls, load_selectors

# Initialize LanguageTool for grammar correction
lang_tool = language_tool_python.LanguageTool('en-US')

# Initialize the summarization pipeline with an explicitly specified model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")


def correct_grammar(text):
    """
    Corrects grammatical errors in the given text using LanguageTool.

    Args:
        text (str): The text to correct.

    Returns:
        str: The grammatically corrected text.
    """
    matches = lang_tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)
    return corrected_text


def generate_summary(content, max_length=1024, summary_length=130, overlap=50):
    """
    Generates a grammatically corrected summary for the given content by breaking it into manageable segments.

    Args:
        content (str): The content to summarize.
        max_length (int): Maximum length of text (in words) for each segment that can be processed.
        summary_length (int): Desired maximum length of the summary.
        overlap (int): Number of words to overlap between segments to ensure continuity.

    Returns:
        str: A grammatically corrected summary of the content.
    """
    tokens = content.split()
    segments = []
    start = 0

    # Break the content into segments
    while start < len(tokens):
        end = start + max_length
        segment = " ".join(tokens[start:min(end, len(tokens))])
        segments.append(segment)
        start = end - overlap

    # Summarize and correct each segment
    summaries = []
    for segment in segments:
        try:
            summary = summarizer(segment, max_length=summary_length,
                                 min_length=30, do_sample=False)[0]['summary_text']
            grammatically_correct_summary = correct_grammar(summary)
            summaries.append(grammatically_correct_summary)
        except Exception as e:
            print(f"Error summarizing segment: {e}")
            summaries.append("")

    # Combine all segment summaries
    combined_summary = " ".join(summaries).strip()
    return combined_summary


def update_article_file(article_json):
    """
    Updates the article's JSON file with new content, including the summary.

    Args:
        article_json (dict): The article data, including the 'filename' key.
    """
    filename = article_json.get('filename')
    if filename:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(article_json, file, indent=4, ensure_ascii=False)
        print(f"Updated file: {filename}")
    else:
        print("Filename not found in article JSON.")


def process_article(article_json, print_summary=True):
    """
    Processes the article JSON to add a summary and then saves it back to the corresponding file.

    Args:
        article_json (dict): The article data in JSON format.

    Returns:
        dict: The article data updated with a summary.
    """
    content = article_json.get('content', '')
    summary = generate_summary(content)
    article_json['summary'] = summary
    update_article_file(article_json)
    print(f"Summary added and file updated.")

    if print_summary:
        print(f"Summary generated: {summary}")

    return article_json


if __name__ == "__main__":
    selectors = load_selectors()
    urls = sample_urls()  # Ensure this returns a list of valid URLs
    articles_data = fetch_articles(urls[0], selectors)  # Fetch article data

    # Process each article to add a summary and update its file
    for article in articles_data:
        process_article(article, print_summary=True)