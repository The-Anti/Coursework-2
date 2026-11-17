import pytest
from app.Performer_Management import get_performer_amount

def test_get_performer_amount_zero():
    assert get_performer_amount(0) == "invalid"
    
def test_get_performer_amount_erroneous():
    assert get_performer_amount("No") == "invalid"
    
def test_get_performer_amount_valid():
    assert get_performer_amount(5) == "valid"