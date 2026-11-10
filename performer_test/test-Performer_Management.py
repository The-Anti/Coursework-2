import pytest
from Performer_Management import get_band_name

def test_good_name():
    assert get_band_name("Slipknot") == "Hello Slipknot."

def test_short_name():
    assert get_band_name("D") ==  "Please input a proper band name."

def test_long_name():
    assert get_band_name("qwertyuiopasdfghjklzxcvbnm") == "Please input a proper band name."