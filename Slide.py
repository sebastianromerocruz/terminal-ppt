from typing import Iterable


class Slide:
    def __init__(self, text: Iterable=None) -> None:
        iter(text)
        self._text: Iterable = text
        
    def __str__(self):
        return self._text
    
    def __repr__(self):
        return f"'{str(self)}'"
    
    def __iter__(self):
        for char in self._text:
            yield char