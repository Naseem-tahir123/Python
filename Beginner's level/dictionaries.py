                # Dictionaries (The Map. Key-Value Pairs. Fast Lookups)
"""
Dictionaries are like real dictionary: you lookup a word (key) to get its meaning (value).
and this lookup is very fast.
Dictionaries are the backbone of JSON and API data. They Map a unique Key to a Value.
"""

"""
1. Structure And Accessing Data:
Keys must be immutable (strings, numbers, tuples). Values can be anything.

"""
# Example Dictionary
student_details = {
    "id": 101,
    "name": "Alice",
    "courses": ["Math", "Science"],
    "is_active": True
}
# Accessing Values
print(student_details['name'])

# The safer way to access values: .get() method
# [] crashes the program if the key does not exist.
# .get() returns None (or a default value you provide) if the key is missing.
print(student_details.get('age')) # None no crash
print(student_details.get('age', 'Not Specified'))
# print(student_details['age']) # This would raise a KeyError: 'age'

"""
2. Essential Methods(keys, values, items, update, pop, popitem):
- keys(): Returns a view object of all keys in the dictionary.
- values(): Returns a view object of all values in the dictionary.
- items(): Returns a view object of key-value pairs (tuples) in the dictionary.
- update(other_dict): Updates the dictionary with key-value pairs from another dictionary.
- pop(key): Removes the specified key and returns its value.
- popitem(): Removes and returns an arbitrary key-value pair as a tuple.

"""

# Loop through keys
for k in student_details.keys():
    print(f"Key: {k}")
# Loop through values
for val in student_details.values():
    print(f"Value: {val}")

# Loop through both items -- Most common
for k, v in student_details.items():
    print(f"{k} => {v}")

# Update dictionary
student_details.update({'age':20 , 'is_active':False})
print(student_details)

# Pop a key
age = student_details.pop('age')
print(f"Popped Age: {age}")
print(student_details)


# Pop an arbitrary item
key, value = student_details.popitem()
print(f"Popped Item: {key} => {value}")
print(student_details)

student_details.pop('id') # Just pop without assignment
print(student_details)




"""
Challenge:
1. Create a List of items: shop_items = ["apple", "banana", "apple", "orange", "banana", "banana"]. 
2. Use a Set to find out how many unique products you have. Print that number. 
3. Create an empty Dictionary called inventory. 
4. Loop through shop_items. 
    -->If the item is not in inventory, add it with a value of 1. 
    -->If the item is in inventory, increment its value by 1. 
5. Output: Print the final dictionary (It should look like {'apple': 2, 'banana': 3, 'orange': 1}). 
"""
shop_items = ["apple", "banana", "apple", "orange", "banana", "banana"]
unique_items = set(shop_items)
print(shop_items)
print(f"Number of unique items: {len(unique_items)}")
inventory = {}
for item in shop_items:
    if item not in inventory:
        inventory[item] = 1
    else:
        inventory[item] += 1
print(f"Final Inventory: {inventory}")
 