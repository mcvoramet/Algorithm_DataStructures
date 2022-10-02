# Iterative Binary Search (only work if the list of number is sorted!)

def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
 # (//) in python it's called float division operator (divide and round down to nearest number ex. 3//2 = 1)
        midpoint = (first + last)//2   
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint+1
        else:
            last = midpoint-1
    return -1


def verify(index):
    if index != -1:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
result = binary_search(numbers, 14)
verify(result)



