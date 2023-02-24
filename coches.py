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



        


