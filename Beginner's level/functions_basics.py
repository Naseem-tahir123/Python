# Functions Basics (The Blueprint. Input -> process -> output)
"""
1. Defining Funcitions (def) and parameters:
To create a function we use a keyword def. Think of a function as a contract:
 --> Name: What is it called?
 --> Parameters: What does it need to do its job? (input)
 --> Body: What does it actually do? (process)
"""

def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}")

# 'def' tells python we are defining a function
# 'greet_user is the name of a function
# 'username' is a parameter (input) the function need to do its job.

# ****************** Using the function (calling it) ******************
greet_user('naseem tahir')
greet_user('Waseem tahir')

# Why is this better?
# If we want to change the greeting to 'Assalamu Alaikum', we only need to change it in one place

"""
2. The return Value (The most misunderstood concept in programming)
Warning:
Beginners often confuse print() with return.
    - print just puts the text on the screen. The computer forgets about the text immediately after.
    - return sends a value back to the program so you can store it and use it later, do math with it 
    or save it a database.
Rule of thumb:
    - Prefessional functions usually return data; they rarely print it.
"""
# Bad funciton example
def add_numbers(a,b): # It prints but gives nothing back
    print(a + b)
result = add_numbers(3,4)
# print(result)  # This will print 'None' because the function does not return anything


def add_nums(a,b): # It returns the data
    sum = a + b
    return sum

# now we can use the reuslt
total = add_nums(3,4)
final_price = total * 1.07  # we can do math with it
print(f"Final Calculation: {final_price}")


"""
3. Docstrings (Documentation Strings):
You might wirte a function today, but will you remeber what it does 4 months from now? 
A Docstring is a special comment format right under the def line that describes the function.

"""
def calculate_area(radius):
    """
    Calculate the area of a circle given its radius.
    parameters: 
    radius (float): The radius of the circle.
    Returns:
    float: The calculated area of the circle.
    """
    pi = 3.14159
    area  = pi * (radius **2)
    return area