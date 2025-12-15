                # Arguments (*agrs, **kwargs)
'''
Sometimes you don't know how many inputs your functions will receive. 
Maybe you are summing 2 numbers, maybe 20 numbers. Python handles this with Packing. 
'''

"""
1. Default Parameters:
    This is your backup plan, If the user does't provide the value, the function user the default.
Warning!:
    Never use a mutable object  (like a list[] or dictionary{}) as a default argument.  It persists
    across function calls.  Use None instead.
"""
# The safe way to do defaults
def connect_to_db(host="localhost", port=5432):
    print(f"Connecting to {host} on port {port} ...")
connect_to_db() # Uses defaults: localhost, 5432
connect_to_db("192.168.1.1") # Uses provided host, default port



"""
2. *args(Positional Arguments):
    The asterisk * packs any number of extra positional arguments into a Tuple.
"""
# I want a function that sums any amount of numbers.
def super_sum(*args):
    print(type(args))
    return sum(args)

print(super_sum(23,34))
print(super_sum(1,2,3,4,5,6))



"""
3. **kwargs (Keyword Arguments):
    The double sterisk ** packs-key value pair into a Dictionary. This is Standard in Data Science
    libraries (like plotting configurations)

"""

def create_profile(name, **kwargs):
    print(f"User: {name}")
    for key, val in kwargs.items():
        print(f" - {key} --> {val}")

create_profile( 'naseem' ,Deapartment = "AI", Gender = "Male" )

