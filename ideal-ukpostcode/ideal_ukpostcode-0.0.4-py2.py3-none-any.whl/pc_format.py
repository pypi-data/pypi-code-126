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
    
    try:
        validate_areacode(area)
    except:
        print("Invalid Area Code")

    try:
        validate_districtcode(district)
    except:
        print("Invalid District Code")
    
    try:
        validate_sectorcode(str(sector))
    except:
        print("Invalid Sector Code")
    
    try:
        validate_unitcode(unit)
    except:
        print("Invalid Unit Code")

    outward_code = area + district
    inward_code = str(sector) + unit

    return outward_code + " " + inward_code