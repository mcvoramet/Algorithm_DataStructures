def quick_sort(values):
    # Remember:list of an empty and one value don't need to be sorted
    if len(values) <= 1:
        return values
    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]
    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    print("%15s %1s %-15s" % (less_than_pivot, pivot, greater_than_pivot))
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

#numbers = [106,5,2,33,5,32,13,554,756,44,33]
#sorted_numbers = quick_sort(numbers) 
#print(sorted_numbers)















