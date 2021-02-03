import re

n, m = map(int, raw_input().split())
a = []

for _ in range(n):
    a.append(raw_input()[:m])

s = ''.join(''.join(e) for e in zip(*a))
result = re.sub(r'([a-zA-Z0-9])([^a-zA-Z0-9]+)(?=[a-zA-Z0-9])', r'\1 ', s)
print result
#import math
#import os
# import random
# import re
# import sys
# first_multiple_input = input().rstrip().split()
# n = int(first_multiple_input[0])
# m = int(first_multiple_input[1])
# matrix = []
# for _ in range(n):
#     matrix_item = input()
#     matrix.append(matrix_item)
# x,y = list(map(int,input().split()))
# rows =[input() for i in range(x)]
# text = "".join([row[i] for i in range(y) for row in rows])
# text = re.sub('([A-Za-z1-9])[^A-Za-z1-9]+([A-Za-z1-9])', r'\1 \2', text)
# text = re.sub('  ', ' ', text)
# print(text)
import re
