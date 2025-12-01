#!/usr/bin/env python3.14

import sys
from enum import StrEnum
from typing import TextIO, assert_never


class Direction(StrEnum):
    """Valid directions to turn a dial."""

    left = "L"
    right = "R"


def count_landings(
    input: TextIO,
    val: int,
    start_val: int,
    num_vals: int,
) -> int:
    """Count the number of times the dial lands on a value after any rotation."""
    cur_val: int = start_val
    landings: int = 0 if cur_val != val else 1
    for line in input:
        distance: int = int(line[1:])
        direction = Direction(line[0])
        match direction:
            case Direction.left:
                cur_val = (cur_val - distance) % num_vals
            case Direction.right:
                cur_val = (cur_val + distance) % num_vals
            case _:
                assert_never(direction)
        assert cur_val >= 0
        assert cur_val < num_vals
        if cur_val == val:
            landings += 1
    return landings


def main() -> int:
    with sys.stdin as input:
        password: int = count_landings(
            input=input,
            val=0,
            start_val=50,
            num_vals=100,
        )
        print(password)
    return 0


if __name__ == "__main__":
    sys.exit(main())
