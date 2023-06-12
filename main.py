arr = [5,17,3,9,1]
for i in range(0, len(arr)):
    arr[i] = arr[i] * 2
min = min(arr)
max = max(arr)
for i in range(0, len(arr)):
    if arr[i] == min:
        arr[i] = arr[i] * 3
    elif arr[i] == max:
        arr[i] = arr[i] * 3

