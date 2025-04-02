from Cidade import Cidade

class Pessoa:
    def __init__(self, nome, cpf = None, cid = Cidade("Porto Alegre")):
        self.id = nome
        self.nome = nome
        self.cpf = cpf
        self.cidade = cid

        def __str__(self):
            txt = "Pessoa: " + self.nome
            txt += "\nCPF: " + str(self.cpf)
            txt += "\nCidade: " + str(self.cid)
            return txt
