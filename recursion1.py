def sumOfIntegers(n):
    if n == 1:
        print(1, end = "")
        return 1
    else:
        print(n, end = " + ")
        return n + sumOfIntegers(n-1)
totalSum = sumOfIntegers(5)
print(" =", totalSum)

def factorialOfIntegers(n):
    if n == 1:
        print (1, end = "")
        return 1
    else:
        print(n, end = " + ")
        return n * factorialOfIntegers(n-1)
totalFactorial = factorialOfIntegers(10)

print(" =", totalFactorial)

def fibonacciSequence(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacciSequence(n-1) + fibonacciSequence(n-2)
    
print(fibonacciSequence(56))

