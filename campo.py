from random import randrange

class Campo:
    def __init__(self) -> None:
        self._matriz = []

    def criaCampo(self):
        for i in range(5):
            linha = []
            for j in range(5):
                linha.append(0)
            self._matriz.append(linha)
        
        for x in range(5):
            bombaLinha = randrange(5)
            bombaColuna = randrange(5)
            self.adicionaBomba(bombaLinha, bombaColuna)

        return self._matriz

    def adicionaBomba(self, linha, coluna):
        self._matriz[linha][coluna] = 7

    def mostraCampo(self) -> str:
        for item in range(len(self._matriz)):
            print("{}".format(self._matriz[item]))
            

if __name__ == "__main__":
    x = Campo()
    x.criaCampo()
    print(x)
