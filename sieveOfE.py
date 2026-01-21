def sieveOfEratosthenes(n):
    primeNumbers = []
    prime = [True]
    prime *= (n + 1)
    prime[0] = False
    prime[1] = False

    p = 2

    while (p * p) <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    
    for j in range(2, n + 1):
        if prime[j]:
            primeNumbers.append(j)
    
    return primeNumbers


while True:
    
    print("\nEnter 'Q' for Quit")
    n = (input("Input n = "))

    if n.upper() == 'Q':
        break
    if not n.isdigit():
        continue
    
    n = int(n)
    print(sieveOfEratosthenes(n))
