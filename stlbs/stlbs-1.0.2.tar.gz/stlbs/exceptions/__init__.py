class SubtractionBelowZeroError(Exception):
    def __str__(self):
        return "The result of subtracting from an StLb object cannot be below zero"
