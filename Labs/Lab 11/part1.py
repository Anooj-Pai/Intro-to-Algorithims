def find_minimum_subset(S, n):
    uncovered = set(range(1, n+1))
    subset = []
    while uncovered:
        max_intersection = set()
        for s in S:
            intersection = s.intersection(uncovered)
            if len(intersection) > len(max_intersection):
                max_intersection = intersection
        subset.append(max_intersection)
        uncovered -= max_intersection
    return subset


S = [{1, 3, 5, 7, 10, 11}, {1, 2, 4, 5, 11}, {
    4, 8, 9}, {1, 3, 5, 8, 9, 10}, {2, 6, 10}]

n = 11

subset = find_minimum_subset(S, n)

print(subset)

# Q2
# The time complexity of this algorithm is O(|S| * n), where |S| is the size of the set S. This is because for each iteration, I go through all
# the sets in S to find the one with the maximum intersection with the uncovered set.

# Q3
# This algorithm is a greedy algorithm, which means that it may not always find the optimal solution. However, in this case, we can prove that
# the approximation ratio is at most ln(n). This means that the number of subsets found by the algorithm is at most ln(n) times greater than the
# minimum number of subsets needed to cover all the numbers between 1 and n.
