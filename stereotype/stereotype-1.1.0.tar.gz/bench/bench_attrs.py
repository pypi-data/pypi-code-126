from __future__ import annotations

from typing import List, Optional

from attrs import define, field, asdict
from bench.common import execute, benchmark_cpu, memory_bench


@define
class BaseStuff:
    name: str = field()
    flag: bool = field(default=False)

    @name.validator
    def name_min_length_2(self, attribute, v):
        if len(v) < 2:
            raise ValueError('must be at least 2 characters long')


@define
class ListStuff(BaseStuff):
    stuff: Stuff = field(converter=lambda data: Stuff(**data), default=None)
    list: List[str] = field(default=list)

    @list.validator
    def list_min_length_1(self, attribute, v):
        if len(v) < 1:
            raise ValueError('must have at least 1 items')


@define
class ModelStuff:
    value: float
    def_value: float = field(default=4.2)


@define
class Stuff(BaseStuff):
    model: ModelStuff = field(converter=lambda data: ModelStuff(**data), default=None)
    items: List[ListStuff] = field(converter=lambda data: [ListStuff(**item) for item in data], default=list)
    optional: Optional[int] = field(default=None)
    strange: Optional[float] = field(default=4.7)

    @optional.validator
    def flag_set_if_not_optional(self, attribute, optional):
        if not self.flag and optional is None:
            raise ValueError('Must be true if optional is not set')


if __name__ == '__main__':
    def benchmark(inputs: List[dict], validate: bool):
        for data in inputs:
            model = Stuff(**data)
            yield asdict(model)

    benchmark_cpu(benchmark, depth=4, validate=True)
    # memory_bench(lambda data: Stuff(**data), lambda model: asdict(model), 10000, 4)  # 339MB
