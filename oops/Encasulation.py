class account:
    def __init__(self,balance):
        self.__balance=balance
    
    def deposit(self,amount):
        self.__balance+=amount
    
    
    def withdraw(self,amount):
        if amount >self.__balance:
            print("insufficient balance:")
        else:
            self.__balance-=amount
    def togetbalance(self):
        return self.__balance
    
acc=account(10000)       
print("current balance of account is:",acc.togetbalance())
acc.deposit(600)
print("after withdraw current balance of account is:",acc.togetbalance())

acc.withdraw(600)
print(acc.togetbalance())
