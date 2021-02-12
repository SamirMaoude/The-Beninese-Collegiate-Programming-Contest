import sys
import string

sys.stdin=open("mango.in", "r")

s = input().lower()

for i in string.ascii_lowercase:
    print(s.count(i),'' if i != 'z' else '\n',end='')

print(''.join(sorted(list(s))))