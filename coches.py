class Coche:
    def __init__(self, matricula):
        self.matricula = matricula
    
    def get_matricula(self):
        return self.matricula
    
    def set_matricula(self, matricula2):
        self.matricula = matricula2
    
    def __str__(self):
        return 'Matricula: ' + self.matricula

class Camion(Coche):
    def __init__(self,matricula, peso):
        super().__init__(matricula)
        self.peso = peso
    
    def get_peso(self):
        return self.peso
    
    def set_peso(self, peso2):
        self.peso = peso2
    
    def __str__(self):
        return super().__str__() + 'Peso: ' + str(self.peso)

camion1 = Camion('1234 ABC', 222)
print(camion1.get_peso())
camion1.set_peso(334)
print(camion1)



valencia =  [Camion('0001VVV',8000), Camion('0002VVV',7000), Camion('0003VVV',5500)]
castellon = [Camion('0001CCC',4000), Camion('0002CCC',6500)]
alicante =  [Camion('0001AAA',3500), Camion('0002AAA',5000), Camion('0003AAA',9000)]
murcia =    [Camion('0001MMM',2000), Camion('0002MMM',3000)]

ciudades = ['Valencia', 'Castellon', 'Alicante', 'Murcia']
flotas = [valencia, castellon, alicante, murcia]

flota = dict(zip(ciudades, flotas))
for c in flota:
    for cam in flota[c]:
        print(cam)
print()

# cada pedido es una lista [CARGA,KILOMETROS]
CARGA = 0; KILOMETROS = 1

pedidos = {'Valencia' : [[6000,400], [5000,800], [6900, 980]],
           'Castellon' : [[5000,400], [6000,800]],
           'Alicante' : [[4900,400], [3000,800], [7900, 980]],
           'Murcia' : [[2800,400], [1500,800]]
          }

def carga(ciudad):
    peso=0
    for i in flota:
        if i == ciudad:
            for j in range(len(flota[i])):
                peso += flota[i][j].get_peso()

    return peso
print(carga('Valencia'))

def cargasobrante(ciudad):
    peso1 = 0
    for i in pedidos:
        if i == ciudad:
            for j in i:
                peso1 += pedidos[i][j][0]
    peso2=carga(ciudad)

    return peso2-peso1

def comprobar(ciudad):
    peso1 = 0
    for i in flota:
        if i == ciudad:
            for j in range(len(flota[i])):
                peso1 = flota[i][j].get_peso()

    peso2 = 0
    for i in pedidos:
        if i == ciudad:
            for j in i:
                peso2 += pedidos[i][j][0]
    
    if peso1 <= peso2:
        d = {}
        
