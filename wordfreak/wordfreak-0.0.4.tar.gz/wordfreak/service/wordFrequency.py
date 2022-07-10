import json

from wordfreak.parser.DocxParser import DocxParser
from wordfreak.parser.PdfParser import PdfParser
from wordfreak.parser.TxtParser import TxtParser


def extractWordFrequencies(inputFilePath: str, outputFilePath: str) -> None:
    """
    Takes a file and saves all word frequencies to a JSON file.
    """
    TXT_FILE_EXTENSION = ".txt"
    PDF_FILE_EXTENSION = ".pdf"
    DOCX_FILE_EXTENSION = ".docx"

    if inputFilePath.lower().endswith(TXT_FILE_EXTENSION):
        wordFrequencies = TxtParser.getWordFrequency(inputFilePath)
    elif inputFilePath.lower().endswith(PDF_FILE_EXTENSION):
        wordFrequencies = PdfParser.getWordFrequency(inputFilePath)
    elif inputFilePath.lower().endswith(DOCX_FILE_EXTENSION):
        wordFrequencies = DocxParser.getWordFrequency(inputFilePath)
    else:
        raise ValueError(f"Filetype not supported for parsing (tried to parse file at '{inputFilePath}').")

    # sort word frequencies by number of occurrences
    orderedWordFreq = dict(sorted(wordFrequencies.items(), reverse=True, key=lambda item: item[1]))

    # save to JSON file
    with open(outputFilePath, "w+") as file:
        json.dump(orderedWordFreq, file)
