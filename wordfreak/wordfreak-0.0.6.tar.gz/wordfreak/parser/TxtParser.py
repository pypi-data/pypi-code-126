from wordfreak.parser.Parser import Parser


class TxtParser(Parser):
    """
    For use parsing .txt files.
    """

    @classmethod
    def getWordFrequency(cls, pathToTxtFile: str) -> dict[str, int]:
        # get all word frequencies from the given .txt file
        with open(pathToTxtFile) as file:
            lines = file.readlines()
        return cls._getWordFrequencyFromLines(lines)
