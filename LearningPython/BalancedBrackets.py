import sys
from collections import defaultdict

bracket_map = {'{':'}', '(':')', '[':']'}
t = int(input().strip())
for a0 in range(t):
    s = input().strip()
    counter = defaultdict(int)
    for ch in s:
        if(ch in bracket_map):
            counter[bracket_map[ch]] += 1
        else:
            counter[ch] -= 1
            
    if(any(val != 0 for val in counter.values())):
        print('NO')
    else:
        print('YES')
