class Animal:
    def comer(self):
        print("O animal esta comendo")

    def andar(self):
            print("O animal esta andando na jaula")


class Felino(Animal):
    def lamber(self):
        print("O felino esta lambendo seu pelo")


class Leao(Felino):
     def rugir(self):
          print("O leão esta rugindo")


class Pessoa:
     def observa(self, animal:Animal):
          animal.comer()