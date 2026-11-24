from app.Performer_Management import get_performers, contact_details
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
    
    
    
    
def test_contact_details():
    Performer_inputs = [
        "Alex", "Guitar",
        "John", "Bass",
        "stop"
    ]
    
    Contact_inputs = [
        "44773812852",
        "44783017693"
    ]
    
    with patch("builtins.input", side_effect = Performer_inputs):
        performer_results = get_performers()
        
    with patch("builtins.input", side_effect = Contact_inputs):
        contact_results = contact_details()
        
    assert contact_results == {
        "Alex": "44773812852",
        "John": "44783017693"
    }
    
def test_contact_details_dupe_ignored():
    performerInputs = [
        "Alex", "Bass",
        "John", "Drums",
        "Jimmy", "Drums", "n",
        "stop"
    ]
    
    contactInputs = [
        "07783292800",
        "07798217462"
    ]
    
    with patch("builtins.input", side_effect = performerInputs):
        performerResults = get_performers()
    
    with patch("builtins.input", side_effect = contactInputs):
        contactResults = contact_details()
        
    assert contactResults == {
        "Alex": "07783292800",
        "John": "07798217462"
    }