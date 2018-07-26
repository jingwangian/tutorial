from typing import Generator

def search(text: str, sub_text: str) -> Generator[int, None, None]:
    """
    Return next pos by generator 
    """

    text = text.lower()
    sub_text = sub_text.lower()

    pos = 0
    while True:
        pos = text.find(sub_text,pos)
        if pos != -1:
            pos += 1
            yield pos
        else:
            break
