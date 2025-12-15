                            # Inheritance (The DNA Of Code. Don't repeat yourself DRY)
'''
Inheritance allows a new class (Child) to adopt all attributes and methods of 
existing class(Parent). We can then add specific features to the child class

    Parent (Base Class ): The generic version (e.g., vehicle).
    Child (Derived Class ): The specific one (e.g., car, truck)

=> super():
    Sometimes the Child need to do everything the Parent does, plus a little more. Super allows
    the child to call all the parent's method without rewriting the code.

=> Method Overriding:
    If a child class defines a method with the same name as the Parent, the Child's version 
    take's precedence. This is called overriding.
'''

# Parent Class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def work(self):
        return f"{self.name} is working generally"


#  Child class one   
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        # use super() to let handle Parent the standard stuff.
        super().__init__(name, salary)
        self.programming_language = programming_language

    # Method Overriding: Changing what "work" means for a dev
    def work(self):
        return f"{self.name} is coding in {self.programming_language}"

# Child class two    
class Manager(Employee):
    def work(self):
        return f"{self.name} is attending meetings."
    

dev = Developer("Naseem", 90000, 'Python')
mgr = Manager("Hanzala", 90000)

print(dev.work())
print(mgr.work())




                        # Multiple Inheritance

'''
Python allows a Class to inherit from more than one parent. This is powerful but dangerous
(It can lead to complexity).

'''

class Camera:
    def take_photo(self):
        print("Click! photo taken.")

class Phone:
    def call(self):
        print("Calling...")

class SmartPhone(Camera,Phone):
    pass

iphone = SmartPhone()
iphone.take_photo()
iphone.call()