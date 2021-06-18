#TODO otimizar algoritmos de jogadas do computador (prioridade disso é baixa. As respostas são rápidas o suficiente).

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
                tabuleiro.jogada_incorreta()

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

    while tabuleiro.get_resposta() != 'N':

        while not tabuleiro.verificação():
            tabuleiro.limpa_tela()
            tabuleiro.desenho_do_tabuleiro()

            if tabuleiro.get_numero_jogada() % 2 == 1:
                if not tabuleiro.jogada(str(input(f'Digite o numero da casa em que vai jogar, Jogador: '))):
                    tabuleiro.jogada_incorreta()

                tabuleiro.increase_numero_jogada()
                
            else:
                if tabuleiro.get_numero_jogada() == 2:
                    if tabuleiro.get_jogada(0) in '1379':
                        tabuleiro.jogar_no_tabuleiro(1, '5', 'O', 1)
                        
                    elif tabuleiro.get_jogada(0) == '2':
                        tabuleiro.jogar_no_tabuleiro(2, '7', 'O', 0)

                    elif tabuleiro.get_jogada(0) == '4':
                        tabuleiro.jogar_no_tabuleiro(2, '9', 'O', 2)

                    elif tabuleiro.get_jogada(0) == '6':
                        tabuleiro.jogar_no_tabuleiro(0, '1', 'O', 0)

                    elif tabuleiro.get_jogada(0) == '8':
                        tabuleiro.jogar_no_tabuleiro(0, '1', 'O', 1)

                    else:
                        tabuleiro.jogar_no_tabuleiro(2, '7', 'O', 0)

                    tabuleiro.increase_numero_jogada()

                elif tabuleiro.get_numero_jogada() == 4:
                    if tabuleiro.quase_lá():
                        tabuleiro.increase_numero_jogada()

                    elif tabuleiro.get_jogada(0) in '1379':
                        if tabuleiro.get_jogada(0) == '3' and tabuleiro.get_jogada(1) == '7':
                            tabuleiro.jogar_no_tabuleiro(1, '4', 'O', 0)

                        elif tabuleiro.get_jogada(0) == '3' and tabuleiro.get_jogada(1) == '8':
                            tabuleiro.jogar_no_tabuleiro(2, '9', 'O', 2)

                        elif tabuleiro.get_jogada(0) == '3' and tabuleiro.get_jogada(1) == '4':
                            tabuleiro.jogar_no_tabuleiro(0, '1', 'O', 0)

                        elif tabuleiro.get_jogada(0) == '1' and tabuleiro.get_jogada(1) == '9':
                            tabuleiro.jogar_no_tabuleiro(1, '6', 'O', 2)

                        elif tabuleiro.get_jogada(0) == '1' and tabuleiro.get_jogada(1) == '8':
                            tabuleiro.jogar_no_tabuleiro(2, '7', 'O', 0)

                        elif tabuleiro.get_jogada(0) == '1' and tabuleiro.get_jogada(1) == '6':
                            tabuleiro.jogar_no_tabuleiro(1, '6', 'O', 2)

                        elif tabuleiro.get_jogada(0) == '7' and tabuleiro.get_jogada(1) == '3':
                            tabuleiro.jogar_no_tabuleiro(1, '4', 'O', 0)

                        elif tabuleiro.get_jogada(0) == '7' and tabuleiro.get_jogada(1) == '2':
                            tabuleiro.jogar_no_tabuleiro(0, '1', 'O', 0)

                        elif tabuleiro.get_jogada(0) == '7' and tabuleiro.get_jogada(1) == '6':
                            tabuleiro.jogar_no_tabuleiro(2, '9', 'O', 2)

                        elif tabuleiro.get_jogada(0) == '9' and tabuleiro.get_jogada(1) == '1':
                            tabuleiro.jogar_no_tabuleiro(1, '4', 'O', 0)

                        elif tabuleiro.get_jogada(0) == '9' and tabuleiro.get_jogada(1) == '2':
                            tabuleiro.jogar_no_tabuleiro(0, '3', 'O', 2)

                        elif tabuleiro.get_jogada(0) == '9' and tabuleiro.get_jogada(1) == '4':
                            tabuleiro.jogar_no_tabuleiro(2, '7', 'O', 0)

                        tabuleiro.increase_numero_jogada()

                    elif tabuleiro.get_jogada(0) == '2':
                        if tabuleiro.get_jogada(1) == '4':
                            tabuleiro.jogar_no_tabuleiro(2, '9', 'O', 2)

                        elif tabuleiro.get_jogada(1) == '6':
                            tabuleiro.jogar_no_tabuleiro(0, '1', 'O', 0)

                        elif tabuleiro.get_jogada(1) == '9':
                            tabuleiro.jogar_no_tabuleiro(0, '1', 'O', 0)

                        tabuleiro.increase_numero_jogada()

                    elif tabuleiro.get_jogada(0) == '4':
                        if tabuleiro.get_jogada(1) == '8':
                            tabuleiro.jogar_no_tabuleiro(0, '3', 'O', 2)

                        elif tabuleiro.get_jogada(1) == '2':
                            tabuleiro.jogar_no_tabuleiro(2, '7', 'O', 0)

                        elif tabuleiro.get_jogada(1) == '3':
                            tabuleiro.jogar_no_tabuleiro(2, '7', 'O', 0)

                        tabuleiro.increase_numero_jogada()

                    elif tabuleiro.get_jogada(0) == '6':
                        if tabuleiro.get_jogada(1) == '2':
                            tabuleiro.jogar_no_tabuleiro(2, '7', 'O', 0)

                        elif tabuleiro.get_jogada(1) == '8':
                            tabuleiro.jogar_no_tabuleiro(0, '3', 'O', 2)

                        elif tabuleiro.get_jogada(1) == '7':
                            tabuleiro.jogar_no_tabuleiro(0, '3', 'O', 2)

                        tabuleiro.increase_numero_jogada()

                    elif tabuleiro.get_jogada(0) == '8':
                        if tabuleiro.get_jogada(1) == '6':
                            tabuleiro.jogar_no_tabuleiro(0, '1', 'O', 0)

                        elif tabuleiro.get_jogada(1) == '4':
                            tabuleiro.jogar_no_tabuleiro(2, '9', 'O', 2)

                        elif tabuleiro.get_jogada(1) == '1':
                            tabuleiro.jogar_no_tabuleiro(2, '9', 'O', 2)

                        tabuleiro.increase_numero_jogada()

                    elif tabuleiro.get_jogada(0) == '5':
                        if tabuleiro.get_jogada(1) == '3':
                            tabuleiro.jogar_no_tabuleiro(2, '9', 'O', 2)

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

        if tabuleiro.get_numero_jogada() == 10:
            print('EMPATE!!!')

        elif (tabuleiro.get_numero_jogada() - 1) % 2 == 1:
            print('FIM DE JOGO! Vitória do Jogador!!!')
            tabuleiro.increase_vit_jogador()

        elif (tabuleiro.get_numero_jogada() - 1) % 2 == 0:
            print('FIM DE JOGO! Vitória do Computador!!!')
            tabuleiro.increase_vit_cpu()

        tabuleiro.set_resposta()
        tabuleiro.resetar_tabuleiro()

    tabuleiro.limpa_tela()
    tabuleiro.tela_do_final_cpu()
    
else:
    print('ERRO! Numero Inválido. Tente novamente')
