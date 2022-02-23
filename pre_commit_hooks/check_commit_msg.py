#!/usr/bin/env python
import sys
from enum import Enum

# https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
class bcolors(str, Enum):
    OK = "\033[92m"
    INFO = "\033[94m"
    WARNING = "\033[93m"
    ERROR = "\033[91m"
    BOLD = "\033[1m"
    ENDC = "\033[0m"


class Level(str, Enum):
    OK = "OK"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


def print_with_color(message: str, level: Level):
    print(
        bcolors[level]
        + bcolors.BOLD
        + f"{level}: [Policy] "
        + message
        + bcolors.ENDC
    )


def check_commit_msg_pattern():
    # The argument passed to the "commit-msg" hook is the path to a
    # temporary file that contains the commit message written by the
    # developer.
    msg_temp_file = sys.argv[1]

    with open(msg_temp_file, "r") as f_msg:
        lines = f_msg.readlines()

    # Remove the comment lines in the commit message.
    lines = [l for l in lines if not l.strip().startswith("#")]

    has_warning = False
    if len(lines) < 3:
        message = "There should at least three lines in your commit message."
        print_with_color(message, Level.ERROR)
        exit()

    if len(lines[0]) > 50:
        has_warning = True
        message = (
            "There should be less then 50 characters in the commit title."
        )

        print_with_color(message, Level.WARNING)

    if lines[1].strip() != "":
        has_warning = True
        message = (
            "There should be an empty line between the commit title and body."
        )
        print_with_color(message, Level.WARNING)

    for line in lines[2:]:
        if len(line) > 72:
            has_warning = True
            message = "The commit body should wrap at 72 characters."
            print_with_color(message, Level.WARNING)

    if not has_warning:
        message = "The commit message has the required pattern."
        print_with_color(message, Level.OK)


if __name__ == "__main__":
    check_commit_msg_pattern()
