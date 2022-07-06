# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import random

# Custom Library
from AthenaLib.functions.random import random_bool

# Custom Packages
from AthenaMock.functions.generators_seed import generate_random_seed
from AthenaMock.usernames.data.enclosing import ENCLOSING
from AthenaMock.usernames.data.names import NAMES, NAMES_ADJECTIVES
from AthenaMock.usernames.data.end import END
from AthenaMock.usernames.data.seperations import SEPARATIONS

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------

def generate_username(
        seed=None,
        *,
        probability_separation:float =          1/5,
        probability_adjective:float =           1/2,
        probability_capitalize:float =          1/2,
        probability_end:float=                  1/5,
        probability_end_number:float=           1/10,
        probability_enclosing:float=            1/4,
        probability_enclosing_no_start:float=   1/12,
        probability_enclosing_no_end:float=     1/12,
):
    # if the seed is undefined, generate a random one
    if seed is None:
        seed = generate_random_seed()

    # define and use the seed
    #   if a same seed is used, the same username will be generated
    random.seed(seed)

    #generate the bare name
    sep = random.choice(SEPARATIONS) if random_bool(probability_separation) else ""
    name = sep.join(
        name.capitalize() if random_bool(probability_capitalize) else name
        for name in {random.choice(NAMES) for _ in range(random.randint(1, 3))}
    )

    # add a random adjective in front 1/2 chance by default
    adjective =  random.choice(NAMES_ADJECTIVES) if random_bool(probability_adjective) else ""

    # decide if the username has to have some sort of end partial
    end = (
        "".join(str(random.randint(0,9)) for _ in range(random.randint(0, 5)))
        if random_bool(probability_end_number) else random.choice(END)
    ) if random_bool(probability_end) else ""

    # decide if the enclosing will be present or not
    #   Also has a specific chance not to generate one side at all
    enclose = random.choice(ENCLOSING) if random_bool(probability_enclosing) else ""
    enclose_start = "" if random_bool(probability_enclosing_no_start) else enclose
    enclose_end = "" if random_bool(probability_enclosing_no_end) else enclose[::-1]

    # return the name fully assembled
    return f"{enclose_start}{adjective}{name}{enclose_end}{end}"
