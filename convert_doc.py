from epub2txt import epub2txt

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

def epub_to_str(input_path):
    """
    Convert a Epub file to a string.
    
    Args:
    - input_path (str): Path to convert to string.
    """
    return epub2txt(input_path) 

# from a local epub file
filepath = "/home/nuttaphon/WorkFolder/ConvertDoc/src/1984.epub"
txt_file = "/home/nuttaphon/WorkFolder/ConvertDoc/out/output.txt"

res = epub_to_str(filepath)

num_words = count_words(res)
print("Number of words:", num_words)

write_str_to_txt(res, txt_file)


