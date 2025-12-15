                                        # Scope (The LEGB Rule) 
"""
Who has access to what?
Scope defines the visibility of "variables".
Can code inside of a functions see a variable defined outside?
Can code outside of a function see a variables defined inside?
Pyton follows the LEGB rule to look for the variables.
1. Local (inside the function)
2. Enclosing (Nested functionos - advanced)
3. Global(Top level of the file)
4. Built-in(Python keywords like print, len, list)

"""


"""
1. Local Scope (The Las Vegas Rule):
Variables created inside a function stays inside of the function. "What happens in the function
stays in the function."
"""
def my_secret_function():
    secret_code = 12345
    print(f"Inside function {secret_code}")

# print(secret_code) # This will cause an error NameError: name 'secret_code' is not defined 

"""
2. Global Scope:
Variables created at the main indentation level are Global. Everone can see them (read them).
But modifying them inside a function requires a special step.

"""

greeting = "Assalamu Alaikum" # this is a global variable

def greet(name):
    print(f"{greeting}, {name.title()}") # we can read the global variable insidet the function

def change_greeting(name):
    greeting = "Hello" # This creates a new local variable named greeting
    print(f"{greeting}, {name.title()}")

greet("Naseem") # This will use the global greeting
change_greeting("Waseem") # This will use the local greeting
print(greeting) # This will print the global greeting

"""
3. The 'global' keyword (use with caution):
If you absolutely must modify a global variable iside a function (which is generally discouraged in 
professional code), you can use the 'global' keyword.
"""

score = 0  # global variable
def increase_score():
    global score # tell python we want to use the global variable
    score += 10
increase_score()
print(score)

"""
Challenge:
1. Define a Global Variable called EXCHANGE_RATE and set it to 0.85 (Dollars to Euros). 
2. Create a function called convert_currency that takes one parameter: dollars. 
3. Docstring: Add a docstring explaining the function. 
4. Logic: inside the function, calculate euros (dollars * EXCHANGE_RATE). 
5. Return: The function must return the value (do NOT print inside). 
6. Main Execution: Outside the function, ask the user for an amount in dollars, call your function, and 
print: "That is X Euros." 
"""
EXCHANGE_RATE = 0.85
def convert_currency(dollars):
    """
    This function coverts dollars to euros using the global EXCHANGE_RATE.
    Input: amount in dollars in float
    Output: equivalent amount in euros in float
    """
    euros = dollars * EXCHANGE_RATE
    return euros
# Main Execution

dollars = float(input("Enter amount in Dollars:"))

euros = convert_currency(dollars)
print(f"That is {euros} Euros.")
