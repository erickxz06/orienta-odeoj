class Pessoa():
    def __init__(self, nome, idade, peso):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.comendo=False
        self.falando=False
        self.dormindo=False

    def falar(self):
        print(f" {self.nome} começou a falar")
    def dormir(self):
        print(f"  começou a dormir")
    def comer(self, comida):
        if self.comendo==True
            print("Não pode comer, pois já está comendo")
            print(f"Foi comer {comida}")




