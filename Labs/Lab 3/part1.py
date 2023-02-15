import math


def modexp(x, y, N):
    if y == 0:
        return 1
    z = modexp(x, math.floor(y/2), N)
    if y % 2 == 0:
        return (z**2) % N
    else:
        return x * (z**2 % N)


if __name__ == '__main__':
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    N = int(input("Enter N: "))
    result = modexp(x, y, N)
    print("Result:", result)
