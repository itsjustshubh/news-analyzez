# Article Summarizer

The Article Summarizer is a Python tool designed to fetch articles from a predefined list of URLs, generate concise summaries, correct grammatical errors in these summaries using LanguageTool, and save the updated content to JSON files. This tool leverages the Hugging Face Transformers library for summarization and the LanguageTool Python wrapper for grammar correction.

## Features

- Fetches articles from a list of specified URLs.
- Uses a pre-trained model from Hugging Face's Transformers library to generate article summaries.
- Corrects grammatical errors in summaries using LanguageTool.
- Saves updated articles with summaries to JSON files.

## Installation

Before you can use the Article Summarizer, you need to install its dependencies. This project requires Python 3.6 or later.

1. **Clone the repository:**

   ```
   git clone https://github.com/itsjustshubh/news-analyzer.git
   cd article-summarizer
   ```

2. **Set up a virtual environment (optional but recommended):**

- For Unix/macOS:

  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

- For Windows:
  ```
  python -m venv venv
  .\venv\Scripts\activate
  ```

3. **Install the required packages:**

```
pip install -r requirements.txt
```

## Usage

To run the Article Summarizer, ensure you are in the project directory and your virtual environment is activated.

1. **Fetch and summarize articles:**

   ```
   python model.py
   ```

This command processes the list of URLs defined in `utils.py`, fetches the articles, generates summaries, corrects their grammar, and saves the updated content in the `../data/` directory.

2. **Customization:**

- To add or remove URLs for fetching articles, modify the `sample_urls()` function in `utils.py`.
- Adjust summarization and grammar correction settings in `model.py`.

## Dependencies

- [Transformers](https://huggingface.co/transformers/) for summarization.
- [LanguageTool-Python](https://pypi.org/project/language-tool-python/) for grammar correction.
- [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) for HTML parsing.
- [Requests](https://requests.readthedocs.io/en/master/) for HTTP requests.

## Contributing

Contributions to the Article Summarizer are welcome! Please refer to the contributing guidelines for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Hugging Face team for the Transformers library.
- Thanks to the LanguageTool team for the convenient grammar checking tool.
