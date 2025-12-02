#!/usr/bin/env python3.14

import sys
from typing import TextIO


def is_bad_id(product_id: str) -> bool:
    """Return whether the ID is made only of some sequence of digits repeated twice."""
    if len(product_id) % 2 != 0:  # odd-length strings
        return False
    return product_id[: len(product_id) // 2] == product_id[len(product_id) // 2 :]


def find_bad_ids(start: int, end: int) -> list[int]:
    return [_id for _id in range(start, end + 1) if is_bad_id(product_id=str(_id))]


def sum_bad_ids(
    input: TextIO,
) -> int:
    bad_ids: list[int] = []
    for line in input:
        # Parse Line
        _line: str = line.strip()
        start: int
        end: int
        start, end = tuple([int(tok) for tok in _line.split("-")])
        # Track Bad IDs
        bad_ids.extend(find_bad_ids(start=start, end=end))
    # Sum Bad IDs
    return sum(bad_ids)


def main() -> int:
    with sys.stdin as input:
        print(sum_bad_ids(input=input))
    return 0


if __name__ == "__main__":
    sys.exit(main())
