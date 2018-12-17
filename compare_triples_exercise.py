import itertools
import functools


def solve(a0, a1, a2, b0, b1, b2):
    marked = [0, 0]
    def constraints(group=[]):
        if len(group) == 0: return group
        if min(group) < 1 or max(group) > 100:
            raise ValueError
        else:
            return group

    a, b = constraints([a0, a1, a2]), constraints([b0, b1, b2])
    group_compare = list(itertools.zip_longest(a,b))
    for x in group_compare:
        if x[0] > x[1]:
            marked[0] += 1
        elif x[1] > x[0]:
            marked[1] += 1
    return marked



result = solve(1, 1, 6, 3, 3, 3)
print(result)
print(' '.join(map(str, list(result))))

# a, b = [0, 1, 2], [0, 0, 3]
# print(''.join(map(str,list(filter(None,itertools.starmap(compare, list(itertools.zip_longest(a,b))))))))
