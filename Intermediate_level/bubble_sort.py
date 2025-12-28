arr = [3,2,7,4,9,8]
# print(len(arr))
n = len(arr)

for i in range(n-1):
    for j in range(n-1-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1] , arr[j]
        else:
            pass
print(arr)