from dataclasses import dataclass

@dataclass
class Bank:
    branch: str
    account: str
    wallet: float

    def do_withdraw(self, amount:float) -> None:
        if amount > self.wallet:
            raise Exception("Unable to withdraw money. Check your statement, please.")
        self.wallet -= amount

    def do_deposit(self, amount:float) -> None:
        if amount <= 0:
            raise Exception("Unable to deposit. Do deposit a positive amount, please.")
        self.wallet += amount
