# 📄 PDF Cleaner

A powerful and simple Python script to automatically clean PDF documents by removing pages that contain a specific word or sentence.

## Badges

| Status | Language | Views | Downloads |
| :---: | :---: | :---: | :---: |
| ![GitHub last commit](https://img.shields.io/github/last-commit/Naveen-Jayaraj/pdf_classifier) | ![Python](https://img.shields.io/badge/Language-Python-blue.svg) | ![GitHub views](https://img.shields.io/badge/views-1k+-informational) | ![GitHub downloads](https://img.shields.io/badge/downloads-500+-success) |

*Note: View and Download counts are placeholders and require external services (like GitHub Actions or third-party trackers) to be accurate.*

## ✨ Features

*   **Keyword Removal:** Automatically identifies and removes entire pages containing a specified word or phrase.
*   **Case-Insensitive Search:** Uses regular expressions for flexible matching.
*   **Command-Line Interface:** Easy to use with clear arguments for input, search term, and output file.
*   **Dependency Management:** Uses `requirements.txt` for easy setup.

## 🚀 Getting Started

### Prerequisites

*   Python 3.6+

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Naveen-Jayaraj/pdf_classifier.git
    cd pdf_classifier
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    The required library is `pypdf`.
    ```bash
    pip install -r requirements.txt
    ```

## 💻 Usage

Run the script using `python3` followed by the input PDF path and the search term.

### Syntax

```bash
python3 pdf_cleaner.py <INPUT_PDF_PATH> "<SEARCH_TERM>" [OPTIONS]
```

### Arguments

| Argument | Description |
| :--- | :--- |
| `INPUT_PDF_PATH` | Path to the PDF file you want to clean. |
| `SEARCH_TERM` | The word or sentence to search for (must be enclosed in quotes if it contains spaces). |

### Options

| Option | Default | Description |
| :--- | :--- | :--- |
| `-o`, `--output_file` | `cleaned_output.pdf` | Path for the output PDF file. |

### Examples

1.  **Basic usage (output to `cleaned_output.pdf`):**

    ```bash
    python3 pdf_cleaner.py my_document.pdf "Confidential"
    ```

2.  **Specifying an output file:**

    ```bash
    python3 pdf_cleaner.py report.pdf "Draft Copy" -o final_report.pdf
    ```

## ⚙️ How It Works

The script [`pdf_cleaner.py`](pdf_cleaner.py) utilizes the `pypdf` library to read the PDF. It iterates through each page, extracts the text content, and performs a case-insensitive regular expression search for the specified term. If the term is found, the page is skipped; otherwise, it is added to a new `PdfWriter` object, which is then saved as the cleaned output file.