                            # Encapsulation (The security guard, controlling access)
"""
=> Restricts direct access to some of an object's component.
=> It prevents other developers (or your future self) from accidentally breaking the 
    internal state of an object.

1. Access Modifiers in Python:
    Unlike Java or C++ python does't enforce strict privace. It relies on Convention and Name Mangling.
    --> Public (name): Accessible from anywhere
    --> Protected (_name): Start with one underscore. Convention: "Please don't touch this outside
        the class or its children."
    --> Private (__name): Start with double underscore. Python hides this variable by renaming 
        it internally. Accesible only inside the class.

2. Getters and Setters (@property)
    Instead of letting users change variable directly (e.g., obj.age = -5), we use methods 
    to validate data before setting it.
"""


class BankAccount:
    def __init__(self,owner, balance):
        self.owner = owner
        self.__balance = balance
    
    @property
    def balance(self):
        return f'Total balance: {self.__balance}'
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            print("Balance should not't be nagative")
        else:
            self.__balance = value
         
    def deposit(self, amount):
        if amount < 0:
            print("Balance can't be nagative. ")
        else:
            self.__balance +=amount
        return f'Total balance: {self.__balance}'


account = BankAccount("Naseem", 20000)

# print(account.balance)
# account.balance = -10000
# print(account.balance)
account.deposit(30000)
print(account.balance)
