                        # Arithmetic Operators(+, -, *, /, %, **, //)
a = 10
b = 3
print("Arithmetic Operators:")
print("Addition:", a+b)
print("Subtraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)
print("Modulus:", a%b)
print("Exponentiation:", a**b)
print("Floor Division:", a//b) # chops off the decimal part


            # Comparison Operators(==, !=, >,<, >=, <=) It returns boolean values(True or False)
print("\nComparison Operators:")
print("Equal to:", a==b)
print("Not equal to:", a!=b)
print("Greater than:", a>b)
print("Less than:", a<b)
print("Greater than or equal to:", a>=b)
print("Less than or equal to:", a<=b)

                        # Logical Operators(and, or , not)
print("\nLogical Operators:")
print("AND Operator:", (a>b) and (a!=b))
print("OR Operator:", (a<b) or (a!=b))
print("NOT Operator:", not(a>b))

                        # Identity Operators(is, is not)
print("\nIdentity Operators:")
lst_1 = [1, 2, 3]
lst_2 = [1, 2, 3]
lst_3 = lst_1
print("Is Operator:", lst_1 is lst_3)
print("Is Operator:", lst_1 is lst_2)
print("Is Not operator:", lst_1 is not lst_3) 
print("Is Not operator:", lst_1 is not lst_2)


                        # Membership Operrators(in, not in)
users = ['Athar', 'Naseem', 'Shehbaz']
current_user = 'Hanzala'
if current_user not in users:
    print("Access Denied")

"""
Challenge:
1. Takes a user's yearly_salary as input. 
2. Checks if the input is a valid number (using isdigit()—look this up!). 
3. Calculates monthly_salary (Yearly / 12).
"""

yearly_salary = input("Please Enter your year Salary: ")
try:
    if yearly_salary.isdigit():
        yearly_salary = float(yearly_salary)
        print(f"Your monthly salary is: {yearly_salary/12}")


except:
    print("Invalid Input")