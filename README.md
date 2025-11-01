# PDF Cleaner

A Python script to remove pages from a PDF document that contain a specific word or sentence. The search is case-insensitive.

## Prerequisites

You need Python 3 installed on your system.

## Setup

1.  **Create and activate a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2.  **Install dependencies:**

    The required library is `pypdf`. Install it using the provided `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script using `python3` followed by the input PDF path and the search term.

### Syntax

```bash
python3 pdf_cleaner.py <INPUT_PDF_PATH> "<SEARCH_TERM>" [OPTIONS]
```

### Arguments

*   `INPUT_PDF_PATH`: Path to the PDF file you want to clean.
*   `SEARCH_TERM`: The word or sentence to search for (must be enclosed in quotes if it contains spaces).

### Options

*   `-o`, `--output_file`: Path for the output PDF file (default: `cleaned_output.pdf`).

### Examples

1.  **Basic usage (output to `cleaned_output.pdf`):**

    ```bash
    python3 pdf_cleaner.py my_document.pdf "Confidential"
    ```

2.  **Specifying an output file:**

    ```bash
    python3 pdf_cleaner.py report.pdf "Draft Copy" -o final_report.pdf
    ```

## Script Details

The script [`pdf_cleaner.py`](pdf_cleaner.py) uses the `pypdf` library to iterate through each page, extract the text, and use a regular expression to check for the presence of the search term (case-insensitively). Pages containing the term are skipped, and the remaining pages are written to a new PDF file.