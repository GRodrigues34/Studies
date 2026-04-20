class Main:
    pass

print("main test")

from Client import Client
from Account import Account


c1 = Client("Jão", "4002-8922")
acc = Account(c1.name,1,10000)

print(c1)
print(c1.name,"   ", c1.phone_number)
print(acc.user,"  ", acc.number,"  ", acc.balance)
