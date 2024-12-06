inp = input()
safeCount = 0
while inp != '':
    levels = list(map(int, inp.split(' ')))
    increasing = levels[0] < levels[1]
    valid = True
    if increasing:
        for i in range(1, len(levels)):
            diff = levels[i] - levels[i-1]
            if not (diff >= 1 and diff <= 3):
                valid = False
                break
    else:
        for i in range(1, len(levels)):
            diff = levels[i-1] - levels[i]
            if not (diff >= 1 and diff <= 3):
                valid = False
                break

    if valid:
        safeCount += 1
    inp = input()

print(safeCount)
