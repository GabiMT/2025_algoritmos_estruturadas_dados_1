class Carro:
    def __init__(self, modelo = None, ano = 2025):
        self.modelo = modelo
        self.ano = ano
        self.__quilometragem = 0

    def incrementar(self, km):
        if km > 0:
            self.__quilometragem += km

    def setKM(self, km):
        if km > self.__quilometragem:
            self.__quilometragem = km

    def __str__(self):
        txt = "modelo: " + self.modelo
        txt += "\nAno: " + str(self.ano)
        txt += "\nQuilometragem: " + str(self.__quilometragem)
        return txt

x = Carro("Doblo", 2025)
print(x)