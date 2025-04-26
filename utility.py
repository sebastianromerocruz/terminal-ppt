from typing import TextIO
from enum import Enum
from Slide import Slide
from os import system, name


class Status(Enum):
    ERROR = 0
    SUCCESS = 1


def clear_screen() -> None:
    system('cls' if name == 'nt' else 'clear')


def get_file(filepath: str) -> tuple:
    try:
        file_obj: TextIO = open(file=filepath)
    except FileNotFoundError:
        print(f"ERROR: Lines file '{filepath}' could not be opened.")
        return None, Status.ERROR
    
    return file_obj, Status.SUCCESS


def get_slides(filepath: str) -> list[Slide]:
    file_obj, success = get_file(filepath=filepath)
    
    if not success:
        return None
    
    slides: list[Slide] = []
    
    slide_text: str = ''
    
    for line in file_obj:
        if line.strip() != '-':
            slide_text += line
            continue
        
        try:
            slides.append(Slide(text=slide_text))
            slide_text: str = ''
        except TypeError:
            continue
    
    return slides


if __name__ == "__main__":
    print(get_file(filepath=''))
