import re
import typing
from .tools import analyzer
from dataclasses import dataclass


__all__ = ["Congressman", "List"]


@dataclass
class Congressman:
    __slots__ = (
        "generation",
        "name",
        "party",
        "group",
        "region",
        "gender",
        "n",
        "how",
    )
    generation: int
    name: str
    party: str
    group: typing.Union[list, str]
    region: str
    gender: str
    n: int
    how: str

    def __eq__(self, o: str) -> bool:
        if o == self.name:
            return True
        return False

    def __gt__(self, o) -> bool:
        return True if o.n < self.n else False

    def __lt__(self, o) -> bool:
        return True if self.n < o.n else False

    @property
    def activities(self) -> list:
        result = []
        for n in range(21, 6, -1):
            result.append(analyzer.get_activities_of(self, at=n))
        return result

    @property
    def is_male(self) -> bool:
        return self.gender == "남"

    @property
    def is_female(self) -> bool:
        return self.gender == "여"


class List:
    __slots__ = "generation", "members", "male", "female"

    def __init__(self, generation: typing.Union[int, list]):
        self.generation = generation
        self.members: typing.List[Congressman] = []
        import os
        import csv

        this_module_path = os.path.realpath(__file__).replace("/congressman.py", "")
        number_prefix: typing.Union[None, str] = (
            ""
            if isinstance(generation, int) and generation > 9
            else "0"
            if isinstance(generation, int) and generation <= 9
            else None
        )
        with open(
            f"{this_module_path}/{number_prefix}{generation}_congressman_list.csv",
            "r",
            encoding="UTF-8",
        ) as ls:
            reader = csv.reader(ls)
            for row in reader:
                self.members.append(
                    Congressman(
                        generation if isinstance(generation, int) else -1,
                        row[2],
                        row[3],
                        [] if row[4] == "" else row[4],
                        row[5],
                        row[6],
                        1
                        if row[7] == "초선"
                        else 2
                        if row[7] == "재선"
                        else int(re.findall(r"[0-9]+", row[7])[0]),
                        row[8],
                    )
                )
            self.male: int = 0
            self.female: int = 0
            for individual in self.members:
                if individual.gender == "남":
                    self.male += 1
                elif individual.gender == "여":
                    self.female += 1
                else:
                    ...

    def __iter__(self):
        return iter(self.members)

    def __len__(self):
        return len(self.members)

    @property
    def total(self):
        return len(self.members)

    def __getitem__(self, x):
        return self.members.__getitem__(x)

    def __repr__(self):
        if isinstance(self.generation, list):
            _ls_gen_nb: list = []
            for nb in self.generation:
                _ls_gen_nb.append(str(nb))
            return f"<{' and '.join(_ls_gen_nb)} Congressman List, combined>"
        prefix = (
            "st"
            if self.generation % 10 == "1"
            else "nd"
            if self.generation % 10 == "2"
            else "rd"
            if self.generation % 10 == "3"
            else "th"
        )
        return f"<{self.generation}{prefix} Congressman List (male: {self.male}; female: {self.female}; total: {len(self.members)})>"

    def __add__(self, o: typing.Union["List", str]) -> "List":
        if isinstance(o, str):  # If given a name
            __list = List(self.generation)
            __person = Congressman(
                name=o,
                generation=0,
                party="",
                group="",
                region="",
                gender="",
                n=0,
                how="",
            )
            __list.members.append(__person)
            return __list
        elif isinstance(o, List):
            __list = List(self.generation)
            __list.members += o.members
            __list.generation = [self.generation, o.generation]
            return __list

    def filter(self, **kwargs) -> typing.List[Congressman]:
        result: typing.List[Congressman] = []
        for individual in self.members:
            flag_match: bool = True
            for key in kwargs:
                if individual.__getattribute__(key) != kwargs[key]:
                    flag_match = False
            if flag_match:
                result.append(individual)
        return result

    @property
    def males(self) -> list:
        result = []
        for person in self.members:
            if person.gender == "남":
                result.append(person)
        return result

    @property
    def females(self) -> list:
        result = []
        for person in self.members:
            if person.gender == "여":
                result.append(person)
        return result
