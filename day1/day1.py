sumval = 0

allNums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "0", '1', '2', '3', '4', '5', '6', '7', '8', '9']

with open('input.txt') as f:
    for line in f:
        lineVal = 0
        line = line.strip()
        lind = len(line)
        rind = -1

        for i in range(1,20):
            if allNums[i] in line:
                curInd = line.index(allNums[i])
                if curInd < lind:
                    lind = curInd
                    lineVal = lineVal%10 + (i%10)*10
                curInd = line.rindex(allNums[i])
                if curInd > rind:
                    rind = curInd
                    lineVal = (lineVal//10)*10 + i%10

        print(lineVal)
        sumval += lineVal
print()
print(sumval)
        