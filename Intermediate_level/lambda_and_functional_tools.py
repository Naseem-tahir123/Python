                    # Lambda And Functional Tools
"""
The "Disposible" Funcition
1. lambda funcition:
    A lambda is a small, anonymous function defined in one line.
    => Syntax: lambda arguments : expression
    => Rule: Use them for simple logic that you only need once. it it's  complex, write a read def.

"""

# Standard funcition
def add(a,b):
    return a + b

# Equivalent lambda
add1 = lambda a,b: a+b

print(add1(2,2))

"""
2. map(), filter() and sorted().
    These are power tools that often use lambdas.
    => map(func,list): Apply function to every item
    => filter(func, list): Keep items where the functions returns True.

"""

numbers = [1,2,3,4,5]
print(f"The numbers list is: {numbers}")

squares = map(lambda x: x**2, numbers)
print(f"Squares of the numbers list: {list(squares)}")


even_nums = filter(lambda x: x%2 == 0, numbers )
print(f"Even number from numbers list are: {list(even_nums)}")

odd_nums = filter(lambda x : x%2 != 0 , numbers)
print(f'Odd numbers from numbers list are: {list(odd_nums)}')


"""
3. sorted() with keys:
    This is the most practical use case. How do you sort a list of dictionaries? 
    You tell Python which key to look at using a lambda.

"""
users =[
    {'name':'Naseem', 'age' : 25},
    {'name':'Nadeem', 'age': 23},
    {'name':'Waseem', 'age':20}
]

print(users)

sorted_users = sorted(users, key=lambda x: x['age'], reverse=False)
print(sorted_users)
