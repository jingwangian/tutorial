from typing import Generator


def search(text: str, sub_text: str) -> Generator[int, None, None]:
    """
    Return next pos by generator 
    """

    text = text.lower()
    sub_text = sub_text.lower()
    text_len = len(text)
    sub_text_len = len(sub_text)

    if not sub_text_len:
        return

    for i in range(text_len - sub_text_len + 1):
        k = 0
        while k < sub_text_len and text[i+k] == sub_text[k]:
            k += 1
        if k == sub_text_len:
            yield i+1
