class BankAccount:
     def __init__(self):
         self._current=0
     def withdraw(self,amount):
         if(self._current<amount):
             print("You can't Withdraw..Balance insufficient")
         else:
             print("Withdrawn amount",amount)
             return self._current-amount
     def deposit(self,amount):
         self._current=self._current+amount
         print("Amount deposited",amount)
             

sam=BankAccount()
sam.withdraw(100)
sam.deposit(100)
rio=BankAccount()
p=rio.deposit(200)
k=sam.withdraw(20)
k1=rio.withdraw(30)

print("Balance amount of sam",k)
print("Balance amount of rio",k1)
