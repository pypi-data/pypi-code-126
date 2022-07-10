import json

from wordfreak.parser.DocxParser import DocxParser
from wordfreak.parser.PdfParser import PdfParser
from wordfreak.parser.TxtParser import TxtParser


def extractWordFrequencies(inputFilePath: str, outputFilePath: str) -> None:
    """
    Takes a file path and saves all word frequencies to the given JSON file.

    inputFilePath: Path to file to extract work frequencies from.
    outputFilePath: Path to file to save word frequencies to (must be .json file).
    """
    DOCX_FILE_EXTENSION = ".docx"
    JSON_FILE_EXTENSION = ".json"
    PDF_FILE_EXTENSION = ".pdf"
    TXT_FILE_EXTENSION = ".txt"
    
    if not outputFilePath.lower().endswith(JSON_FILE_EXTENSION):
        raise ValueError(f"Output file must be a .json file.")

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
