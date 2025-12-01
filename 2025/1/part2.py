#!/usr/bin/env python3.14

import sys
from enum import StrEnum
from typing import TextIO, assert_never


class Direction(StrEnum):
    """Valid directions to turn a dial."""

    left = "L"
    right = "R"


def method_0x434C49434B(
    input: TextIO,
    val: int,
    start_val: int,
    num_vals: int,
) -> int:
    """Count the number of times the dial lands on a value after any rotation."""
    cur_val: int = start_val
    pointings: int = 0 if cur_val != val else 1
    for line in input:
        distance: int = int(line[1:])
        direction = Direction(line[0])
        match direction:
            case Direction.left:
                while distance > 0:
                    cur_val = (cur_val - 1) % num_vals
                    if cur_val == 0:
                        pointings += 1
                    distance -= 1
            case Direction.right:
                while distance > 0:
                    cur_val = (cur_val + 1) % num_vals
                    if cur_val == 0:
                        pointings += 1
                    distance -= 1
            case _:
                assert_never(direction)
        assert cur_val >= 0
        assert cur_val < num_vals
    return pointings


def main() -> int:
    with sys.stdin as input:
        password: int = method_0x434C49434B(
            input=input,
            val=0,
            start_val=50,
            num_vals=100,
        )
        print(password)
    return 0


if __name__ == "__main__":
    sys.exit(main())
