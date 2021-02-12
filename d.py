import sys

sys.stdin = open("number.in", "r")

N = input()

digits = list(input())

digits.sort(reverse = 1)

print(''.join(digits))