import time
import matplotlib.pyplot as plt

if __name__ == "__main__":
    n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    timelist = []
    for i in n:
        start = time.time()
        exp = pow(2, i)
        tot = pow(2, exp)
        end = float(time.time() - start)
        timelist.append(end)

    print(timelist)
    plt.plot(n, timelist)
    plt.xlabel("n")
    plt.ylabel("time")
    plt.show()
