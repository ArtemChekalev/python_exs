def binary_search(li, value): #O(log(n))
    low = 0
    high = len(li)-1
    while low<=high:
        middle = high - low
        prediction = li[middle]
        if prediction>value:
            high = middle - 1
        elif prediction == value:
            return middle
        else:
            low = middle + 1
    return None

def quicksort(li): #O(n*log(n))
    if len(li)<2:
        return li
    else:
        pivot = li[int(len(li) / 2)]
        left_half = [i for i in (li[:int(len(li) / 2)]+li[int(len(li) / 2)+1:] ) if i<=pivot]
        rigth_half = [i for i in (li[:int(len(li) / 2)]+li[int(len(li) / 2)+1:] ) if i>pivot]
        return quicksort(left_half)+[pivot]+quicksort(rigth_half)

