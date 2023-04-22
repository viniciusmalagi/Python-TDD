from main import Bank
from dataclasses import is_dataclass
import pytest

@pytest.fixture
def user():
    return Bank("00002", "00002-02", 60.0)

def test_constructor(user):
    assert user.branch == "00002"
    assert user.account == "00002-02"
    assert user.wallet == 60.0

def test_if_it_is_a_dataclass(user):
    assert is_dataclass(user) == True

def test_deposit(user):
    user.do_deposit(50.0)
    assert user.wallet == 110.0

def test_withdraw(user):
    user.do_withdraw(20.0)
    assert user.wallet == 40.0

def test_deposit_a_negative_amount(user):
    with pytest.raises(Exception) as e:
        user.do_deposit(-10.0)
    assert e.value.args[0] == "Unable to deposit. Do deposit a positive amount, please."

def test_withdraw_greater_than_balance(user):
    with pytest.raises(Exception) as e:
        user.do_withdraw(100.0)
    assert e.value.args[0] == "Unable to withdraw money. Check your statement, please."