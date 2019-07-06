'''Write a function to find the redundant or repeated items in a list and return them in sorted order. This method should return a list of redundant integers in ascending sorted order.'''

def duplicate_items(list_numbers): 
    result = []
    list_numbers.sort()
    for i in range(1,len(list_numbers)):
        if list_numbers[i] == list_numbers[i - 1]:
            result.append(list_numbers[i])
    return result