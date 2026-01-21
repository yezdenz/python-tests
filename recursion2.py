#n = 4 + 3 + 2 + 1


# def sumIntegers(n: int) -> int:
#     if (n == 1):
#         return 1
#     else:
#         return n + sumIntegers(n - 1)

    
def sumIntegers(n: int) -> None:
    if (n == 1):
        return 1
    else:
        return n + sumIntegers(n - 1)
    
def countdown(n: int) -> None:
    if (n % 2 == 0):
        isEven(n)
    else:
        isOdd(n) 
    
def isEven(n: int) -> None:
    if (n >= 1):
        print(str(n) + " is even")
        isOdd(n - 1)

def isOdd(n: int) -> None:
    if (n >= 1):
        print(str(n) + " is odd")
        isEven(n - 1)
    
print(countdown(sumIntegers(4)))
