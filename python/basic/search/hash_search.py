from typing import Generator

def quick_find(s1, s2, s2_hash, s2_len, pos):
    """
    s1 : text to be searched
    s2 : sub_text
    s2_hash : hash value of s2
    s2_len : sub_text length
    pos : start pos in s1
    """
    for i in range(pos, len(s1)):
        if s1[i] == s2[0]:
            if hash(s1[i:i+s2_len]) == s2_hash and s1[i:i+s2_len]==s2: 
                return i
    return -1

def search(text: str, sub_text: str) -> Generator[int, None, None]:
    """
    Return next pos by generator 
    """

    text = text.lower()
    sub_text = sub_text.lower()
    sub_text_hash = hash(sub_text)
    sub_text_len = len(sub_text)

    pos = 0
    while True:
        pos = quick_find(text, sub_text, sub_text_hash, sub_text_len , pos)
        if pos != -1:
            pos += 1
            yield pos
        else:
            break