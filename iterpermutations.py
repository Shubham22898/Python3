#printing permutations

from itertools import permutations
s, n = map(str,input().split())
s = sorted(s)

for ele in list(permutations(s,int(n))):
    print("".join(ele))
