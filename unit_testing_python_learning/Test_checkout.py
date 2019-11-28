#TODO
# x can create instance of checkout class
# x can add item price
# x can add an item
# x can calculate the current total
# x can add multiple items and get correct total
# x can add discount rules
# x can apply discount rules to the total
# x Exception is thrown for item added without price

import pytest
from Checkout import Checkout

@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.addItemPrice("a", 1)
    checkout.addItemPrice("b", 2)
    return checkout

def test_CanCalculateTotal(checkout):
    checkout.addItem("a")
    assert checkout.calculateTotal() == 1

def test_GetCorrectTotalWithMultipleItems(checkout):
    checkout.addItem('a')
    checkout.addItem('b')
    assert checkout.calculateTotal() == 3

def test_canAddDicountRule(checkout):
    checkout.addDiscount('a',3,2)

def test_canApplyDiscountRule(checkout):
    checkout.addDiscount('a',3,2)
    checkout.addItem('a')
    checkout.addItem('a')
    checkout.addItem('a')
    assert checkout.calculateTotal() == 2

def test_ExceptionWithBadItem(checkout):
    with pytest.raises(Exception):
        checkout.addItem('c')
