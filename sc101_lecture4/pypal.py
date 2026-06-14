
WITHDRAW_LIMIT = 1000
MONEY = 0


class Pypal:
    def __init__(self, name, money=MONEY, limit=WITHDRAW_LIMIT):
        self._name = name
        self._balance = money
        self._limit = limit

    def withdraw(self, amount):
        if amount > self._limit:
            print("Error: Exceed Limit")
            return

        if amount > self._balance:
            print("Error: You don't have enough balance")
            return

        self._balance -= amount
        print(f"{self._name}: {self._balance}")

    # Name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # Balance
    @property
    def balance(self):
        return self._balance

    # Limit
    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self,value):
        self._limit = value
