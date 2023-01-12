import matplotlib.pyplot as plt
import time


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
    for i in range(0, 5):
        n = int(input("Enter a number: "))
        nVals.append(n)

        start_time = time.time()
        fib2val = fib2(n)
        fib2Vals.append(time.time() - start_time)

    plt.plot(nVals, fib2Vals)
    plt.xlabel('n')
    plt.ylabel('time')
    plt.title('Fib2')
    plt.show()
