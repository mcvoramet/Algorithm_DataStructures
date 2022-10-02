# Recursive Binary Search 1

def recursive_binary_search_1(list, target, start=0, end=None):
    if end is None:
        end = len(list) - 1
    if start > end:
        return -1

    mid = (start + end) // 2

    if target == list[mid]:
        return mid
    else:
        if target < list[mid]:
            return recursive_binary_search_1(list, target, start, mid-1)
        else:
            return recursive_binary_search_1(list, target, mid+1, end)


# Recursive Binary Search 2

def recursive_binary_search_2(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list)//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search_2(list[midpoint+1:], target)
            else:
                return recursive_binary_search_2(list[:midpoint], target)


def verify(result):
    print("Target found: ", result)


numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
result = recursive_binary_search_2(numbers, 3)
verify(result)

result = recursive_binary_search_2(numbers, 33)
verify(result)
