# Heranca Simples
class Veiculo:
    def __init__(self, cor, placa,numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__ (self,cor, placa,numero_rodas ,carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado
        
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")


moto = Motocicleta("preta", "abc123", 2)
moto.ligar_motor()

carro = Carro("branco", "xxt002", 4)
carro.ligar_motor()

caminhao = Caminhao("vermelho", "mmg0210", 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)