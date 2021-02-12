import sys

sys.stdin = open("winner.in", "r")

N = input()

resultats = input().split()

N1 = resultats.count('1')

N2 = resultats.count('2')

if N1 > N2: print("Mike")

elif N2 > N1: print("Jack")

else: print("Tie")