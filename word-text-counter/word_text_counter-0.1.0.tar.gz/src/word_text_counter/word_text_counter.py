from collections import Counter
from string import punctuation
  
def load_text(filename: str) -> str:
    """load text from a file.

    Args:
        filename (str): a file path.

    Returns:
        str: a string of text from the file.

    Examples:
        >>> load_text("data/text.txt")
    """

    with open(filename) as textfile:
        txt = textfile.read()
    return txt

def clean_text(txt: str) -> str:
    """clean text from punctuations.

    Args:
        txt (str): a string that will be cleaned.

    Returns:
        str: cleaned text.
    
    Examples:
        >>> clean_text("Early optimization is the root of all evil!")
        'early optimization is the root of all evil'
    """
    
    cleaned_txt = txt.lower()
    for punc in punctuation:
        cleaned_txt = cleaned_txt.replace(punc,'')
    return cleaned_txt

def count_words(filename: str) -> dict:
    """Counting words from a text.

    Words are made lowercase and punctuation is removed before counting.

    Args:
        filename (str):  a file path.

    Returns:
        dict: total words and count details for each word.

    Examples:
        >>> from word_text_counter import count_words
        >>> count_words("data/text.txt")
    """

    txt = load_text(filename)
    cleaned_txt = clean_text(txt)
    word_counts = dict(Counter(cleaned_txt.split()))
    return {"total":sum([v for k,v in word_counts.items()]),"details":word_counts}
