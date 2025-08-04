from abc import ABC, abstractmethod


class Pessoa(ABC):
    def correr(self):
        print ("Correndo")

    @abstractmethod
    def trabalhar(self):
        pass

class Professor(Pessoa):
    def trabalhar(self):
        print ("Professor trabalhando")


p1 =Professor()
p1.correr()