labr=[" "," ","X","X","X","X","X","X","X","X","X"],["X"," ","X","X","X","X"," "," "," "," ","X"],["X"," ","X","X","X","X"," ","X","X"," ","X"],["X"," "," "," "," ","X"," "," ","X"," ","X"],["X","X","X","X"," ","X","X"," ","X"," ","X"],["X","X","X","X"," "," "," "," ","X"," ","X"],["X","X","X","X","X","X","X","X"," "," ","X"],["X","X","X","X","X","X","X","X"," ","X","X"],["X","X","X","X","X","X","X","X"," "," ","X"],["X","X","X","X","X","X","X","X","X"," "," "]

for i in labr:
    print(i)

posicionX = 0
posicionY = 0
ulti_mov = ''
while True:
    if posicionX == 10 and posicionY == 9:
        print('Ha llegado al final del laberinto')
        break
    else:
        if labr[posicionY][posicionX+1] == ' ' and ulti_mov != 'a':
            posicionX += 1
            ulti_mov='d'
        elif labr[posicionY+1][posicionX] == ' ' and ulti_mov != 'w':
            posicionY += 1
            ulti_mov='s'
        elif labr[posicionY][posicionX-1] == ' ' and ulti_mov != 'd':
            posicionX -= 1
            ulti_mov='a'
        elif labr[posicionY-1][posicionX] == ' ' and ulti_mov != 's':
            posicionY -= 1
            ulti_mov='w'

        print(posicionX, posicionY)