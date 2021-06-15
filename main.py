import os
from random import randint
from functions import *

numero_de_jogadores = int(input('>>>>>>>> O JOGO DA VELHA 5000 <<<<<<<\n'
                                '\nQuantos Jogadores vão Jogar? [1/2] '))

if numero_de_jogadores == 2:
    while not verificação():
        os.system('cls')
        desenho_do_tabuleiro()
        if numjog % 2 == 1:
            jog = 1
        else:
            jog = 2

        if not jogada(str(input(f'Digite o numero da casa em que vai jogar, Jogador {jog}: '))):
            print('ERRO! Jogada inválida! Tente novamente.')
            numjog -= 1
        numjog += 1

    desenho_do_tabuleiro()
    if (numjog - 1) % 2 == 1:
        os.system('cls')
        print('FIM DE JOGO! Vitória do jogador 1!!!')
        vitjog += 1
    else:
        os.system('cls')
        print('FIM DE JOGO! Vitória do jogador 2!!!')
        vitcomp += 1
    input('PRESSIONE [ENTER] PARA SAIR')
elif numero_de_jogadores == 1:
    while resp != 'N':
        while not verificação():
            os.system('cls')
            desenho_do_tabuleiro()
            if numjog % 2 == 1:
                if not jogada(str(input(f'Digite o numero da casa em que vai jogar, Jogador: '))):
                    print('ERRO! Jogada inválida! Tente novamente.')
                    input('PRESSIONE [ENTER] PARA CONTINUAR')
                    numjog -= 1
                numjog += 1
            else:
                if numjog == 2:
                    if jogador[0] in '1379':
                        tabuleiro[1].remove('5')
                        tabuleiro[1].insert(1, 'O')
                    elif jogador[0] == '2':
                        tabuleiro[2].remove('7')
                        tabuleiro[2].insert(0, 'O')
                    elif jogador[0] == '4':
                        tabuleiro[2].remove('9')
                        tabuleiro[2].insert(2, 'O')
                    elif jogador[0] == '6':
                        tabuleiro[0].remove('1')
                        tabuleiro[0].insert(0, 'O')
                    elif jogador[0] == '8':
                        tabuleiro[0].remove('1')
                        tabuleiro[0].insert(1, 'O')
                    else:
                        tabuleiro[2].remove('7')
                        tabuleiro[2].insert(0, 'O')
                    numjog += 1

                elif numjog == 4:
                    if quase_lá(tabuleiro):
                        numjog += 1
                    elif jogador[0] in '1379':
                        if jogador[0] == '3' and jogador[1] == '7':
                            tabuleiro[1].remove('4')
                            tabuleiro[1].insert(0, 'O')
                        elif jogador[0] == '3' and jogador[1] == '8':
                            tabuleiro[2].remove('9')
                            tabuleiro[2].insert(2, 'O')
                        elif jogador[0] == '3' and jogador[1] == '4':
                            tabuleiro[0].remove('1')
                            tabuleiro[0].insert(0, 'O')

                        elif jogador[0] == '1' and jogador[1] == '9':
                            tabuleiro[1].remove('6')
                            tabuleiro[1].insert(2, 'O')
                        elif jogador[0] == '1' and jogador[1] == '8':
                            tabuleiro[2].remove('7')
                            tabuleiro[2].insert(0, 'O')
                        elif jogador[0] == '1' and jogador[1] == '6':
                            tabuleiro[1].remove('6')
                            tabuleiro[1].insert(2, 'O')

                        elif jogador[0] == '7' and jogador[1] == '3':
                            tabuleiro[1].remove('4')
                            tabuleiro[1].insert(0, 'O')
                        elif jogador[0] == '7' and jogador[1] == '2':
                            tabuleiro[0].remove('1')
                            tabuleiro[0].insert(0, 'O')
                        elif jogador[0] == '7' and jogador[1] == '6':
                            tabuleiro[2].remove('9')
                            tabuleiro[2].insert(2, 'O')

                        elif jogador[0] == '9' and jogador[1] == '1':
                            tabuleiro[1].remove('4')
                            tabuleiro[1].insert(0, 'O')
                        elif jogador[0] == '9' and jogador[1] == '2':
                            tabuleiro[0].remove('3')
                            tabuleiro[0].insert(2, 'O')
                        elif jogador[0] == '9' and jogador[1] == '4':
                            tabuleiro[2].remove('7')
                            tabuleiro[2].insert(0, 'O')
                        numjog += 1

                    elif jogador[0] == '2':
                        if jogador[1] == '4':
                            tabuleiro[2].remove('9')
                            tabuleiro[2].insert(2, 'O')
                        elif jogador[1] == '6':
                            tabuleiro[0].remove('1')
                            tabuleiro[0].insert(0, 'O')
                        elif jogador[1] == '9':
                            tabuleiro[0].remove('1')
                            tabuleiro[0].insert(0, 'O')
                        numjog += 1

                    elif jogador[0] == '4':
                        if jogador[1] == '8':
                            tabuleiro[0].remove('3')
                            tabuleiro[0].insert(2, 'O')
                        elif jogador[1] == '2':
                            tabuleiro[2].remove('7')
                            tabuleiro[2].insert(0, 'O')
                        elif jogador[1] == '3':
                            tabuleiro[2].remove('7')
                            tabuleiro[2].insert(0, 'O')
                        numjog += 1

                    elif jogador[0] == '6':
                        if jogador[1] == '2':
                            tabuleiro[2].remove('7')
                            tabuleiro[2].insert(0, 'O')
                        elif jogador[1] == '8':
                            tabuleiro[0].remove('3')
                            tabuleiro[0].insert(2, 'O')
                        elif jogador[1] == '7':
                            tabuleiro[0].remove('3')
                            tabuleiro[0].insert(2, 'O')
                        numjog += 1

                    elif jogador[0] == '8':
                        if jogador[1] == '6':
                            tabuleiro[0].remove('1')
                            tabuleiro[0].insert(0, 'O')
                        elif jogador[1] == '4':
                            tabuleiro[2].remove('9')
                            tabuleiro[2].insert(2, 'O')
                        elif jogador[1] == '1':
                            tabuleiro[2].remove('9')
                            tabuleiro[2].insert(2, 'O')
                        numjog += 1

                    elif jogador[0] == '5':
                        if jogador[1] == '3':
                            tabuleiro[2].remove('9')
                            tabuleiro[2].insert(2, 'O')
                        numjog += 1

                elif numjog > 4:
                    if quase_lá_cpu(tabuleiro):
                        numjog += 1
                    elif quase_lá(tabuleiro):
                        numjog += 1
                    elif empate():
                        numjog += 11
                        break
                    else:
                        while True:
                            if jogada_cpu(str(randint(1, 9))):
                                numjog += 1
                                break
        os.system('cls')
        desenho_do_tabuleiro()
        if numjog > 10:
            print('EMPATE!!!')
        elif (numjog - 1) % 2 == 1:
            print('FIM DE JOGO! Vitória do Jogador!!!')
            vitjog += 1
        elif (numjog - 1) % 2 == 0:
            print('FIM DE JOGO! Vitória do Computador!!!')
            vitcomp += 1
        resp = input('Deseja jogar novamente? [S/N] ').upper()
    os.system('cls')
    print(f'>>>>> FIM DE JOGO! <<<<<\n'
          f'\n|     PLACAR GERAL:    |\n'
          f'\nCOMPUTADOR: [{vitcomp:^3}]\n'
          f'JOGADOR:    [{vitjog:^3}]\n')
    input('\nPRESSIONE [ENTER] PARA SAIR')

else:
    print('ERRO! Numero Inválido. Tente novamente')
