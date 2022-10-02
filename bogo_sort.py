import random

# As the list grow larger the number of attempts increase significantly
numbers = [3,2,5,67,43,32]

def is_sorted(values):
    for index in range(len(values)-1):
        if values[index] > values[index+1]:
            return False
    return True

def bogo_sort(values):
    attempts = 0
    while not is_sorted(values):
        random.shuffle(values)
        attempts += 1
    print("#attempts: ", attempts)
    return values

print(bogo_sort(numbers))
 
