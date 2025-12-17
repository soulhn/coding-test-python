import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
  str_ = input().rstrip()
  print(str_[0]+str_[-1])
