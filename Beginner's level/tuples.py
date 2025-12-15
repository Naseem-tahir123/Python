                # Tuples (The vault, immutable, faster, safe)
"""
Tuples looks like lists but use parentheses () instead of square brackets []. 
The key difference?
---> You cannot change them after creation.
---> They are sealed.
This immutability makes tuples faster and safer to use in certian situations.
For example, if you have a collection of values that should not change throughout the program,
    
"""

"""
1. Immutability & Why we use it:
Use tuples for data that should never change during program execution. 
For example, GPS coordinates, birth dates, Database configurations.
"""

# Example 1. A tuple of coordinates [latitude, longitude]
coordinates = (40.7128, -74.0060)  # New York City coordinates
# coordinates[0] = 41.0 <--- This will raise a TypeError 'tuple' object does not support item assignment

"""
2. Unpacking and Swapping:
    -> Unpacking allows you to extract tuple values to variables instantly.
"""
# Example 2. Unpacking a tuple

detail = ('Naseem', 25, 'AI Engineer') # packing a tupel
name, age, profession = detail         # unpacking the tuple
print(f"Profession: {profession}")

"""
The magic swap trick:
In other languages, you need a temporary variable to swap values. (temp = a; a=b; b=temp)
In Python, you can do it in one line using tuple unpacking.

"""
a = 5
b = 10
print(f"Before Swap: a={a}, b= {b}")
a, b = b, a # Python creates a temporary tuple (b,a) and unpacks it back to a and b
print(f"After Swap: a={a}, b= {b}")