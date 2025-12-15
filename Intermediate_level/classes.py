                                # Classes & Objects (The Blueprint And Printing)
"""
1. Difference between class and objects:
    This is the fundamental concept.
    => class: The Blueprint or template. It defines what something looks like and do. 
              It does't exist in physical world yet.
    => object: The Instance. The instance. The actual house built from the blueprint. 
                you can built 1000 houses(objects) from single blueprint(class).
"""

"""
2. Understanding __init__ (The Constructor):
    When you create an object, you need to setup its initial state. In other programming languages
    this is called constructor. In Python we use the magic magic method __init__.
    It runs automatically the moment an object is created.
"""

"""
3. The role of self:
    This is the number one source of confusion
    => The Scenario:
        You have a blueprint of a vehicle. You built two vehicles: car_1 and car_2.
    => The Problem:
        If the code says set_name("Honda Accord"). How does Python know whether to rename 
        car_1 or car_2 ? 
    => The Solution (self):
        => The self translates to: "The specific object being worked on right now."
        => When car_1 calls the method self is car_1 and 
        => When car_2 calls the method self is car_2

"""

class Vehicle:
    def set_name(self, name):
        self.name = name
 
car_1 = Vehicle() # Vehicle object 1
car_2 = Vehicle() # Vehicle object 2

car_1.set_name("Honda civic") # self is car_1
# print(car_1.name)
car_2.set_name("Land Cruser") # self is car_2
print(car_2.name)



# E-Commerce Product

class Product:
    def __init__(self, name, price , stock):
        self.name = name
        self.price = price
        self.stock = stock

    def apply_discount(self, percent):
        discount_price = self.price * (percent/100)
        discount_percent = (discount_price/self.price)*100
        self.price -= discount_price
        print(f"{discount_percent} % Discount is applied! new price for {self.name} is $ {self.price}")
    
    def sell(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            print(f"{quantity} {self.name} sold. reamining {self.stock} items")
        else:
            print(f"Error: Not enough {self.name} stock is available")

laptop = Product('Hp', 10000, 20)

mobile = Product("Oppo", 20000, 12)

laptop.apply_discount(10)
laptop.sell(0)
         

