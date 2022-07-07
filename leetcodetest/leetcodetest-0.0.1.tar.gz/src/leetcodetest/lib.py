from inspect import getmembers, ismethod
from typing import Any
import tracemalloc
import time

ENDC = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = '\033[92m'
ORANGE = "\033[93m"

class LeetcodeTester:
    def test(Solution: Any, givenInput: Any, expectedOutput: Any):
        solution = Solution()
        members = [(name, method) for name, method in getmembers(solution) if not name.startswith("_") and ismethod(method)]
        assert len(members) > 0, f"{RED}Could not find any method in your provided Solution class. Did you pass the right object?"
        assert len(members) == 1, f"{RED}Found more than one potential method, if you create additional methods please prefix them with '_'.\n{ORANGE}Methods found: {[name for name, _method in members]}"

        for name, method in members:
            print(f"Calling {name}.")
            # Benchmarking
            tracemalloc.start()
            memory_start = tracemalloc.take_snapshot()
            memory_start.statistics("lineno")
            runtime_start = time.perf_counter()

            # Run solution
            givenOutput = method(givenInput)

            # Stop benchmarking
            runtime_end = time.perf_counter()
            memory_end = tracemalloc.take_snapshot()
            tracemalloc.stop()

            runtime_difference = runtime_end - runtime_start
            memory_difference = memory_end.compare_to(memory_start, "lineno")
            memory_stats = memory_difference.pop()

            # Display results
            print(f"{BOLD}Input{ENDC}: {type(givenInput).__name__} = {givenInput}")
            print(f"{BOLD}Output{ENDC}: {type(givenOutput).__name__} = {givenOutput}")
            print(f"{BOLD}Correct Output{ENDC}: {type(expectedOutput).__name__} = {expectedOutput}")
            print("")
            print(f"{BOLD}Runtime{ENDC}: {runtime_difference:0.4f}s")
            print(f"{BOLD}Memory{ENDC}: {memory_stats.size}B")
            if givenOutput == expectedOutput:
                print(f"{BOLD}Result{ENDC}: {GREEN}Success")
            else:
                print(f"{BOLD}Result{ENDC}: {RED}Failure")