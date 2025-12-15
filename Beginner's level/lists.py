                                 # Lists (The swiss army knife, mutable, ordered, flexible)
"""
1. Slicing:
    Slicing is superpower  in Python. Especially for AI/Data Science work.
    The syntax is: list_name[start:stop:step]
    - start: The index to start the slice (inclusive). Default is 0.
    - stop: The index to end the slice (exclusive). Default is the length of the list.
    - step: The step size or interval between elements. Default is 1.

"""

llms = ["GPT-3", "BERT", "T5", "RoBERTa", "XLNet", "GPT-4"]

print(llms[0]) 
print(llms[1:4]) # Slicing from index 1 to 3
print(llms[-1])  # last element
print(llms[::2]) # Every second element

"""
2. Essential Methods (append, extend, insert, remove, pop, index, count, sort, reverse):
- append(item): Adds an item to the end of the list.
- extend(iterable): Extends the list by appending elements from an iterable (like another list).
- insert(index, item): Inserts an item at a specified index.
- remove(item): Removes the first occurrence of an item from the list.
- pop(index): Removes and returns the item at the specified index (default is the last item).
- index(item): Returns the index of the first occurrence of an item.
- count(item): Returns the number of occurrences of an item in the list.
- sort(): Sorts the list in ascending order.
- reverse(): Reverses the order of the list.


"""
fruits = ["Apple", "Banana", "Cherry"]
fruits2 = ["Elderberry", "Fig", "Grape"]
print(fruits)
fruits.append("Date")
print(fruits)
fruits.extend(fruits2)
print(fruits)
fruits.insert(1,"Blueberry")
print(fruits)
fruits.remove("Fig")
print(fruits)
popped_fruit = fruits.pop()
print(f"Popped fruit: {popped_fruit}")
print(fruits)
index_of_cherry = fruits.index("Cherry")
print(f"Index of Cherry: {index_of_cherry}")
count_of_apple = fruits.count("Apple")
print(f"Count of Apple: {count_of_apple}")
fruits.sort()
print(f"Sorted fruits: {fruits}")
fruits.reverse()

print(f"Reversed fruits: {fruits}")



"""
3. List Comprehensions:
This is the hallmark of a Python Programmer. It allows you to create new lists in a very consise way.
- Syntax: [expression for item in iterable if condition]
- expression: The value to be added to the new list.
- item: The variable representing each element in the iterable.
- iterable: The collection you are iterating over (like a list).
- condition (optional): A filter that determines whether the item should be included in the new list.
squares = [x**2 for x in range(1,11)]
---> expression is x**2
---> item is x
---> iterable is range(1,11)
---> condition is omitted here

"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# The old way (c++/Java style)
squares = []
for num in numbers:
    squares.append(num**2)
print(f"Squares (old way): {squares}")

# The Pythonic way (List Comprehension)
squares = [num**2 for num in numbers]
print(f"Squares (List Comprehension): {squares}")