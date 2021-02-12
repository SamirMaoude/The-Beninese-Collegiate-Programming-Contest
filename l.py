import sys

sys.stdin=open("trick.in", "r")

X , Y = map(int, input().split())

print(max(X + Y, X * Y, X - Y, Y - X))