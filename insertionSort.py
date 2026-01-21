numbers = [1, 98, 15, 73, 41]

# def bubbleSortASC(a):
#     n = len(a)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]
#     return a

# print("Original List:", ' '.join(str(num) for num in numbers))
# sortedNumbers = bubbleSortASC(numbers)
# print("Ascending Sorted List:", ' '.join(str(num) for num in numbers))

def insertionSortASC(a):
    n = len(a)

    for i in range(1, n):
        temp = a[i]
        j = i - 1

        while j >= 0 and a[j] > temp:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = temp
    return a

def insertionSortDSC(a):
    n = len(a)

    for i in range(1, n):
        temp = a[i]
        j = i - 1

        while j >= 0 and a[j] < temp:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = temp
    return a

print("Original List:", ' '.join(str(num) for num in numbers))

ascendingNumbers = insertionSortASC(numbers.copy())
descendingNumbers = insertionSortDSC(numbers.copy())

print("Ascending Sorted List:", ' '.join(str(num) for num in ascendingNumbers))
print("Descending Sorted List:", ' '.join(str(num) for num in descendingNumbers))

