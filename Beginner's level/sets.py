        # Sets (The Filter, Unordered, Unique, Mathematical)
"""
Sets use curly braces {}. They do not allow duplicates and they have no order (you cannot index them
like my_set[0]).
"""

"""
1. Unique Values:
This is the fastest way to remvoe duplicates from a list.
"""
raw_emails = ['abc@gmail.com', 'xyz@gmail.com', 'abc12@gmail.com', 'abc@gmail.com', 'xyz@gmail.com']

clean_emails = list(set(raw_emails)) # (Order may varry since sets are unordered)
print(raw_emails)
print(clean_emails)

"""
2. Set Operations (union, intersection, difference, symmetric difference):
This is pure venn diagram logic. Extremely useful in data analysis.

"""
# Example Sets
dev_team = {'Alice', 'Bob', 'Charlie', 'David'}
design_team = {'Eve', 'Frank', 'Charlie', 'Grace'}
# Union ' | ': Combine everyone (no duplicates)
all_team_members = dev_team.union(design_team)
print(dev_team)
print(design_team)
print(f"All Team Members: {all_team_members}")

# Intersection ' & ': who is in both team:
common_members = dev_team.intersection(design_team)
print(f"Common Members: {common_members}")

# Differnce ' - ': who is in dev_team but not in design_team
pure_coders = dev_team.difference(design_team)
print(f"Pure Coders: {pure_coders}")