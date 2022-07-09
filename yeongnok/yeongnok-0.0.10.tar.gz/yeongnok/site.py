"""
    This program was written on July 2nd, 2022
    by Anji Wong (anzhi0708@hufs.ac.kr, anzhi0708@gmail.com),
    **for research use only.**

    Even through I tried to access KR Assembly data by
    using its Open API service,
    some critical data was missing in the returned json / xml string.

    So I had to manually write this web crawler.
    Hopefully this will help me finishing my paper.

    Since we are trying to keep sending http requests
    to the KR Assembly website,
    we have to keep the request's frequency on a relatively low level,
    **so that we won't be end up in jail.**
    This is important, especially when you have no basic knowledge of
    the principles of http services.
    So please always write `time.sleep(n)` and keep n greater than 2.
"""
import os
import re
import csv
import sys
import json
import time
import faker
import datetime
import requests
from typing import Union
from objprint import add_objprint

__all__ = ["page"]


@add_objprint
class Page:
    """A specific web page of KR Assembly video data page.
    With 'objprint', you can simply print the object
    like this: print(my_instance)
    to see its properties.
    """

    def __init__(self, *, nth: int, index: int = 1) -> None:

        GEN_PERIOD = {
            19: (2012, 2016),
            18: (2008, 2012),
            17: (2004, 2008),
            16: (2000, 2004),
            15: (1996, 2000),
            14: (1992, 1996),
            13: (1988, 1992),
            12: (1985, 1988),
            11: (1981, 1985),
            10: (1979, 1980),
            9: (1973, 1979),
            8: (1971, 1972),
            7: (1967, 1971),
            6: (1963, 1967),
        }
        self.time_begin: str = time.strftime("%Y%m%d-%H%M%S")

        if not isinstance(nth, int) or not isinstance(index, int):
            raise TypeError("Argument type must be integer")

        # We currently are only interested in the 20th & 21st assembly.
        # And since only 6 to 21 are available on the official website,
        # (nth > 21) or (nth < 6) not allowed.
        if nth > 21 or nth < 6:
            raise IndexError(
                "\n\tIn 2022 (this year), \n\tassembly index must be in range 6th to 21st (21 included)"
            )

        # Which year is this year?
        current_year: int = datetime.date.today().year

        # If any (not improtant) error occurs,
        # add it to this list.
        # This list will be printed out
        # at the end of a loop.
        self.errors: list = []  # log

        self.total: int = 0  # Maximum page number.
        # self.total is the REAL maximum index possible.

        self.nb_current_page_items: int = 0  # Number of current page's items.
        self.data: dict = {}  # After processing json data,
        # we store some significant info here.

        self.start_year: int = 0  # Assembly period.
        self.end_year: int = 0

        self.nth: Union[int, str] = nth  # nth assembly
        self.__suffix: str = (
            "st"
            if str(self.nth)[-1] == "1"
            else "nd"
            if str(self.nth)[-1] == "2"
            else "rd"
            if str(self.nth)[-1] == "3"
            else "th"
        )  # For friendly console outputs.

        # Since we are only interested in 20th & 21st assembly,
        # we write some basic logic here...
        # also, this program is now being written, in July 2022
        if self.nth == 20:
            self.start_year = 2016
            self.end_year = 2020
        elif self.nth == 21:
            self.start_year = 2020
            self.end_year = current_year if current_year <= 2024 else 2024

        else:
            self.start_year = GEN_PERIOD[self.nth][0]
            self.end_year = GEN_PERIOD[self.nth][1]
            # Also have to turn '9' to '09', etc.

        if self.nth < 10:
            self.nth = f"0{self.nth}"
        else:
            self.nth = str(self.nth)

        # Target URL for sending http request.
        self.url: str = ""

        self.index: int = 1  # Current page number.
        self.__ok: bool = False  # Http request status.
        self.__json: dict = {}  # The data we need.

        # This 'self.index_max' is used as a init flag, too.
        # If its value is zero, the program sees the Page object
        # as 'Not Initialized'.
        # Then the 'refresh' method will be called,
        # causing the Page object to be updated to page 1.
        # It's not always equal to self.total.
        # self.total always holds the max index number.
        # That is, 'self.total' is the REAL 'total page number' value.
        # Which means,
        # if using `page(start, end, nth_assembly)` for a range,
        # then (self.index_max <= self.total) is True.
        self.index_max: int = 0  # Max(or a range's end) page number.

        # initializing
        print("Initializing".center(os.get_terminal_size()[0], "-"))
        print("[INIT]     Initializing data (sending request, index = 1)...")
        self.refresh(1)
        self.total = self.index_max
        # Printing log

        print(f"           Initialized.")
        print(
            f"{self.nth}{self.__suffix} assembly".center(os.get_terminal_size()[0], "-")
        )
        if index != 1:
            self.index = index
            self.refresh(self.index)  # Updating data

    # The method 'refresh' partly does the initialization job, too.
    # But it also dynamiclly updates Page object (json data) by:
    # (some Page object).refresh(page number)
    # Arguments:
    #    _index: int
    #        The requested page number.
    #    delta_time: int | float
    #        Time seperation between the page's
    #        each record. Defaults to 1.5
    def refresh(self, _index: int, delta_time: Union[int, float] = 1.5) -> None:
        """Updates json data and current page index."""
        print("[PAGE]     Refreshing...")

        self.data = {}  # Clear the dict for initializing the page
        if self.index_max == 0:  # If the page not initialized

            # Seems like this line is not really needed,
            # but we leave it as it is for debugging reasons.
            print(f"[PAGE]     Initializing {self.__class__.__name__} object...")

            url = f"https://w3.assembly.go.kr/vod/main/service/list.do?cmd=subList&menu=1&ct1={self.nth}&mc=&searchUpdateDate={self.start_year}&searchUpdateDate2={self.end_year}&searchCt2=&searchType_id=&mc_param2=&searchSelect=1&searchString=&curPages=1&vv={int(time.time())}&"
            respond = requests.get(
                url, headers={"User-Agent": faker.Faker().user_agent()}
            )
            self.__json = json.loads(respond.content)
            print("[PAGE]     JSON loaded.")

            # Done initializing

            try:
                self.index_max = int(self.__json["paging"]["moveLast"])
            except ValueError:
                self.index_max = 1

            print(
                f"           Maximum page index is {self.index_max} ({self.nth}{self.__suffix} assembly)"
            )
            self.url = url
            print("[READY]    Ready.")
            return None
        else:  # If already has data
            print(f"[UPDATE]   Trying to get new page (page {_index})")
            if _index > self.index_max:
                print(f"[WARNING]  Index {_index} / {self.total} does not exist.")
                _index = self.index_max
                print(f"           Resetting index '{_index}' to {self.total}...")
                self.index = _index
                print(
                    f"[PAGE]     Page number has been reset to {self.index} / {self.total}."
                )

            if _index < 1:
                print(f"[INFO]     Getting the first page...")
                self.index = 1
            else:
                self.index = _index
                print(
                    f"[PAGE]     Page number has been updated to {self.index} / {self.total}."
                )

        url = f"https://w3.assembly.go.kr/vod/main/service/list.do?cmd=subList&menu=1&ct1={self.nth}&mc=&searchUpdateDate={self.start_year}&searchUpdateDate2={self.end_year}&searchCt2=&searchType_id=&mc_param2=&searchSelect=1&searchString=&curPages={self.index}&vv={int(time.time())}&"
        respond = requests.get(url, headers={"User-Agent": faker.Faker().user_agent()})
        self.__ok = respond.ok
        self.__json = json.loads(respond.content)
        self.url = url

        # The visual data we can actually see on the website.
        print(f"[CONFIG]   Time interval: {delta_time} seconds.")
        for each in self.__json["confList"]:
            tmp = {}
            tmp["date"] = each["confDate"]
            tmp["time"] = each["confOpenTime"]
            tmp["group"] = each["commName"]

            if "," in each["confTitle"]:
                self.errors.append(
                    f"[LOG]      {self.nth}{self.__suffix}, page {self.index},"
                )
                self.errors.append(
                    f"               title '{each['confTitle']}':\n               Comma found in title."
                )
                # raise RuntimeError("There's a comma in the title. Not your fault tho.")
                print(f"\n[WARNING]  Comma detected: {each['confTitle']}.")
                print("           Replacing the comma (',') with ‘，’.")
                each["confTitle"] = each["confTitle"].replace(",", "，")
                print("\n[OK]       Comma replaced.")
            tmp["title"] = each["confTitle"]

            # 'Type' can have multiple elements. For example,
            # one meeting can be both '청문회' and '소위원회'.
            if len(each["angunType"]) == 0:
                tmp["type"] = ""
            elif len(each["angunType"]) == 1:
                tmp["type"] = each["angunType"][0]["name"]
            else:
                type_list = []
                for each_obj in each["angunType"]:
                    type_list.append(each_obj["name"])
                tmp["type"] = "+".join(type_list)

            link = f"https://w3.assembly.go.kr/vod/main/player.do?menu=1&mc={each['mc']}&ct1={self.nth}&ct2={each['ct2']}&ct3={each['ct3']}&wv=1&"
            tmp["link"] = link
            tmp["ct1"] = each["ct1"]
            tmp["ct2"] = each["ct2"]
            tmp["ct3"] = each["ct3"]

            # The 'mc' argument in the url contains not only numbers, but also alphabets.
            mc: str = ""
            mc = re.findall(r"mc=[^&]*", link)[0].replace("mc=", "")

            essential_link: str = f"https://w3.assembly.go.kr/vod/main/service/movie.do?cmd=movieInfo&mc={mc}&ct1={self.nth}&ct2={tmp['ct2']}&ct3={tmp['ct3']}&no=&wv=1&vv={int(time.time())}&"
            try:
                tmp["essential_json"] = json.dumps(
                    json.loads(requests.get(essential_link).content)["movieList"][0][
                        "subList"
                    ]
                )
            except KeyError:
                print(f"[WARNING]  {tmp['date']} {tmp['time']}")
                print(f"           {tmp['title']}")
                print("           Seems like nobody spoke that day")
                tmp["essential_json"] = "{}"
                print("           Check its link for more:\n")
                print(link)
                print()
                self.errors.append(f"[WARNING]   {tmp['date']} {tmp['time']}")
                self.errors.append(f"            {tmp['title']}")
                self.errors.append("            Seems like nobody spoke that day.")
                self.errors.append(f"Check {link} for more.\n")

            tmp_title_suffix: str = f" ({tmp['type']})" if tmp["type"] != "" else ""
            print(
                f"[LOADING]  {tmp['date']} {tmp['time']} {tmp['group']}"
                + tmp_title_suffix
            )
            time.sleep(delta_time)

            self.data[
                tmp["date"]
                + " "
                + tmp["time"]
                + " "
                + tmp["title"]
                + f" #{tmp['ct1']}_{tmp['ct2']}_{tmp['ct3']}"
            ] = tmp

        self.nb_current_page_items = len(self.to_list())
        if self.nb_current_page_items != 10 and self.index != self.total:
            raise IndexError(
                f"This page should have 10 items, instead it has {self.nb_current_page_items} items. This should not happen, and you might want to check the web page."
            )
        print(
            f"[PAGE]     Loaded page {self.index} of {self.nth}{self.__suffix} assembly."
        )

    def to_csv(
        self,
        target_path: str = "",
        write_header: bool = False,
    ) -> None:

        if target_path == "":
            target_path = f"{self.nth}{self.__suffix}_{self.time_begin}.csv"

        field_names = [
            "date",
            "time",
            "group",
            "title",
            "type",
            "link",
            "ct1",
            "ct2",
            "ct3",
            "essential_json",
        ]
        with open(target_path, "a+", encoding="UTF-8") as output:
            writer = csv.DictWriter(output, fieldnames=field_names)
            if write_header:
                writer.writeheader()
            for each in self.data.keys():
                writer.writerow(self.data[each])
            print(f"\n[SAVED]    Page {self.index} saved to:")
            print(f"           '{target_path}'")
            print("\n[OK]\n")

    def filter(self, *, key: str, value: str) -> list:
        result: list = []
        for each in self.data.keys():
            tmp: dict = {}
            if self.data[each][key] == value:
                tmp[each] = self.data[each]
                result.append(tmp)
                del tmp
        return result

    def to_list(self) -> list:
        result: list = []
        for each in self.data:
            result.append(self.data[each])
        return result

    def __iter__(self):
        def gen(p):
            while p.index <= p.index_max:
                if p.index < p.index_max:
                    yield p
                    print("[LOOPING]  Getting the next page ;-)\n")
                    p.refresh(p.index + 1)
                if p.index == p.index_max:
                    print("[LOOPING]  Ops, this is the last page!\n")
                    print("[OK]       Finished ;-)")
                    if len(self.errors) != 0:
                        for e in self.errors:
                            print(e)
                    else:
                        print("[FINISHED] MANSE! No error found.")
                    yield p
                    break
            return

        return gen(self)


class page:
    """An object similar to the built-in 'range' object."""

    __slots__ = "start", "end", "nth", "page"

    def __init__(self, start: int, end: int, *, nth: int):
        self.start: int = 0
        self.end: int = 0
        if not isinstance(start, int) or not isinstance(end, int):
            raise TypeError("Page range args must be integers.")
        if not isinstance(nth, int):
            raise TypeError("Arg 'nth' must be a integer.")

        # Initializing.
        self.page: Page = Page(nth=nth)
        # After initializing, we got `self.page.total` and
        # every other stuff.

        if start > self.page.total:
            print(f"[RANGE]    Invalid start value '{start}',")
            print(f"           resetting to {self.page.total}...")
            self.start = self.page.total
        elif start < 0:
            self.start = self.page.total + start + 1
        elif start == 0:
            self.start = 1
        else:
            self.start = start

        self.page.refresh(self.start)

        if end > self.page.total:
            print(f"[RANGE]    Invalid end value '{end}',")
            print(f"           resetting to {self.page.total}...")
            self.end = self.page.total
        elif end < self.start:
            if end == 0:
                print("[RANGE]    Will loop through all indexes.")
                self.end = self.page.total
            elif end < 0:
                self.end = end + self.page.total + 1
            else:
                print(f"[RANGE]    Invalid end value '{end}',")
                print(f"           resetting to {self.page.total}...")
                self.end = self.page.total
        else:
            self.end = end

        self.page.index_max = self.end

    def __iter__(self):
        return iter(self.page)


def from_cli(
    *, delta: int, nth: int, start: int = 1, end: int = -1, csv_path: str = ""
):

    flag_csv = False

    if csv_path != "":
        print(f"[RUNNING]  CSV data will be saved here: {csv_path}")
        flag_csv = True
    else:
        print("[RUNNING]  Output will not be written to disk.")

    for p in page(start, end, nth=nth):
        print(f"[LOOPING]  Sleeping for {delta} seconds...")
        time.sleep(delta)
        if flag_csv:
            p.to_csv(csv_path)
            print(f"[CSV]      Written to CSV file {csv_path}")


if __name__ == "__main__":
    args = sys.argv
    argc: int = 0
    delta: int = 3
    nth: int = 0
    start: int = 0
    end: int = 0
    csv_path: str = ""

    for index, e in enumerate(args):
        if e == "--start" or e == "-s":
            start = int(args[index + 1])
            argc += 1
        if e == "--end" or e == "-e":
            end = int(args[index + 1])
            argc += 1
        if e == "--csv":
            csv_path = args[index + 1]
        if e == "--nth" or e == "-n":
            nth = int(args[index + 1])
            argc += 1
        if e == "--delta" or e == "-d":
            delta = int(args[index + 1])

    if argc == 3:
        from_cli(nth=nth, start=start, end=end, csv_path=csv_path, delta=delta)
    else:
        raise ValueError(
            "Invalid argument.\nUsage:\n\t-d | --delta [seconds]\n\t-n | --nth <generation>\n\t-s | --start <start_index>\n\t-e | --end <end_index>\n\t--csv <output_csv_path>"
        )
