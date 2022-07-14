def DigitExtractor(input_value):
    processed_value = []
    if isinstance(input_value,float):
        processed_value.append("NO")
    elif input_value == "Not Available" or input_value == "Expected First Response Time" or input_value == "Actual First Response Time" or input_value == "Expected Resolution Time" or input_value == "Actual Resolution Time":
        processed_value.append("NO")
    else:
        split_vale = input_value.split()
        for i in range(len(split_vale)):
            if split_vale[i].isdigit():
                string_lower = split_vale[i+1].lower()
                processed_value.append((float(split_vale[i]), string_lower[0]))
    return processed_value