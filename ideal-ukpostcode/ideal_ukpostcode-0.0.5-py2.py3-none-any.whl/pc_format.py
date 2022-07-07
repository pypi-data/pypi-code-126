import re

def validate_areacode(area):
    # Validate a uk postcode area
    # input = The postcode area is either one or two characters long and is alphabetical.
    # return = A boolean result with whether the postcode area is valid or not

    result = bool(re.match("[A-Z]{1,2}$", area))
    return result

def validate_districtcode(district):
    # Validate a uk postcode district
    # input = The postcode district is one digit, two digits or a digit followed by a letter.
    # return = A boolean result with whether the postcode area is valid or not

    result = bool(re.match("[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA", district))
    return result

def validate_sectorcode(sector):
    # Validate a uk postcode sector
    # input = The postcode sector is made up of a single digit
    # return = A boolean result with whether the postcode sector is valid or not

    result = bool(re.match("\d$", sector))
    return result

def validate_unitcode(unit):
    # Validate a uk postcode unit
    # input = The postcode unit is two characters
    # return = A boolean result with whether the postcode sector is valid or not

    result = bool(re.match("[A-Z]{2}$", unit))
    return result
    
def format(area, district, sector, unit):
    
    if not validate_areacode(str(area)):
        raise Exception("Invalid Area Code")

    if not validate_districtcode(str(district)):
        raise Exception("Invalid District Code")
    
    if not validate_sectorcode(str(sector)):
        raise Exception("Invalid Sector Code")
    
    if not validate_unitcode(str(unit)):
        raise Exception("Invalid Unit Code")

    outward_code = area + district
    inward_code = str(sector) + unit

    return outward_code + " " + inward_code