class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"O {self.nome} foi comer...")

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def miar(self):
        print(f"O {self.nome} foi miando...")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def latir(self):
        print(f"O {self.nome} foi latindo")

class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def mugir(self):
        print(f"A {self.nome} foi mugir")

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def guinchar(self):
        print(f"O {self.nome} foi guinchar")

class Ingresso():
    def __init__(self, valor):
        self.valor = valor
    def imprimevalor(self):
        print(f"{self.valor}")

class Vip(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)
    def imprimavip(self):
        self.valor+=(self.valor*50/100)
        print(f"{self.valor}")

class Forma():
    def __init__(self, area, perimetro):
        self.area = area
        self.perimetro = perimetro

class Retangulo(Forma):
    def __init__(self, base, altura):
        super().__init__(base, altura)
        self.base=base
        self.altura=altura
    def calculaarea(self):
        self.calculaarea = (self.base * self.altura)
        print(f"A área do retângulo é {self.calculaarea}")
    def calculaperimetro(self):
        self.calculaperimetro = 2 * (self.base*self.altura)
        print(f"O perímetro do retângulo é {self.calculaperimetro}")












