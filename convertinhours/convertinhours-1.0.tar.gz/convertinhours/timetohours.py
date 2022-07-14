def Time_to_Hours(x):
    if len(x) == 1:
        if x[0][1] == "d":
            days = round(x[0][0] * 24, 2)
            return days
        elif x[0][1] == "h":
            hours = round(x[0][0], 2)
            return hours
        elif x[0][1] == "m":
            minutes = round(x[0][0] / 60, 2)
            return minutes
        else:
            return "NO"
    elif len(x) == 2:
        if x[0][1] == "d" and x[1][1] == "h":
            days = round(x[0][0] * 24, 2)
            hours = round(x[1][0], 2)
            fv = days + hours
            return fv
        elif x[0][1] == "h" and x[1][1] == "m":
            hours = round(x[0][0], 2)
            minutes = round(x[1][0] / 60, 2)
            fv = hours + minutes
            return fv 
        elif x[0][1] == "d" and x[1][1] == "m":
            days = round(x[0][0] * 24, 2)
            minutes = round(x[1][0] / 60, 2)
            fv = days + minutes
            return fv
    else:
        days = round(x[0][0] * 24, 2)
        hours = round(x[1][0], 2)
        minutes = round(x[2][0] / 60, 2)
        fv = days + hours + minutes
        return fv






















"""


def Time_to_Hours(x):
    if len(x) == 1:
        if x[0][1] == "d":
            days = round(x[0][0] * 24, 5)
            return days
        elif x[0][1] == "h":
            hours = round(x[0][0], 5)
            return hours
        elif x[0][1] == "m":
            minutes = round(x[0][0] / 60, 5)
            return minutes
        else:
            return "NO"
    elif len(x) == 2:
        if x[0][1] == "d" and x[1][1] == "h":
            days = round(x[0][0] * 24, 5)
            hours = round(x[1][0], 5)
            fv = days + hours
            return fv
        elif x[0][1] == "h" and x[1][1] == "m":
            hours = round(x[0][0], 5)
            minutes = round(x[1][0] / 60, 5)
            fv = hours + minutes
            return fv 
        elif x[0][1] == "d" and x[1][1] == "m":
            days = round(x[0][0] * 24, 5)
            minutes = round(x[1][0] / 60, 5)
            fv = days + minutes
            return fv
    else:
        days = round(x[0][0] * 24, 5)
        hours = round(x[1][0], 5)
        minutes = round(x[2][0] / 60, 5)
        fv = days + hours + minutes
        return fv




"""