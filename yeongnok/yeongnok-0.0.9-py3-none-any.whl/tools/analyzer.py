"""

"""
import sys
from typing import Union

__all__ = ["get_activities_of"]


def get_activities_of(
    person, *, at: int = 0, path: str = ".", display: bool = False
) -> Union[None, list]:
    if at == 0:
        at = person.generation

    sys.path.append("..")
    from yeongnok.congressman import Congressman

    if not isinstance(person, Congressman):
        raise TypeError("Object must be of the type 'Congressman'")

    import os
    import re
    import csv
    import json
    import pprint

    suffix: str = (
        "st"
        if at % 10 == 1
        else "nd"
        if at % 10 == 2
        else "rd"
        if at % 10 == 3
        else "th"
    )
    matched: bool = False

    # # # Logic of analyzing file on disk
    # # # Same code reused later, by copy & pasting
    for file in os.listdir(path):
        if re.match(rf"[0]*{at}(st|nd|rd|th)", file) and file.endswith(".csv"):
            print(f"\n[ANALYZER] {path=}, {file=}, {at}{suffix} Assembly")
            result: list = []
            matched = True
            with open(f"{path}/{file}", "r") as f:
                print(
                    f"[SCANNING] {person.name}'s activities at {at}{suffix} assembly...\n"
                )
                reader = csv.reader(f)
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
            return None if result == [] else result

    print(
        f"[WARNING]  {at}{suffix}: CSV file not found in {'current directory' if path == '.' or './' else path}.\n"
        if not matched
        else "\n[OK]"
    )
    print(f"           Download from github? [yes/no]")
    user_input: str = input("\n[YES/no]:  ")
    if user_input.lower == "y" or "yes" or "ye" or "" or " ":
        import wget

        try:
            wget.download(
                f"https://github.com/anzhi0708/yeongnok/raw/main/{at}{suffix}_20220706-000000.csv"
            )
            for file in os.listdir():
                if re.match(rf"[0]*{at}(st|nd|rd|th)", file) and file.endswith(".csv"):
                    print(f"\n[ANALYZER] {path=}, {file=}, {at}{suffix} Assembly")
                    result = []
                    matched = True
                    with open(f"{file}", "r") as f:
                        print(
                            f"[SCANNING] {person.name}'s activities at {at}{suffix} assembly...\n"
                        )
                        reader = csv.reader(f)
                        for index, line in enumerate(reader):
                            data = json.loads(line[-1])
                            for i, d in enumerate(data):
                                if person.name in d["movieTitle"]:
                                    result.append(
                                        f"{d['realTime'] if d['realTime'] is not None else '        '} {person.name} {d['speakType']}, {line[0]} {line[1]} {line[2]}, {line[3]}, {d['movieTitle']}"
                                    )
                    if display:
                        for line in result:
                            pprint.pp(line)
                    return None if result == [] else result
        except:
            print("[DOWNLOAD] Could not download data.")

            print(f"           Download from 'https://w3.assembly.go.kr/' ? [yes/no]")
            user_input = input("\n[YES/no]:  ")
            if user_input.lower == "y" or "yes" or "ye" or "" or " ":

                import time

                start_time: str = time.strftime("%Y%m%d-%H%M%S")
                from yeongnok.site import page
                import time

                result = []
                for pg in page(1, -1, nth=at):
                    pg.to_csv(f"{path}/{at}{suffix}_{start_time}.csv")
                    print(f"[SCANNING] Page {pg.index}")
                    print(
                        f"           {pg.nb_current_page_items} records on page {pg.index}."
                    )
                    print(f"           Searching for {person.name}...\n")
                    for _d in pg.data:
                        d = json.loads(pg.data[_d]["essential_json"])
                        for o in d:
                            if person.name in o["movieTitle"]:
                                print(
                                    f"[FOUND]    {person.name} {o['speakTime']}, {line[1]}"
                                )
                                print(f"           {o['movieTitle']}\n")
                                result.append(
                                    f"{o['realTime'] if o['realTime'] is not None else '        '} {person.name} {o['speakType']}, {line[0]} {line[1]} {line[2]}, {line[3]}, {o['movieTitle']}"
                                )
                if display:
                    for line in result:
                        pprint.pp(line)
                return result

    return [f"{at}{suffix} - file not found, skipping."]
