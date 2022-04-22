from campo import *
from fila import *

class Jogo:
    def __init__(self, pontoX, pontoY) -> None:
        self._pontoX = pontoX
        self._pontoY = pontoY
    
    def verificaAoRedor(self, campo):
        fila = Fila()
        count = 0
        if campo[self._pontoY + 1][self._pontoX] == 7:
            count += 1
        
        campo[self._pontoY][self._pontoX + 1]
        campo[self._pontoY - 1][self._pontoX]
        campo[self._pontoY][self._pontoX - 1]


    def verificaPontos(self, campo):
        if self._pontoY == 0:
            print("Não existe ponto acima")
        if (campo[self._pontoY][self._pontoX]) == 7:
            print("Você perdeu!")
            