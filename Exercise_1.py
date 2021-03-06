# Python code to implement iterative Binary
# Search.

# It returns location of x in given array arr
# if present, else returns -1
def binarySearch(arr, l, r, x):
    l = 0
    h = len(arr) - 1

    while l <= h:
        mid = l + (h-l) // 2
        if x == arr[mid]:
            return mid
        if x < arr[mid]:
            h = mid - 1
        else:
            l = mid + 1

    return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")

# Time complexity: O(log n) where n is size of input
# Space - O(1)