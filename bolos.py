import random

class Bolos:
    def __init__(self, partida):
        self.bolos = 10
        self.partida = partida

    def inciar_partida(self):
        self.partida.append({})
        self.partida.append({})

    def tirados(self):
        l = []
        bolos_tirados = random.randint(0, 10)
        l.append(bolos_tirados)
        if bolos_tirados == 10:
            print('Has hecho pleno')
        else:
            bolos_tirados_dos = random.randint(0, 10-bolos_tirados)
            l.append(bolos_tirados_dos)
            if bolos_tirados_dos == 10-bolos_tirados:
                print('Has hecho semipleno')

        return l
    
    def partidaa(self):
        self.inciar_partida()
        jugador1 = input('Digame el nombre del jugador 1')
        jugador2 = input('Digame el nombre del jugador 2')
        turnos = 0
        while turnos != 10:
            print('Turno jugador 1')
            tj1 = self.tirados()
            if tj1[0]==10:
                print("Bolos tirados "+str(tj1[0]))
            else:
                print("Bolos tirados "+str(tj1[0])+ " "+ str(tj1[1]))

            print('Turno jugador 2')
            tj2 = self.tirados()
            if tj2[0]==10:
                print("Bolos tirados "+str(tj2[0]))
            else:
                print("Bolos tirados "+str(tj2[0])+ " "+ str(tj2[1]))

            clave_dic="Turno "+ str(turnos)
            self.partida[0][clave_dic] = tj1
            self.partida[1][clave_dic] = tj2
            turnos +=1

        print(jugador1 + '\n')
        for i in self.partida[0]:
            if self.partida[0][i][0]<10:
                print(i+str(self.partida[0][i][0])+str(self.partida[0][i][1]))
            else:
                print(i+str(self.partida[0][i][0]))

        print(jugador2 + '\n')
        for i in self.partida[1]:
            if self.partida[1][i][0]<10:
                print(i+str(self.partida[1][i][0])+str(self.partida[1][i][1]))
            else:
                print(i+str(self.partida[1][i][0]))


        return self.partida


bolos = Bolos([])
print(bolos.partidaa())
    


