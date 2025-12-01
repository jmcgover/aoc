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
    start_val: int,
    num_vals: int,
) -> int:
    """Count the number of times the dial points at or crosses 0."""
    cur_val: int = start_val

    crossings: int = 0
    landings: int = 0 if cur_val != 0 else 1
    for line in input:
        # Parse the dial rotation operation
        distance: int = int(line[1:])
        direction = Direction(line[0])

        # Rotate the dial
        nominal: int
        match direction:
            case Direction.left:
                nominal = cur_val - distance
            case Direction.right:
                nominal = cur_val + distance
            case _:
                assert_never(direction)
        q, r = divmod(nominal, num_vals)
        pointed: int = abs(q)
        landed: int = r
        print(f"{cur_val} {direction!s}{distance} points at {landed}", file=sys.stderr)

        # Lands on 0
        if landed == 0:
            print(f"Points at 0", file=sys.stderr)
            landings += 1

        # Crosses 0
        if pointed:
            print(f"Pointed at 0 {pointed}x on this operation", file=sys.stderr)
            if cur_val != 0 and landed != 0:
                crossings += pointed
            else:
                print("Ignoring 1 crossing", file=sys.stderr)
                crossings += pointed - 1

        # Commit the landed value
        cur_val = r
        assert cur_val >= 0
        assert cur_val < num_vals
        print(f"{crossings=}", file=sys.stderr)
        print(f"{landings=}", file=sys.stderr)
        print(file=sys.stderr)

    return crossings + landings


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
        password: int = method_0x434C49434B(
            input=input,
            start_val=50,
            num_vals=100,
        )
        print(password)
    return 0


if __name__ == "__main__":
    sys.exit(main())
