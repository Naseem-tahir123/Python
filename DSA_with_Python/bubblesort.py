# arr = [6,3,5,9,8,11,1]
# n = len(arr)
# for i in range(n-1):
#     for j in range(n-i-1):
#         if arr[j] >  arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]

# print(f"Sorted array: {arr}")

array = [9,4,7,3,8,11,2,1]
n = len(array)
for i in range(n-1):
    swaped = False
    for j in range(n-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1] , array[j]
            swaped = True
    if not swaped:
        break
print(f"sorted array is {array}")
