def permute(string, temp=""):
    if len(string) == 0:
        print(temp)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0:i]
            back = string[i+1:]
            frontback = front + back
            permute(frontback, letter + temp)

print(permute("ABC", ""))

def reverseString(string):
    if len(string) <= 1:
        return string
    return reverseString(string[1:]) + string[0]

print(reverseString("Denz"))

def largestNumber(array):
    largest = array[0]

    for i in range(len(array)):
        if array[i] > largest:
            largest = array[i]
    return largest

array = [12, 4, 13, 15, 19]

print("Array:", array)
print("The largest number is:", largestNumber(array))
    

def smallestNumber(array):
    smallest = array[0]

    for i in range(len(array)):
        if array[i] < smallest:
            smallest = array[i]
    return smallest 

print("Array:", array)
print("The largest number is:", smallestNumber(array))
