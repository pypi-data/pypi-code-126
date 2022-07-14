#!/usr/bin/env python3


def load_lines(path: str):
    with open(path) as f:
        return f.read().splitlines()


def compute_statistics(a: list, b: list):
    a_set = set(a)
    b_set = set(b)
    set_stats = {
        "{A}": len(a_set),
        "A": len(a),
        "{B}": len(b_set),
        "B": len(b),
        "|A|-|B|": len(a) - len(b),
        "A ∖ B": len(a_set - b_set),
        "B ∖ A": len(b_set - a_set),
        "A ∪ B": len(a_set | b_set),
        "A ∩ B": len(a_set & b_set),
    }
    return set_stats


def print_stats(stats: dict):
    r = "\n".join([f"{k:>8}  {v:,}" for k, v in stats.items()])
    print(r)


def statistics(path_a: str, path_b: str):
    a = load_lines(path_a)
    b = load_lines(path_b)
    stats = compute_statistics(a, b)
    print_stats(stats)


def run():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("path_a", type=str)
    parser.add_argument("path_b", type=str)
    args = parser.parse_args()

    f = args.path_a
    t = args.path_b

    statistics(f, t)


if __name__ == "__main__":
    run()
