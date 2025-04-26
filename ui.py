from time import sleep
from sys import stdout
from typing import Iterable
from Slide import Slide


SLEEP_TIMER: float = 0.01


def typewriter_print(slide: Slide) -> None:
    if not slide:
        raise ValueError("Lines iterable is null.")
    if not isinstance(slide, Slide):
        raise ValueError("Lines iterable is not a Slide object")
    
    for character in slide:        # for each character in each line
        print(character, end='')  # print a single character, and keep the cursor there.
        stdout.flush()            # flush the buffer
        sleep(SLEEP_TIMER)        # wait a little to make the effect look good.
    
    print()


if __name__ == "__main__":
    lines: list = ["You have woken up in a mysterious maze\n",
            "The building has 5 levels\n",
            "Scans show that the floors increase in size as you go down\n"]
    
    typewriter_print(slide=lines)
