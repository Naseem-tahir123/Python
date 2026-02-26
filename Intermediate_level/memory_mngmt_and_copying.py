# Memory Management And Copying
"""
1. The Id function and references
In many programming languages (like C) variable is a box where you put data.
In python a variable is a Reference (a tag or sticky note) attached to an object in memory.

"""

# Integers are immutable objects in Python.
a = 100 
b = 100
print(id(a))
print(id(b))
print(a is b)  # True, because both a and b reference the same object in memory

# lists are mutable objects in Python.

l1 = [1, 2, 3]
l2 = [1, 2, 3]

print(id(l1))
print(id(l2))
print(l1 is l2)  # False, because l1 and l2 reference different objects in memory


"""
2. The Assignment Trap (=)
This is the common bug in code reviews.
When you say list3 = list1, you are not copying the data. You are just 
adding the second sticky note to the same object in memory.
"""

original_students = ['Alice', 'Bob', 'Charlie']
aliase = original_students # Just a new reference.

print(id(aliase) == id(original_students)) # True. They point to the same memory.

# The Disaster Scenario
aliase.append("David")
print(original_students)  
# Output: ['Alice', 'Bob', 'Charlie', 'David']    
# Wait I did't touch the original_students list!
# Because they are the same object, changing the one changes the other.

"""
3. Shallow Copy Vs Deep Copy:
To actually create the duplicate so you can modify one without affecting the other,
you need the copy module.   
a. A Shallow Copy (copy.copy())
b. A Deep Copy (copy.deepcopy())

"""

"""
                            -- Shallow Copy --
                => Good for: Flat lists (lists containing only numbers/strings).
                => Bad for: Nested lists (list inside lists)

"""
import copy 

menu = ["chowmein", "fried rice", ["Coke", "Sprite"]]

shallow_copied_menu = copy.copy(menu) # Creating a shallow copy

print(id(menu) == id(shallow_copied_menu))

# Proof 1: The containers are different
print(menu is shallow_copied_menu) # False, different objects
print(menu == shallow_copied_menu) # True, same content

# Proof 2: Modifying the top level is safe
shallow_copied_menu[0]  = "Pizza"
print(menu[0])  # Output: chowmein (Safe. The original is unchanged)


# THE TRAP: Modifying the nested list affects both
shallow_copied_menu[2][0] = "Marinda"
print(menu[2])  # Output: ['Marinda', 'Sprite'] (Not Safe. Original is changed)
# Catastrophe! The original menu changed!
# Why? Because the shallow copy only copied the reference of inner list, not the list itself.



"""
                            -- Deep Copy --
A deep copy walks through the object recursively. If it finds list inside a list, it copies 
that too. It creates a completey independent clone.
                => Good for: Nested lists (lists inside list).
                => Trade-off: It is slower and user more memory, but it is 100% safe
                            
"""
import copy

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

deep_copied_matrix = copy.deepcopy(matrix)  # Creating a deep copy
# Proff 1: The containers are different
print(id(matrix ) == id(deep_copied_matrix)) # False, different objects

# Proff 2: Modifying the top level is safe
deep_copied_matrix[0] = ['a', 'b', 'c']

print(matrix[0])  # Output: [1, 2, 3] (Safe. The original is unchanged)

# Proff 3: Modifying the nested list is also safe
deep_copied_matrix[2][2] = 'a'
print(deep_copied_matrix[2])  # Output: [7, 8, 'a'] (Changed in the copy)
print(matrix[2])  # Output: [7, 8, 9] (Safe. The original is unchanged)



"""
----- Pro Tip -----
When to use what?
- Use assignment (=) when you want multiple references to the same object.
- Use shallow copy for flat lists (no nested lists). e.g. list of strings or numbers.
- Use deep copy for nested lists (lists inside lists) or complex objects. 
    e.g. (a dictionary of json configuration, a matrix or AI datasets)
"""
