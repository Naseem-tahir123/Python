"""
                            Conditionals (Decision Making)
This module demonstrates the use of conditional statements in Python.
It includes examples of if, elif, and else statements to control the flow of execution
based on different conditions.
if:
    Executes a block of code if a specified condition is true.
elif:
    Allows checking multiple conditions sequentially.
else:
    Executes a block of code if none of the preceding conditions are true.  
"""     

server_load = 85 # percentage
if server_load > 90:
    print("CRITICAL: Spinnig up new server instances!")
elif server_load > 70:
    print("WARNING: Load is getting high, Monitoring closely.")
elif server_load > 50:
    print("INFO: Trafffic is moderate.")
else:
    print("OK: System is idling.")

                                # Nested Condition
"""
You can put an if inside of an if. This is called nesting
Warning:
    Be careful when nesting conditionals. Too much nesting can make your code hard to read.
    If you find yourself doing this, you usually need to refactor your code.
"""

user_logged_in = True 
is_admin = False
if user_logged_in:
    if is_admin:
        print("Redirecting to admin dashboard...")
    else:
        print("Redirecting to homepage...")
else:
    print("Please log in to continue.")


                            # Ternary Operators (One line Conditionals)
"""
This is for the cases where you want to assign a value based on a condition in a single line.
It allows us to condense 4 lines of if/else logic into a single line.
We use this for simple variable assignment.
"""

# The long way (Beginner)
score = 80
status = ""
if score >= 50:
    status = "Pass"
else:
    status = "Fail"

# The professional way (Ternary)
status = "Pass" if score >= 50 else "Fail"