#!/usr/bin/env python3

import pytest
from bf_search import search 


@pytest.fixture
def text1():
    return 'Peter told me that Peter the pickle piper piped a pitted pickle before he petered out. Phew!'


@pytest.fixture
def text2():
    return 'Python is a very coool tools and used in evererwhere!'

class TestSearch:

    @pytest.mark.parametrize('sub_text, expected', (
        ('Peter', [1, 20, 75]),
        ('peter', [1, 20, 75]),
        ('peTer', [1, 20, 75]),
        ('pick', [30,58]),
        ('pi', [30, 37, 43, 51, 58]),
        ('z', []),
        ('Peterz', []),
        ('Phewx', []),
    ))
    def test_search_text1(self, text1, sub_text, expected):
        for i in search(text1, sub_text):
            i = i-1
            assert text1[i:i+len(sub_text)].lower() == sub_text.lower()
        
        results = [i for i in search(text1,sub_text)]

        assert results == expected

    @pytest.mark.parametrize('sub_text, expected', (
        ('oo',[19, 20, 25]),
        ('er', [14, 44, 46, 50]),
        ('Python is a very coool tools and used in evererwhere!',[1]),
        ('Python is a very coool tools and used in evererwhere! ', []),
        ('Python i ', []),
        ('Python i', [1])
    ))
    def test_search_text2(self, text2, sub_text, expected):
        for i in search(text2, sub_text):
            i = i-1
            assert text2[i:i+len(sub_text)].lower() == sub_text.lower()

        results = [i for i in search(text2, sub_text)]

        assert results == expected
