class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement speak()")


class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."


class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. Remaining balance: {self.__balance}")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.__balance


if __name__ == "__main__":
    print("=== OOP Tutorial Demo ===")

    dog = Dog("Buddy")
    cat = Cat("Milo")

    print(dog.speak())
    print(cat.speak())

    account = BankAccount("Alice", 1000)
    account.deposit(200)
    account.withdraw(300)
    print(f"Current balance: {account.get_balance()}")
