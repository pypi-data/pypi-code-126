type(1)


def foo(x, y=10):
    """foo doc"""
    return x + y


dir(foo)


class Bar:
    def __new__(cls, *args, **kwargs):
        print("new")
        return object.__new__(cls)

    def __init__(self):
        print("init")
        self.l = range(3)

    def __call__(self):
        return "Hello"

    def __iter__(self):
        return self.l.__iter__()

    def __enter__(self):
        print("Enter")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_val, exc_tb)
        print("Exit")
        return True

    def foo(self):
        return "foo"


b = Bar()
b()

for n in b:
    print(n)

with b:
    print("With bar")
    raise Exception("foo")

b.foo()
Bar.foo(1)
Bar.__dict__["foo"](1)
type(b).foo(b)
Bar.__dict__["foo"]
b.foo
Bar.foo

b.__setattr__("baz", lambda: "baz")
b.baz()
b.__getattribute__("foo")

foo = type("Foo", (object,), {"foo": lambda self: "foo"})
dir(foo)
foo.foo()
foo.__class__

int.__mul__(2, 4)

command = "save quit"
command = "foo"
command = "go east"
match command.split():
    case ["quit"]:
        print("quit")
    case ["save", "quit"]:
        print("save", "quit")
    case ["go", ("north" | "south" | "east" | "west") as direction]:
        print(f"go {direction}")
    case _:
        print("default")

print("\a")


class Dummy:
    def __str__(self):
        return "str"

    def __repr__(self):
        return "repr"


f"{Dummy() !r}"
s = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
