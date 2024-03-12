#Write a program to print all the unique combinations of 1,2,3 and 4

import itertools
combinations = list(itertools.permutations([1, 2, 3, 4]))
for combo in combinations:
    print(combo)
