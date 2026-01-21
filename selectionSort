numbers = [4, 5, 6, 8, 9]


def selectionSortASC(a):
    n = len(a)
    for i in range(0, n - 1):
        temp = i
        for j in range(i + 1, n):
            if a[j] < a[temp]:
                temp = j

        if temp != i:
            a[temp], a[i] = a[i], a[temp]
    return a

def selectionSortDSC(a):
    n = len(a)
    for i in range(0, n - 1):
        temp = i
        for j in range(i + 1, n):
            if a[j] > a[temp]:
                temp = j

        if temp != i:
            a[temp], a[i] = a[i], a[temp]
    return a



sortedListASC = selectionSortASC(numbers.copy())
sortedListDSC = selectionSortDSC(numbers.copy())

print("Ascending Sorted List:", ' '.join(str(num) for num in sortedListASC))
print("Descending Sorted List:", ' '.join(str(num) for num in sortedListDSC))

