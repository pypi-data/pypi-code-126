from donation_alerts_handler.types.donations import Donations


def minimum_value(n: int):
    async def f(donate: Donations):
        return n <= donate.amount

    return f


def maximum_value(n: int):
    async def f(donate: Donations):
        return n >= donate.amount

    return f


def message_prefix(s: str):
    async def f(donate: Donations):
        return donate.message.startswith(s)

    return f


def name_prefix(s: str):
    async def f(donate: Donations):
        return donate.name.startswith(s)

    return f


def currency(s: str):
    async def f(donate: Donations):
        return donate.currency == s

    return f
