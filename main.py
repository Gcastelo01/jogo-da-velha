import os
from random import randint
from functions import *

tabuleiro = Tabuleiro()

numero_de_jogadores = int(input('>>>>>>>> O JOGO DA VELHA 5000 <<<<<<<\n'
                                '\nQuantos Jogadores vão Jogar? [1/2] '))

if numero_de_jogadores == 2:
    while not tabuleiro.verificação():
        os.system('cls')
        tabuleiro.desenho_do_tabuleiro()
        if tabuleiro.numjog % 2 == 1:
            tabuleiro.jog = 1
        else:
            tabuleiro.jog = 2

        if not tabuleiro.jogada(str(input(f'Digite o numero da casa em que vai jogar, Jogador {tabuleiro.jog}: '))):
            print('ERRO! Jogada inválida! Tente novamente.')
            tabuleiro.numjog -= 1
        tabuleiro.numjog += 1

    tabuleiro.desenho_do_tabuleiro()
    if (tabuleiro.numjog - 1) % 2 == 1:
        os.system('cls')
        print('FIM DE JOGO! Vitória do jogador 1!!!')
        tabuleiro.vitjog += 1
    else:
        os.system('cls')
        print('FIM DE JOGO! Vitória do jogador 2!!!')
        tabuleiro.vitcomp += 1
    input('PRESSIONE [ENTER] PARA SAIR')
elif numero_de_jogadores == 1:
    while tabuleiro.resp != 'N':
        while not tabuleiro.verificação():
            os.system('cls')
            tabuleiro.desenho_do_tabuleiro()
            if tabuleiro.numjog % 2 == 1:
                if not tabuleiro.jogada(str(input(f'Digite o numero da casa em que vai jogar, Jogador: '))):
                    print('ERRO! Jogada inválida! Tente novamente.')
                    input('PRESSIONE [ENTER] PARA CONTINUAR')
                    tabuleiro.numjog -= 1
                tabuleiro.numjog += 1
            else:
                if tabuleiro.numjog == 2:
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
                    tabuleiro.numjog += 1

                elif tabuleiro.numjog == 4:
                    if tabuleiro.quase_lá():
                        tabuleiro.numjog += 1
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
                        tabuleiro.numjog += 1

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
                        tabuleiro.numjog += 1

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
                        tabuleiro.numjog += 1

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
                        tabuleiro.numjog += 1

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
                        tabuleiro.numjog += 1

                    elif tabuleiro.jogador[0] == '5':
                        if tabuleiro.jogador[1] == '3':
                            tabuleiro.tabuleiro[2].remove('9')
                            tabuleiro.tabuleiro[2].insert(2, 'O')
                        tabuleiro.numjog += 1

                elif tabuleiro.numjog > 4:
                    if tabuleiro.quase_lá_cpu():
                        tabuleiro.numjog += 1
                    elif tabuleiro.quase_lá():
                        tabuleiro.numjog += 1
                    elif tabuleiro.empate():
                        tabuleiro.numjog += 11
                        break
                    else:
                        while True:
                            if tabuleiro.jogada_cpu(str(randint(1, 9))):
                                tabuleiro.numjog += 1
                                break
        os.system('cls')
        tabuleiro.desenho_do_tabuleiro()
        if tabuleiro.numjog > 10:
            print('EMPATE!!!')
        elif (tabuleiro.numjog - 1) % 2 == 1:
            print('FIM DE JOGO! Vitória do Jogador!!!')
            tabuleiro.vitjog += 1
        elif (tabuleiro.numjog - 1) % 2 == 0:
            print('FIM DE JOGO! Vitória do Computador!!!')
            tabuleiro.vitcomp += 1
        tabuleiro.resp = input('Deseja jogar novamente? [S/N] ').upper()
        tabuleiro.resetar_tabuleiro()

    os.system('cls')
    print(f'>>>>> FIM DE JOGO! <<<<<\n'
          f'\n|     PLACAR GERAL:    |\n'
          f'\nCOMPUTADOR: [{tabuleiro.vitcomp:^3}]\n'
          f'JOGADOR:    [{tabuleiro.vitjog:^3}]\n')
    input('\nPRESSIONE [ENTER] PARA SAIR')

else:
    print('ERRO! Numero Inválido. Tente novamente')
