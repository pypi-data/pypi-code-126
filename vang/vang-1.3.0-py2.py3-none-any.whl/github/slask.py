from dataclasses import dataclass

from vang.misc.util import thread_first, thread_last


def foo(f):
    print('decorator')

    def inner(*args, **kwargs):
        print('before')
        result = f(*args, **kwargs)
        print('after')
        return result

    return inner


@foo
def add(x, y):
    return x + y


add(3, 4)


@dataclass
class Bar:
    name: str
    number: int

    def do_it(self) -> int:
        return self.number


bar = Bar('a_name', 1)
bar

from functools import partial, reduce


def tf(arg, *partials):
    fs = [partial(f, *args) for f, args in partials]
    print(fs)
    return reduce(lambda mem, f: f(mem), fs, arg)


tf(1,
   (add, [2]))

# def thread_first(arg, *partials):
#     return reduce(lambda mem, p: p[0](mem, *p[1:]) if len(p) > 1 else p[0](mem), partials, arg)
#
#
# def thread_last(arg, *partials):
#     return reduce(lambda mem, p: p[0](*p[1:], mem) if len(p) > 1 else p[0](mem), partials, arg)


from operator import add

thread_first('a',
             [add, 'b'],
             [lambda x: x],
             [add, 'c'])

thread_first(0,
             [add, 1],
             [lambda x: x * 2],
             [add, 1])

thread_last('a',
            [add, 'b'],
            [lambda x: x],
            [add, 'c'])

thread_first('abc',
             (str.replace, 'b', 'x'),
             (add, 'y'))

thread_last('a',
            (add, 'b'),
            (add, 'c'))
