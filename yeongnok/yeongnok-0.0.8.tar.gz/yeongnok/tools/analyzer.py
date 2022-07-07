"""

"""


def get_activities_of(person: str, *, at: int, path: str = ".", display: bool = False) -> list:
    import os
    import re
    import csv
    import json
    import pprint

    suffix: str = "st" if at % 10 == 1 else "nd" if at % 10 == 2 else "rd" if at % 10 == 3 else "th"
    matched: bool = False

    for file in os.listdir(path):
        if re.match(rf"[0]*{at}(st|nd|rd|th)", file) and file.endswith(".csv"):
            result: list = []
            print(f"[FOUND]    {file}")
            matched = True
            with open(f"{path}/{file}", "r") as f:
                print(f"[LOADING]  {path}/{file}")
                reader = csv.reader(f)
                print(
                    f"[BEGIN]    Searching {person.name}'s activities at {at} assembly...")
                for index, line in enumerate(reader):
                    data: dict = json.loads(line[-1])
                    for i, d in enumerate(data):
                        if person.name in d["movieTitle"]:
                            result.append(
                                f"{d['realTime'] if d['realTime'] is not None else '        '} {person.name} {d['speakType']}, {line[0]} {line[1]} {line[2]}, {line[3]}, {d['movieTitle']}"
                            )
            if display:
                for line in result:
                    pprint.pp(line)
            return result

    print(
        f"[WARNING]  {at}{suffix}: Data not found on disk ({path}).\n" if not matched else "\n[OK]")
    print(f"           Search on: 'https://w3.assembly.go.kr/' ? [yes/no]")
    user_input: str = input("[YES/no]:  ")
    if user_input.lower == "y" or "yes" or "ye" or "" or " ":
        import sys
        sys.path.append("..")
        from yeongnok.site import page
        result = []
        for pg in page(1, -1, nth=at):
            for _d in pg.data:
                print(f"[INFO]     Searching on page {pg.index}...")
                d = json.loads(pg.data[_d]['essential_json'])
                for o in d:
                    if person.name in o["movieTitle"]:
                        print(
                            f"[FOUND]    {person.name} {o['speakTime']}, {line[1]}")
                        print(f"           {o['movieTitle']}\n")
                        result.append(
                            f"{o['realTime'] if o['realTime'] is not None else '        '} {person.name} {o['speakType']}, {line[0]} {line[1]} {line[2]}, {line[3]}, {o['movieTitle']}"
                        )
        if display:
            for line in result:
                pprint.pp(line)
        return result
    return [f"{at}{suffix} - file not found, skipping."]
