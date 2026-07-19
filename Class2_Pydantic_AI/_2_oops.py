"""
_2_oop_classes.py

Classes, taught clean -- no Agent in sight. Class 1 only ever showed
you a class wearing an "Agent" costume; this file is the bare pattern,
on its own, so it actually generalizes instead of feeling like
something you can only use for AI.

Run with: uv run _2_oop_classes.py
"""


class BankAccount:
    
    def __init__(self,owner:str, balance:float = 0.0):
        self.owner = owner
        self.__balance = balance
        self.history = []
        
    def deposit(self,amount: float) -> None:
        
        self.__balance += amount
        self.history.append(("deposited amount", amount))
        
    def withdraw(self,amount:float) -> None:
        
        if amount > self.__balance:
            print(f"Insufficient funds : Withdraw amount {amount} exceeds balance {self.__balance}") 
        else:
            self.__balance -= amount
            self.history.append(("withdrawn amount", amount))
            
    def show_history(self) ->None:
        for action, amount in self.history:
            print(f"{action}: {amount}")
            
            
            
acc_1 = BankAccount("Alice", 1000.0)
acc_2 = BankAccount("Bob", 500.0)

acc_1.deposit(200.0)
acc_1.withdraw(1500.0)
print(f"{acc_1.owner}'s balance: {acc_1._BankAccount__balance}")
acc_1.show_history()


# Equivalent dataclass version
from dataclasses import dataclass, field


@dataclass
class BankAccountDataClass:
    owner: str
    balance: float = 0.0
    history: list[tuple[str, float]] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.__balance = self.balance

    def deposit(self, amount: float) -> None:
        self.__balance += amount
        self.history.append(("deposited amount", amount))

    def withdraw(self, amount: float) -> None:
        if amount > self.__balance:
            print(f"Insufficient funds : Withdraw amount {amount} exceeds balance {self.__balance}")
        else:
            self.__balance -= amount
            self.history.append(("withdrawn amount", amount))

    def show_history(self) -> None:
        for action, amount in self.history:
            print(f"{action}: {amount}")


acc_3 = BankAccountDataClass("Charlie", 800.0)
acc_3.deposit(100.0)
acc_3.withdraw(900.0)
print(f"{acc_3.owner}'s balance: {acc_3._BankAccountDataClass__balance}")
acc_3.show_history()
