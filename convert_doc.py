from epub2txt import epub2txt
from pdfminer.high_level import extract_text
from docx import Document
from bs4 import BeautifulSoup
import os 

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
    with open(txt_path, 'w') as txt_file:
        txt_file.write(input_str)

def process_epub(input_path):
    """
    Convert a Epub file to a string.
    
    Args:
    - input_path (str): Path to convert to string.
    """
    return epub2txt(input_path) 


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
        with open(html_file_path, "r", encoding="utf-8") as file:
            html_content = file.read()

        # Parse the HTML
        soup = BeautifulSoup(html_content, "html.parser")

        # Extract text
        text = soup.get_text()

        return text
    except Exception as e:
        print("An error occurred:", str(e))
        return None

def get_file_extension(file_path):
    """Function to get the file extension from a file path."""
    return os.path.splitext(file_path)[1].lower()

def process_file(file_path):
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
        return process_function(file_path)
    else:
        print("Unsupported file type.")


# from a local epub file

filepath = input("Enter the file path: ")

# filepath = "/home/nuttaphon/WorkFolder/ConvertDoc/src/1984.pdf"
txt_file = "/home/nuttaphon/WorkFolder/ConvertDoc/out/output.txt"

res = process_file(filepath)

num_words = count_words(res)
print("Number of words:", num_words)

write_str_to_txt(res, txt_file)


