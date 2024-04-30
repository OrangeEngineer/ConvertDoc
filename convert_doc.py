from pdfminer.high_level import extract_text
from docx import Document
from bs4 import BeautifulSoup
import os 
from html.parser import HTMLParser
import epub
import nltk
from nltk.tokenize import sent_tokenize


def count_words(input_str):
    """
    Count the number of words in a string.
    
    Args:
    - input_str (str): The input string.
    
    Returns:
    - int: The number of words in the input string.
    """
    # Split the string into words using whitespace as delimiter
    words = input_str.split()
    # Count the number of words
    num_words = len(words)
    return num_words


def write_str_to_txt(input_str, txt_path):
    """
    Write a string to a text file.
    
    Args:
    - input_str (str): The string to write to the text file.
    - txt_path (str): Path to save the text file.
    """
    with open(txt_path, 'w', encoding='utf-8') as file:
        file.write(input_str)


# def process_epub(input_path):
#     """
#     Convert a Epub file to a string.
    
#     Args:
#     - input_path (str): Path to convert to string.
#     """
#     parsed = parser.from_file(input_path)
#     content = parsed["content"]

#     return content
class HTMLFilter(HTMLParser):
    """
    Source: https://stackoverflow.com/a/55825140/1209004
    """
    text = ""
    def handle_data(self, data):
        self.text += data


def process_epub(input_path):
    """
    Convert a Epub file to a string.
    
    Args:
    - input_path (str): Path to convert to string.
    """

    # Load EPUB file
    book = epub.open_epub(filepath)

    # Extract text from EPUB
    text = ''
    for item_id, href in book.opf.manifest.items():
        if href.media_type == 'application/xhtml+xml':
            content = book.read_item(href)
            text += content.decode('utf-8', 'ignore')

    # # Save html file
    # with open(html_output, 'w', encoding='utf-8') as file:
    #     file.write(text)

    # # Parse the HTML content
    soup = BeautifulSoup(text, 'html.parser')

    # Find all <p> tags
    paragraphs = soup.find_all('p')

    res = ''
    for paragraph in paragraphs:
        # if paragraph:
        #     paragraph.text.replace('\n','')
        res += paragraph.text.replace('\n','')
        res += "\n\n"

    return res


def process_pdf(pdf_path):
    """
    Convert a PDF file to a string.
    
    Args:
    - input_path (str): Path to convert to string.
    """
    return extract_text(pdf_path)

def process_docx(file_path):
    """
    Convert a docx file to a string.
    
    Args:
    - input_path (str): Path to convert to string.
    """
    doc = Document(file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def process_html(html_file_path):
    try:
        # Read the HTML file
        with open(html_file_path, "rb") as file:
            html_content = file.read()

        # Parse the HTML
        soup = BeautifulSoup(html_content, "html.parser")

        # Extract text
        text = soup.get_text()
        clean_text = text.replace('\n', ' ')
        print(clean_text)
        return clean_text
    except Exception as e:
        print("An error occurred:", str(e))
        return None

def get_file_extension(file_path):
    """Function to get the file extension from a file path."""
    return os.path.splitext(file_path)[1].lower()

def process_file(file_path, output_file):
    """Function to process different file types."""
    file_extension = get_file_extension(file_path)
    
    print(file_extension)

    # Switch cases based on file extensions
    switch_cases = {
        '.pdf': process_pdf,
        '.docx': process_docx,
        '.epub': process_epub,
        '.html': process_html,
    }

    # Get the appropriate function based on the file extension
    process_function = switch_cases.get(file_extension, None)

    # Execute the appropriate function if found
    if process_function:
        res = process_function(file_path)
        num_words = count_words(res)
        print("Number of words:", num_words)
        write_str_to_txt(res, output_file)

        # return process_function(file_path)
    else:
        print("Unsupported file type.")


# from a local epub file

# filepath = input("Enter the input file path: ")
# txt_file = input("Enter the output file path: ")

filepath = "/home/nuttaphon/WorkFolder/ConvertDoc/src/orwell-animal-farm.epub"
# txt_file = "/home/nuttaphon/WorkFolder/ConvertDoc/out/output.txt"
output_file = "/home/nuttaphon/WorkFolder/ConvertDoc/out/output_orwell-animal-farm_epub2txt_clean.txt"

process_file(filepath, output_file)




