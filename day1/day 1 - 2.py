from curses.ascii import isdigit


numnames = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numnamesrev = ['orez', 'eno', 'owt', 'eerht', 'ruof', 'evif', 'xis', 'neves', 'thgie', 'enin']

inp = input()
ssum = 0
outp = []
while inp:
# for i in range(10):
    revinp = inp[::-1]
    num=0
    left=len(inp)
    right=len(inp)

    for nameind,name in enumerate(numnames):
        findind = inp.find(name)
        if findind>=0 and findind<left:
            left = findind
            num = nameind*10
    for i in range(left):
        if inp[i].isdigit():
            num = int(inp[i])*10
            break
    
    for nameind, name in enumerate(numnamesrev):
        findind = revinp.find(name)
        if findind>=0 and findind < right:
            right = findind
            num = (num//10)*10 + nameind
    for i in range(right):
        if revinp[i].isdigit():
            num = (num//10)*10 + int(revinp[i])
            break

    ssum += num
    # print(inp, ':', num)
    outp.append((inp,num))
    inp = input()

print(ssum)
# print(outp)