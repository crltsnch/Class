labr=[" "," ","X","X","X","X","X","X","X","X","X"],["X"," ","X","X","X","X"," "," "," "," ","X"],["X"," ","X","X","X","X"," ","X","X"," ","X"],["X"," "," "," "," ","X"," "," ","X"," ","X"],["X","X","X","X"," ","X","X"," ","X"," ","X"],["X","X","X","X"," "," "," "," ","X"," ","X"],["X","X","X","X","X","X","X","X"," "," ","X"],["X","X","X","X","X","X","X","X"," ","X","X"],["X","X","X","X","X","X","X","X"," "," ","X"],["X","X","X","X","X","X","X","X","X"," "," "]

for i in labr:
    print(i)

posicionX = 0
posicionY = 0

while True:
    cop=labr
    if posicionX == 10 and posicionY == 9:
        print('Ha llegado al final del laberinto')
        break
    else:
        m = input('Ingrese a donde quiere moverse: ')
        if m == 'w':
            if posicionY == 0:
                print('No puede moverse hacia arriba')
            elif labr[posicionY-1][posicionX] == 'X':
                print('No puede moverse hacia arriba')
            else:
                cop[posicionY-1][posicionX] = 'O'
                posicionY -= 1
            
        elif m == 'a':
            if posicionX == 0:
                print('No puede moverse hacia la izquierda')
            elif labr[posicionY][posicionX-1] == 'X':
                print('No puede moverse hacia la izquierda')
            else:
                cop[posicionY][posicionX-1] = 'O'
                posicionX -= 1
        
        elif m == 's':
            if posicionY == len(labr)-1:
                print('No puede moverse hacia abajo')
            elif labr[posicionY+1][posicionX] == 'X':
                print('No puede moverse hacia abajo')
            else:
                cop[posicionY+1][posicionX] = 'O'
                posicionY += 1
        
        elif m == 'd':
            if posicionX == len(labr[0])-1:
                print('No puede moverse hacia la derecha')
            elif labr[posicionY][posicionX+1] == 'X':
                print('No puede moverse hacia la derecha')               
            else:
                cop[posicionY][posicionX+1] = 'O'
                posicionX += 1
        for i in cop:
            print(i)
        #print(posicionX, posicionY)
