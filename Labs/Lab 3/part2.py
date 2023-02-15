import random
import math


def modexp(x, y, N):
    if y == 0:
        return 1
    z = modexp(x, math.floor(y/2), N)
    if y % 2 == 0:
        return (z**2) % N
    else:
        return x * (z**2 % N)


def primality2(N, k):
    arr = []
    prime = True
    count = 0
    for i in range(k):
        arr.append(random.randint(1, N-1))
    for a in arr:
        if modexp(a, N-1, N) != 1:
            count += 1
            prime = False
    print("Coprime with", count, "numbers.")
    print("Probability prime:", (1-(count/k)))
    return prime


if __name__ == "__main__":
    arr = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745, 63973, 75361, 101101,
           115921, 126217, 162401, 172081, 188461, 252601, 278545, 294409, 314821, 334153, 340561, 399001, 410041, 449065, 488881]
    for a in arr:
        if primality2(a, 20) == False:
            print(a, "is not prime.\n")
        else:
            print(a, "is prime.\n")
