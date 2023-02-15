import random
import math
import timeit


def method1(x, y):
    answer = 0
    while (y != 0):
        if y & 1:
            answer += x
        x <<= 1
        y >>= 1
    return answer


def method2(x, y):
    if y == 0:
        return 0
    z = method2(x, math.floor(y/2))
    if (y % 2) == 0:
        return 2*z
    else:
        return x + 2*z


def method3(x, y):
    n = max(x.bit_length(), y.bit_length())
    if (n == 1):
        return x*y
    if x == 0 or y == 0:
        return 0

    nR = math.floor(n/2)

    xL = x >> nR
    m = xL << nR
    xR = x - m

    yL = y >> nR
    m = yL << nR
    yR = y - m

    P1 = method3(xL, yL)
    P2 = method3(xR, yR)
    P3 = method3(xL + xR, yL + yR)
    return P1 * (2**(2*nR)) + (P3 - P1 - P2) * 2**(nR) + P2


if __name__ == "__main__":
    d = int(input('Number of digits: '))
    m1_times = []
    m2_times = []
    m3_times = []
    print("Method 1: ", method1(10, 8))
    print("Method 2: ", method2(10, 8))
    print("Method 3: ", method3(10, 8))
    for i in range(10):
        a = b = ''
        for j in range(d):
            a += str(random.randint(1, 9))
            b += str(random.randint(1, 9))
        print("Trial", i+1, ":", "a =", a, "b =", b)
        m1_times.append(timeit.timeit('method1(' + a + ',' + b + ')',
                                      'from __main__ import method1', number=1))
        m2_times.append(timeit.timeit('method2(' + a + ',' + b + ')',
                                      'from __main__ import method2', number=1))
        m3_times.append(timeit.timeit('method3(' + a + ',' + b + ')',
                                      'from __main__ import method3', number=1))
    average_m1 = float(sum(m1_times))/10
    average_m2 = float(sum(m2_times))/10
    average_m3 = float(sum(m3_times))/10
    print("Average Times:", "\n\tMethod 1: %lf \n\tMethod 2: %lf \n\tMethod 3: %lf" % (
        average_m1, average_m2, average_m3))

    # Method 1 is 100000
    # Method 2 is limited to 1000 digits (Overload Error)
    # Method 3 is limited to 100000 digits (Slow)
