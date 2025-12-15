arr = [2,4,2,7,5,1,9]

min_val = 2
def minVal(*args):
    global min_val
    for i in args:
        if i < min_val:
            min_val = i
    return min_val

print(f"The minimum value is: {minVal(*arr)}")
     
