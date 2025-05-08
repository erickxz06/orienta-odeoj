class Pessoa():
    def __init__(self, nome, idade, peso):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.comendo=False
        self.falando=False
        self.dormindo=False

    def dormir(self):
        if self.dormindo==True:
            print("Já está dormindo")
        elif self.comendo==True:
            print("Não pode dormir, pois está comendo")
        elif self.falando==True:
            print("Não pode dormir, pois está falando")
        else:
            print("Foi dormir")
            self.dormindo=True
    def acordar(self):
        if self.dormindo==True:
            print("Acordou")
            self.dormindo=False
        else:
            print("Já está acordado")

    def falar(self):
        if self.falando==True:
            print("Já está falando")
        elif self.comendo==True:
            print("Não pode falar, pois está comendo")
        elif self.dormindo==True:
            print("Não pode falar, pois está dormindo")
        else:
            print("Começou a falar")
            self.falando=True
    def paroudefalar(self):
        if self.falando==True:
            print("Parou de falar")
            self.falando=False
        else:
            print("Já parou de falar")

    def comer(self):
        if self.comendo==True:
            print(f"Já está comendo")
        elif self.dormindo==True:
            print(f"Não pode comer, pois está dormindo")
        elif self.falando==True:
            print(f"Não pode comer, pois está falando")
        else:
            print("Começou a comer")
            self.comendo=True
    def paroudecomer(self):
        if self.comendo()==True:
            print("parou de comer")
            self.comendo=False
        else:
            print("Já parou de comer")











