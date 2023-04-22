import unittest
from main import Bank
from dataclasses import is_dataclass

class TestBank(unittest.TestCase):

    def setUp(self) -> None:
        self.user = Bank("00002", "00002-02", 60.0)
        
    def test_constructor(self):
        self.assertEqual(self.user.branch, "00002")
        self.assertEqual(self.user.account, "00002-02")
        self.assertEqual(self.user.wallet, 60.0)

    def test_if_it_is_a_dataclass(self):
        self.assertEqual(is_dataclass(self.user), True)

    def test_deposit(self):
        self.user.do_deposit(50.0)
        self.assertEqual(self.user.wallet, 110.0)

    def test_withdraw(self):
        self.user.do_withdraw(20.0)
        self.assertEqual(self.user.wallet, 40.0)

    def test_deposit_a_negative_amount(self):
        with self.assertRaises(Exception) as e:
            self.user.do_deposit(-10.0)
        self.assertEqual(e.exception.args[0], "Unable to deposit. Do deposit a positive amount, please.")

    def test_withdraw_greater_than_balance(self):
        with self.assertRaises(Exception) as e:
            self.user.do_withdraw(100.0)
        self.assertEqual(e.exception.args[0], "Unable to withdraw money. Check your statement, please.")

if __name__ == "__main__":
    unittest.main()