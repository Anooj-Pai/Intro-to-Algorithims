import matplotlib.pyplot as plt
import time


def fib1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fib1(n-1) + fib1(n-2)


def fib2(n):
    nums = [0, 1]
    if n == 0:
        return 0

    for i in range(2, n+1):
        nums.append(nums[i-1] + nums[i-2])

    return nums[n]


if __name__ == '__main__':
    fib1Vals = []
    fib2Vals = []
    nVals = []
    for i in range(0, 12):
        n = int(input("Enter a number: "))
        nVals.append(n)
        start_time = time.time()
        fib1val = fib1(n)
        fib1Vals.append(time.time() - start_time)

        start_time = time.time()
        fib2val = fib2(n)
        fib2Vals.append(time.time() - start_time)

    print("Fib1:")
    print("---------------------")
    for j in range(0, 12):
        print("%d %lf" % (nVals[j], fib1Vals[j]))
    print("---------------------")

    print("Fib2:")
    print("---------------------")
    for j in range(0, 12):
        print("%d %lf" % (nVals[j], fib2Vals[j]))
    print("---------------------")

    plt.plot(nVals, fib1Vals)
    plt.xlabel('n')
    plt.ylabel('time')
    plt.title('Fib1')
    plt.show()

    plt.plot(nVals, fib2Vals)
    plt.xlabel('n')
    plt.ylabel('time')
    plt.title('Fib2')
    plt.show()
