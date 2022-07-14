from .digitextractor import DigitExtractor
from .timetohours import Time_to_Hours

def conversionHours(x):
    result = []
    for i in x:
        output_from_digitextractor = DigitExtractor(i)
        output_from_time_to_hours = Time_to_Hours(output_from_digitextractor)
        result.append(output_from_time_to_hours)
    return result