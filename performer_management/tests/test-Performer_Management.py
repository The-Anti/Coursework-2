from app.Performer_Management import get_performers
from unittest.mock import patch
import pytest

# TESTS FOR PERFORMERS UP TO LINE 86
# TEST 1: Check whether a performer is added correctly
def test_add_performer():
    inputs = ["Joshua", "Lead Guitar", "stop"]

    with patch("builtins.input", side_effect=inputs):
        result = get_performers()

    assert result == {"Joshua": "Lead Guitar"}


# TEST 2: Check whether multiple performers can be added
def test_multiple_performers():
    inputs = [
        "Joshua", "Lead Guitar",
        "Macauley", "Bass",
        "stop"
    ]

    with patch("builtins.input", side_effect=inputs):
        result = get_performers()

    assert result == {
        "Joshua": "Lead Guitar",
        "Macauley": "Bass"
    }


# TEST 3: Check whether duplicate instruments are rejected
def test_reject_duplicate_instrument():
    inputs = [
        "Joshua", "Lead Guitar",
        "Macauley", "Lead Guitar", "n",
        "stop"
    ]

    with patch("builtins.input", side_effect=inputs):
        result = get_performers()

    assert result == {"Joshua": "Lead Guitar"}


# TEST 4: Check whether duplicate instruments are accepted
def test_accept_duplicate_instrument():
    inputs = [
        "Joshua", "Lead Guitar",
        "Macauley", "Lead Guitar", "y",
        "stop"
    ]

    with patch("builtins.input", side_effect=inputs):
        result = get_performers()

    assert result == {
        "Joshua": "Lead Guitar",
        "Macauley": "Lead Guitar"
    }


# TEST 5: Check whether stop terminates the program
def test_stop_program():
    inputs = ["stop"]

    with patch("builtins.input", side_effect=inputs):
        result = get_performers()

    assert result == {}


# TEST 6: Check whether duplicate detection is case-insensitive
def test_duplicate_accept_uppercase():
    inputs = [
        "Joshua", "Lead Guitar",
        "Macauley", "Lead Guitar", "Y",
        "stop"
    ]

    with patch("builtins.input", side_effect=inputs):
        result = get_performers()

    assert len(result) == 2
    assert result["Macauley"] == "Lead Guitar"