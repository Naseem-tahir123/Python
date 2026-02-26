                        # Decorators (The "Wrapper". Changing behavior without chaning code)

"""
This is an advanced concept. A Decorator is a function that takes another function, adds some 
functionality to it, and returns it.
Think of it like a phone case. The phone (your function) works exactly the same, but now it has 
extra protection (the decorator).
"""

"""
1. The Concept (Higher-Order Function)
    In python, functions are objects. You can pass them around like variables.
"""
def my_decorator(func):
    # The wrapper is the sandwich bread around the meat (func)
    def wrapper(*args):
        print("--- something happens before the function called")
        res = func(args)
        print("--- something happens after the function called.")
        return res

    return wrapper


@my_decorator
def squ(x):
    l1 = []
    for i in x:
        l1.append(i**2)
    print(l1)
    return l1


lst = [1,2,3,4,5]
print(lst)
print(squ(*lst))



import time 

def timer_decorator(process):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = process(*args, **kwargs)
        end_time = time.time()
        total_time_taken = end_time - start_time
        print(f"The process take {total_time_taken:.4f} seconds to complete the process")
        return result   
    return wrapper


@timer_decorator
def process():
    total = sum(range(100000))
    return total


process()



"""
Challenge: "The Smart Logger":

    Combine everything you just learned. 
1. Create a decorator called @logger. 
o It should print: "Function [name] called with args: [args]" before running the function. 
2. Create a function called process_data that uses *args. 
o It should take any number of integers. 
o Apply the @logger decorator to it. 
3. Inside process_data: 
o Use filter and a lambda to keep only numbers greater than 10. 
o Return the filtered list. 
4. Call process_data(5, 12, 8, 20) and verify the output. 
"""
 
def logger(func):
    def wrapper(*args):
        print(f"Function {func.__name__} called with args: {args}")
        res = func(*args)
        return res
    return wrapper

@logger
def process_data(*args: int):
    return list(filter(lambda x : x> 10, args))

s = process_data(1,20,3,40)
print(s)
 
  
 
    

 

 


 