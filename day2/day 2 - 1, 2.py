record = input()
powerSum = 0
while record and record != '':
    id_game = record.split(': ')
    rounds = id_game[1].split('; ')
    minR, minG, minB = (0,0,0)
    for round in rounds:
        r,g,b = (0,0,0)
        balls = round.split(', ')
        for ball in balls:
            count, color = ball.split()
            if color[0] == 'r': 
                r = int(count)
                minR = max(minR, r)
            if color[0] == 'g': 
                g = int(count)
                minG = max(minG, g)
            if color[0] == 'b': 
                b = int(count)
                minB = max(minB, b)
    powerSum += minR * minG * minB    

    record = input()
print(powerSum)
