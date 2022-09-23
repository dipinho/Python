class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor  #self é o this do Python
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = 1

    #criando métodos
    def buzinar(self):
        print("plim plim\n")

    def parar(self):
        print("Parando a bicicleta...")
        print("Bicicleta parada!\n")

    def correr(self):
        print("CorrendoooOoOooooooo!\n")

    def __str__(self):
        return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"

    def trocar_marcha(self, nro_marcha):
        print("Trocando a marcha...\n")

        def _trocar_marcha():
            if nro_marcha > self.marcha:
                print("Marcha trocada\n")
            else:
                print("Não foi possivel trocar a marcha")


#criando a estancia
bike1 = Bicicleta("Vermelha", "bmx", 2020, 1000)
bike2 = Bicicleta("Preta", "monark", 2017, 689)


bike2.parar()

bike2.trocar_marcha()
bike2.correr()