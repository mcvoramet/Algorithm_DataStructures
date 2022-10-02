# The implementation of linear search covered in the course is provided below.

def linear_search(lst, target):
    """Returns the index position of the target if found, else returns -1"""

    for i in range(0, len(lst)):
        if lst[i] == target:
            return i
    return -1

def verify(index):
    if index != -1:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
result = linear_search(numbers, 21)
verify(result)



# The code can be cleaned up a bit by using the enumerate function on the list.

def linear_search(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1




