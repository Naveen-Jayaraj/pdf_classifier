import argparse
import re
from pypdf import PdfReader, PdfWriter

def clean_pdf(input_pdf_path, output_pdf_path, search_term):
    """
    Reads a PDF, searches for a specific term (word/sentence) on each page,
    and creates a new PDF excluding the pages where the term is found.
    
    :param input_pdf_path: Path to the input PDF file.
    :param output_pdf_path: Path to save the cleaned output PDF file.
    :param search_term: The word or sentence to search for.
    """
    try:
        reader = PdfReader(input_pdf_path)
        writer = PdfWriter()
        
        # Compile regex for case-insensitive search
        search_pattern = re.compile(re.escape(search_term), re.IGNORECASE)
        
        pages_removed = 0
        
        for page_num, page in enumerate(reader.pages):
            text = page.extract_text()
            
            if text and search_pattern.search(text):
                print(f"Page {page_num + 1} contains '{search_term}'. Removing page.")
                pages_removed += 1
            else:
                writer.add_page(page)
                
        if pages_removed == len(reader.pages):
            print("Warning: All pages contained the search term. Output PDF will be empty.")
            
        if len(writer.pages) == 0 and len(reader.pages) > 0:
            print("No pages to write. Output file will not be created or will be empty.")
            return

        with open(output_pdf_path, "wb") as output_file:
            writer.write(output_file)
            
        print(f"\nSuccessfully created cleaned PDF: {output_pdf_path}")
        print(f"Total pages in original PDF: {len(reader.pages)}")
        print(f"Total pages removed: {pages_removed}")
        print(f"Total pages in new PDF: {len(writer.pages)}")

    except FileNotFoundError:
        print(f"Error: Input file not found at {input_pdf_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Clean a PDF by removing pages containing a specific word or sentence."
    )
    parser.add_argument(
        "input_file", 
        help="Path to the input PDF file."
    )
    parser.add_argument(
        "search_term", 
        help="The word or sentence to search for (case-insensitive)."
    )
    parser.add_argument(
        "-o", "--output_file", 
        default="cleaned_output.pdf",
        help="Path for the output PDF file (default: cleaned_output.pdf)."
    )
    
    args = parser.parse_args()
    
    clean_pdf(args.input_file, args.output_file, args.search_term)