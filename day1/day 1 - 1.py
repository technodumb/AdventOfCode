
from curses.ascii import isdigit


ssum = 0
inp = input()
while inp:
    num = 0
    for i in inp:
        if i.isdigit():
            num = int(i)*10
            break
    for i in reversed(inp):
        if i.isdigit():
            num += int(i)
            break
    ssum += num
    inp = input()

print(ssum)