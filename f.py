import sys

sys.stdin=open("seq.in", "r")

n = input()

numbers = input().split()

tri = sorted(numbers)

if tri == numbers:

    print(1)

    sys.exit(0)

if tri == numbers[::-1]:

    print(2)

    sys.exit(0)

print(3 if numbers[0] < numbers[1] else 4)