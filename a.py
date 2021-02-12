import sys

sys.stdin = open("digits.in", "r")

dico = {'0' : 'O','1' : 'I','2' : 'Z','3' : 'E','5' : 'S','7' : 'L','8' : 'B','9' : 'G'}

n = int(input())



for _ in range(n):

    res=""

    for i in input(): res+=dico[i]

    print(res[::-1])