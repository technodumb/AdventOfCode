record = input()
idSum = 0
while record and record != '':
    id_game = record.split(': ')
    id = int(id_game[0].split()[1])
    rounds = id_game[1].split('; ')
    maxR, maxG, maxB = (12, 13, 14)
    valid = True
    for round in rounds:
        balls = round.split(', ')
        for ball in balls:
            count, color = ball.split()
            if color[0] == 'r': 
                if int(count) > maxR:
                    valid = False
                    break
                
            if color[0] == 'g': 
                if int(count) > maxG:
                    valid = False
                    break

            if color[0] == 'b': 
                if int(count) > maxB:
                    valid = False
                    break
        
    if valid:
        idSum += id
    record = input()
print(idSum)
