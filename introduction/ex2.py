class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def balance(self):
        return self.__balance
    
a = BankAccount(1000)
print(a.balance())