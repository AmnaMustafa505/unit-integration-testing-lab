import pytest
from bank_app import transfer, calculate_interest

def test_transfer_valid():
    b1, b2 = transfer(5000, 2000, 1000)
    assert b1 == 4000
    assert b2 == 3000

def test_transfer_insufficient():
    with pytest.raises(ValueError):
        transfer(500, 1000, 2000)

def test_transfer_and_interest():
    b1, b2 = transfer(5000, 2000, 1000)
    updated_b2 = calculate_interest(b2, 10, 1)
    assert round(updated_b2, 2) == 3300.00

def test_transfer_invalid_amount():
    with pytest.raises(ValueError):
        transfer(5000, 2000, -500)
