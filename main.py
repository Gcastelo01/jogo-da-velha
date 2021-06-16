import os
from random import randint
from functions import *

tabuleiro = Tabuleiro()

tabuleiro.limpa_tela()
tabuleiro.set_jogadores()

if tabuleiro.get_jogadores() == 2:
    while tabuleiro.get_resposta() != 'N':

        while not tabuleiro.verificação():

            tabuleiro.limpa_tela()
            tabuleiro.desenho_do_tabuleiro()

            if tabuleiro.get_numero_jogada() % 2 == 1:
                jogador = 1

            else:
                jogador = 2

            if not tabuleiro.jogada(str(input(f'Digite o numero da casa em que vai jogar, Jogador {jogador}: '))):
                print('ERRO! Jogada inválida! Tente novamente.')
                tabuleiro.decrease_numero_jogada()

            tabuleiro.increase_numero_jogada()

        tabuleiro.limpa_tela()

        tabuleiro.desenho_do_tabuleiro()
        if (tabuleiro.get_numero_jogada() - 1) % 2 == 1:
            print('FIM DE JOGO! Vitória do jogador 1!!!')
            tabuleiro.increase_vit_jogador()

        else:
            print('FIM DE JOGO! Vitória do jogador 2!!!')
            tabuleiro.increase_vit_cpu()

        tabuleiro.set_resposta()
        tabuleiro.resetar_tabuleiro()
        
    tabuleiro.limpa_tela()
    tabuleiro.tela_do_final_jog()
      
elif tabuleiro.get_jogadores() == 1:

    while tabuleiro.resp != 'N':

        while not tabuleiro.verificação():
            tabuleiro.limpa_tela()
            tabuleiro.desenho_do_tabuleiro()

            if tabuleiro.get_numero_jogada() % 2 == 1:
                if not tabuleiro.jogada(str(input(f'Digite o numero da casa em que vai jogar, Jogador: '))):
                    print('ERRO! Jogada inválida! Tente novamente.')
                    input('PRESSIONE [ENTER] PARA CONTINUAR')
                    tabuleiro.decrease_numero_jogada()

                tabuleiro.increase_numero_jogada()
            else:
                if tabuleiro.get_numero_jogada() == 2:
                    if tabuleiro.jogador[0] in '1379':
                        tabuleiro.tabuleiro[1].remove('5')
                        tabuleiro.tabuleiro[1].insert(1, 'O')
                    elif tabuleiro.jogador[0] == '2':
                        tabuleiro.tabuleiro[2].remove('7')
                        tabuleiro.tabuleiro[2].insert(0, 'O')
                    elif tabuleiro.jogador[0] == '4':
                        tabuleiro.tabuleiro[2].remove('9')
                        tabuleiro.tabuleiro[2].insert(2, 'O')
                    elif tabuleiro.jogador[0] == '6':
                        tabuleiro.tabuleiro[0].remove('1')
                        tabuleiro.tabuleiro[0].insert(0, 'O')
                    elif tabuleiro.jogador[0] == '8':
                        tabuleiro.tabuleiro[0].remove('1')
                        tabuleiro.tabuleiro[0].insert(1, 'O')
                    else:
                        tabuleiro.tabuleiro[2].remove('7')
                        tabuleiro.tabuleiro[2].insert(0, 'O')
                    tabuleiro.increase_numero_jogada()

                elif tabuleiro.get_numero_jogada() == 4:
                    if tabuleiro.quase_lá():
                        tabuleiro.increase_numero_jogada()
                    elif tabuleiro.jogador[0] in '1379':
                        if tabuleiro.jogador[0] == '3' and tabuleiro.jogador[1] == '7':
                            tabuleiro.tabuleiro[1].remove('4')
                            tabuleiro.tabuleiro[1].insert(0, 'O')
                        elif tabuleiro.jogador[0] == '3' and tabuleiro.jogador[1] == '8':
                            tabuleiro.tabuleiro[2].remove('9')
                            tabuleiro.tabuleiro[2].insert(2, 'O')
                        elif tabuleiro.jogador[0] == '3' and tabuleiro.jogador[1] == '4':
                            tabuleiro.tabuleiro[0].remove('1')
                            tabuleiro.tabuleiro[0].insert(0, 'O')

                        elif tabuleiro.jogador[0] == '1' and tabuleiro.jogador[1] == '9':
                            tabuleiro.tabuleiro[1].remove('6')
                            tabuleiro.tabuleiro[1].insert(2, 'O')
                        elif tabuleiro.jogador[0] == '1' and tabuleiro.jogador[1] == '8':
                            tabuleiro.tabuleiro[2].remove('7')
                            tabuleiro.tabuleiro[2].insert(0, 'O')
                        elif tabuleiro.jogador[0] == '1' and tabuleiro.jogador[1] == '6':
                            tabuleiro.tabuleiro[1].remove('6')
                            tabuleiro.tabuleiro[1].insert(2, 'O')

                        elif tabuleiro.jogador[0] == '7' and tabuleiro.jogador[1] == '3':
                            tabuleiro.tabuleiro[1].remove('4')
                            tabuleiro.tabuleiro[1].insert(0, 'O')
                        elif tabuleiro.jogador[0] == '7' and tabuleiro.jogador[1] == '2':
                            tabuleiro.tabuleiro[0].remove('1')
                            tabuleiro.tabuleiro[0].insert(0, 'O')
                        elif tabuleiro.jogador[0] == '7' and tabuleiro.jogador[1] == '6':
                            tabuleiro.tabuleiro[2].remove('9')
                            tabuleiro.tabuleiro[2].insert(2, 'O')

                        elif tabuleiro.jogador[0] == '9' and tabuleiro.jogador[1] == '1':
                            tabuleiro.tabuleiro[1].remove('4')
                            tabuleiro.tabuleiro[1].insert(0, 'O')
                        elif tabuleiro.jogador[0] == '9' and tabuleiro.jogador[1] == '2':
                            tabuleiro.tabuleiro[0].remove('3')
                            tabuleiro.tabuleiro[0].insert(2, 'O')
                        elif tabuleiro.jogador[0] == '9' and tabuleiro.jogador[1] == '4':
                            tabuleiro.tabuleiro[2].remove('7')
                            tabuleiro.tabuleiro[2].insert(0, 'O')
                        tabuleiro.increase_numero_jogada()

                    elif tabuleiro.jogador[0] == '2':
                        if tabuleiro.jogador[1] == '4':
                            tabuleiro.tabuleiro[2].remove('9')
                            tabuleiro.tabuleiro[2].insert(2, 'O')
                        elif tabuleiro.jogador[1] == '6':
                            tabuleiro.tabuleiro[0].remove('1')
                            tabuleiro.tabuleiro[0].insert(0, 'O')
                        elif tabuleiro.jogador[1] == '9':
                            tabuleiro.tabuleiro[0].remove('1')
                            tabuleiro.tabuleiro[0].insert(0, 'O')
                        tabuleiro.increase_numero_jogada()

                    elif tabuleiro.jogador[0] == '4':
                        if tabuleiro.jogador[1] == '8':
                            tabuleiro.tabuleiro[0].remove('3')
                            tabuleiro.abuleiro[0].insert(2, 'O')
                        elif tabuleiro.jogador[1] == '2':
                            tabuleiro.tabuleiro[2].remove('7')
                            tabuleiro.tabuleiro[2].insert(0, 'O')
                        elif tabuleiro.jogador[1] == '3':
                            tabuleiro.tabuleiro[2].remove('7')
                            tabuleiro.tabuleiro[2].insert(0, 'O')
                        tabuleiro.increase_numero_jogada()

                    elif tabuleiro.jogador[0] == '6':
                        if tabuleiro.jogador[1] == '2':
                            tabuleiro.tabuleiro[2].remove('7')
                            tabuleiro.tabuleiro[2].insert(0, 'O')
                        elif tabuleiro.jogador[1] == '8':
                            tabuleiro.tabuleiro[0].remove('3')
                            tabuleiro.tabuleiro[0].insert(2, 'O')
                        elif tabuleiro.jogador[1] == '7':
                            tabuleiro.tabuleiro[0].remove('3')
                            tabuleiro.tabuleiro[0].insert(2, 'O')
                        tabuleiro.increase_numero_jogada()

                    elif tabuleiro.jogador[0] == '8':
                        if tabuleiro.jogador[1] == '6':
                            tabuleiro.tabuleiro[0].remove('1')
                            tabuleiro.tabuleiro[0].insert(0, 'O')
                        elif tabuleiro.jogador[1] == '4':
                            tabuleiro.tabuleiro[2].remove('9')
                            tabuleiro.tabuleiro[2].insert(2, 'O')
                        elif tabuleiro.jogador[1] == '1':
                            tabuleiro.tabuleiro[2].remove('9')
                            tabuleiro.tabuleiro[2].insert(2, 'O')
                        tabuleiro.increase_numero_jogada()

                    elif tabuleiro.jogador[0] == '5':
                        if tabuleiro.jogador[1] == '3':
                            tabuleiro.tabuleiro[2].remove('9')
                            tabuleiro.tabuleiro[2].insert(2, 'O')
                        tabuleiro.increase_numero_jogada()

                elif tabuleiro.get_numero_jogada() > 4:
                    if tabuleiro.quase_lá_cpu():
                        tabuleiro.increase_numero_jogada()
                    elif tabuleiro.quase_lá():
                        tabuleiro.increase_numero_jogada()
                    elif tabuleiro.empate():
                        tabuleiro.get_numero_jogada() 
                        break
                    else:
                        while True:
                            if tabuleiro.jogada_cpu(str(randint(1, 9))):
                                tabuleiro.increase_numero_jogada()
                                break

        tabuleiro.limpa_tela()
        tabuleiro.desenho_do_tabuleiro()

        if tabuleiro.get_numero_jogada() > 10:
            print('EMPATE!!!')

        elif (tabuleiro.get_numero_jogada() - 1) % 2 == 1:
            print('FIM DE JOGO! Vitória do Jogador!!!')
            tabuleiro.increase_vit_jogador()

        elif (tabuleiro.get_numero_jogada() - 1) % 2 == 0:
            print('FIM DE JOGO! Vitória do Computador!!!')
            tabuleiro.increase_vit_cpu()

        tabuleiro.resp = input('Deseja jogar novamente? [S/N] ').upper()
        tabuleiro.resetar_tabuleiro()

    tabuleiro.limpa_tela()
    tabuleiro.tela_do_final_cpu()
else:
    print('ERRO! Numero Inválido. Tente novamente')
