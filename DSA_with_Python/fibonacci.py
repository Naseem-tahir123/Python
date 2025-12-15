                            # 1. Implementation Using a For Loop
# a = 0
# b = 1
# print(a)
# print(b)
# for i in range(1,19):
#     c = a + b
#     print(c)
#     a = b
#     b = c

                            # 2. Implementation Using Recursion (Function calling itself)

a, b = 0, 1
print(a)
print(b)
count = 2
def fibonacci(num1, num2):
    global count
    if count <= 19:
        
        num3 = num1 + num2
        print(num3)
        num1 = num2
        num2 = num3
        count += 1
        fibonacci(num1, num2)
    else:
        return

fibonacci(0,1)

                        # 3. Finding The nth Fibonacci Number Using Recursion
def F(n):
    if n <= 1:
        return n
    else:
        return F(n-1) + F(n-2)
    
print(F(4))


    