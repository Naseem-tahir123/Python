                                    # Loops (Do not repeat Yourself)

"""
1. for loop (iterating with in a sequence):
In C or Java you iterate using index numbers (i = 10 , i < 10, i++). Python is different.
Python iterates directly over the items usign the in keyword.

"""
# Example 1: Iterating over a list
frameworks = ["Django", "Flask", "FastAPI", "Pyramid"]
for tool in frameworks:
    print(f"Installing ..... {tool}")

# Example 2: Iterating a specific number of times using range()
# range(start, stop, step) -> stop is EXCLUSIVE (not included)

for i in range(1,6):
    print(f"Attempt {i} of 5")

"""
2. while loop (repeating until a condition is met):
Use this when you don't know how many times loop need to run. It runs as long as the condition is True.
Warning:
    Also ensure there is a logic to break the loop, otherwise you will create an 'infinite loop'.
    and your program crashes.
"""

battery_level = 10
while battery_level >0:
    print(f"Batter level is at {battery_level}%.")
    battery_level -= 2 # Decrement is CRITICAL to stop the loop.
print("System shutting down...")

"""
3. Loop Control Statements (break, continue, pass):
    => break: "EMERGENCY EJECT" Stop the loop immediately
    => continue: "SKIP THIS ITERATION" Stop the current iteration and jump to the next one
    => pass: "DO NOTHING" Placeholder when no action is needed
"""
data_stream = [10, 20, -5, 30, None, 50, 0, 70]

for data in data_stream:
    if data is None:
        print("Data is missing, skipping...")
        continue
    if data <=0:
        print("Invalid data encountered, stopping processing.")
        break
    if data % 10 == 0:
        pass
    print(f"processing data: {data}")



"""
Challenge:
1. Create a variable correct_password = "Rahi123". 
2. Use a while loop to allow the user 3 attempts to enter the password. 
3. Inside the loop: 
    --> Take input() from the user. 
    --> If the input matches correct_password: Print "Access Granted" and break. 
    --> Else: Print "Try Again". 
4. If the loop finishes (user fails 3 times), print "Account Locked". 
    --> Hint: You might need a counter variable or the else block of a while loop (look that up!).
    """
correct_password = "Rahi123"
attempt = 0
while attempt < 3:
    user_input = input("Enter your password:")
    attempt +=1
    
    if user_input == correct_password:
        print("Logging in ...")
        break
    else:
        print("Try Again")
    print("Maximum attempts reached. Acount locked.")
    

