from pypal import Pypal


def bank():
    a1 = Pypal("Brian Lai", money=1000, limit=700)
    a1.withdraw(1000)
    a1.withdraw(700)
    a1.withdraw(700)










if __name__ == "__main__":
    bank()