import sys


def matrix_chain_order(p):
    n = len(p) - 1
    m = [[sys.maxsize for j in range(n+1)] for i in range(n+1)]
    s = [[0 for j in range(n)] for i in range(n)]

    for i in range(n+1):
        m[i][i] = 0

    for l in range(2, n+1):
        for i in range(1, n-l+2):
            j = i + l - 1
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i-1][j-2] = k

    return m[1][n], s


def print_optimal_parens(s, i, j):
    if i == j:
        print("A{}".format(i), end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i-1][j-2])
        print_optimal_parens(s, s[i-1][j-2]+1, j)
        print(")", end='')


# Test the algorithm on the given input
p = [10, 20, 30, 40, 50, 40, 10, 50, 20]
cost, s = matrix_chain_order(p)
print("Minimum number of operations:", cost)
print_optimal_parens(s, 1, len(p)-1)
print('\n')
