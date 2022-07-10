from string import punctuation
from collections import Counter

def load_text(input_file):
    """Loads text file

    Args:
        input_file (str): filepath 

    Returns:
        string: Text from file
    """      
    with open(input_file, "r") as file:
          text = file.read()

    return text


def clean_text(text):
    """Converts text to lowercase and removes punctuation

    Args:
        text (str): Original text

    Returns:
        str: Lowercase text with punctuation removed
    """        
        
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, "")
    return text


def count_words(input_file):
    """Count words in a text file

    Args:
        input_file (str): Filepath 

    Returns:
        Counter: Counts of words
    """        
    
    text = load_text(input_file)
    text = clean_text(text)
    words = text.split()
    return Counter(words)