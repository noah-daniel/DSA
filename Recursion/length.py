#calculate the length of an array using recursion
def length(arr):
    if arr == []:
        return 0
    else:
        return 1 + len(arr[1:])

print(length([1,2,3,4,5,6,7]))