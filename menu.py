from jogo import *
from campo import *

def menu():
  return print(
    """
    --- Campo Minado ---

    Digite o Ponto desejado: 

    ---------------------
    """
  )
matriz = Campo()
campo = matriz.criaCampo()
print(matriz.mostraCampo())
menu()
pontoX = int(input("linha: "))
pontoY = int(input("coluna: "))
operacao = Jogo(pontoX, pontoY)
operacao.verificaPontos(campo)