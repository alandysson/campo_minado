from jogo import *
from campo import *


def menu():
    print("=*= Campo Minado =*=")
    tamanhoCampo = int(input("Digite o tamanho do campo: "))
    bombas = int(input("Quantidade de bombas: "))

    if bombas > tamanhoCampo:
        return print('\nNumero de bombas nao pode ser maior que o campo!')
    jogo = Campo(tamanhoCampo, bombas)
    campo = jogo.criaCampo()
    jogador = jogo.criaCampoJogador()
    operacao = Jogo(tamanhoCampo)
    while True:
        if operacao.checarVitoria(jogador) == False:
            print(jogo.mostraCampoJogador())
            pontoX = int(input("linha: "))
            pontoY = int(input("coluna: "))
            operacao.verificaJogada(pontoX, pontoY, campo, jogador)
            jogo.mostraCampo()
            if campo[pontoY][pontoX] == 'X':
                jogo.mostraCampo()
                break


menu()
