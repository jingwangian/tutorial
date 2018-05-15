#!/usr/bin/env python3

import pytest


class TestNumbers:
    def test_init_float(self):
        assert 1 == 1.0

    def test_init_str(self):
        assert 1 == "1"


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5
