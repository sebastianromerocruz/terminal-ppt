from ui import typewriter_print
from utility import get_slides, clear_screen
from Slide import Slide


TXT_PATH: str = "assets/lines.txt"


if __name__ == "__main__":
    slides: list[Slide] = get_slides(filepath=TXT_PATH)
        
    if not slides:
        pass
    
    clear_screen()
    
    for slide in slides:
        typewriter_print(slide=slide)
        input('[Press Enter To Continue]')
        clear_screen()
