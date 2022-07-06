# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import random
import string
import itertools

# Custom Library

# Custom Packages
from AthenaMock.functions.generators_seed import generate_random_seed

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
CHOICES = string.ascii_letters + string.digits + string.punctuation

def generate_password(
        seed=None,
        *,
        length_min:int=6,
        length_max:int=32
):
    # if the seed is undefined, generate a random one
    if seed is None:
        seed = generate_random_seed()

    random.seed(seed)
    return "".join(random.sample(CHOICES,random.randint(length_min, length_max)))

def generate_password_fixed_length(
        seed=None,
        *,
        length:int=32
):
    # if the seed is undefined, generate a random one
    if seed is None:
        seed = generate_random_seed()

    random.seed(seed)
    return "".join(random.sample(CHOICES,length))