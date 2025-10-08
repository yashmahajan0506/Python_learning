from abc import ABC ,abstractmethod

class payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class creditcardpayment(payment):
    def pay(self, amount):
        print(f"Paid {amount} using credit card")

class upipayment(payment):
     def pay(self, amount):
        print(f"Paid {amount} using Upi")
        
c1=creditcardpayment()
c1.pay(500)

u1=upipayment()

c1.pay(400)