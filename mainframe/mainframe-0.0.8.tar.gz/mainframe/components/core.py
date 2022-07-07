import pyro


def deterministic(name: str, expression):
    return pyro.deterministic(name, expression)

def stochastic(name: str, distribution):
    return pyro.sample(name, distribution)
