from atexit import register
from typing import Callable, List
from functools import reduce
from operator import xor


class FlowDigest:


    @staticmethod
    def simple_hash_op(size: int) -> Callable[[int, int], int]:
        def hash_op(a: int, b: int) -> int:
            for _ in [None] * size:
                if a & 1:
                    # if 1 prefer 0s
                    (b, a) = ((b + a - 1) % (2 ** size), a & b)
                else:
                    # if 0 prefer 1s
                    (b, a) = ((b - a + 1) % (2 ** size), a | b)
                # clylic shift
                a <<= 1
                if (a & (2 ** size)): a += 1
                a %= 2 ** size
            return a
        return hash_op


    def __init__(self, address_size: int, bit_count: int, digest: List[int] = None, hash_op: Callable[[int, int], int] = None, fold_register: int = 0):

        # check that address_size fits within the bitcount
        if address_size > bit_count:
            raise ValueError(f"address_size ({address_size}) must be <= bit_count ({bit_count})")

        # check that digest is properly addressable
        if digest is None:
            digest = [0] * (2 ** address_size)
        elif len(digest) != 2 ** address_size:
            raise ValueError(f"digest must be of length 2 ** address_size ({address_size})")

        # default hash_op is simple_hash_op
        if hash_op is None:
            hash_op = FlowDigest.simple_hash_op(address_size)

        # const props
        self.address_size = address_size
        self.bit_count = bit_count
        self.register_count = bit_count - address_size

        self.hash_op = hash_op # val #= x :: val = hash_op(val, x)

        # state
        self.digest = digest
        self.state_registers = [0] * self.register_count
        self.fold_register = 0

        self.instruction_address = 0

    
    def execute(self):
        # fetch
        instruction = self.digest[self.instruction_address]
        # decode
        goto = instruction % (2 ** self.address_size)
        register_io = instruction >> self.address_size
        # execute
        input_registers = [i for i in range(self.register_count) if register_io & (1 << i)]
        output_registers = [i for i in range(self.register_count) if not register_io & (1 << i)]
        # go to address
        while self.instruction_address != goto:
            # churn digest: fold, *output_registers #= x #= fold, *input_registers
            input_value = self.fold_register
            for i in input_registers: input_value ^= self.state_registers[i]
            self.digest[self.instruction_address] = self.hash_op(self.digest[self.instruction_address], input_value)
            self.fold_register = self.hash_op(self.fold_register, self.digest[self.instruction_address])
            for i in output_registers: self.state_registers[i] = self.hash_op(self.state_registers[i], self.digest[self.instruction_address])
            # incriment memory address
            self.instruction_address += 1
            self.instruction_address %= 2 ** self.address_size
        # invert input and output for final churn, *input_registers #= x #= fold, *output_registers
        input_value = self.fold_register
        for i in output_registers: input_value ^= self.state_registers[i]
        self.digest[self.instruction_address] = self.hash_op(self.digest[self.instruction_address], input_value)
        self.fold_register = self.hash_op(self.fold_register, self.digest[self.instruction_address])
        for i in input_registers: self.state_registers[i] = self.hash_op(self.state_registers[i], self.digest[self.instruction_address])
        
        return self


    def __call__(self, steps: int) -> int:
        for _ in range(steps):
            self.execute()
        return self.fold_register


