from sys import platform
from os import system
import sys



class Tabuleiro:
    def __init__(self) -> None:
        self.__tabuleiro = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        self.__resultado = ''
        self.__numjog = 1
        self.__jogador = list()
        self.__vitjog = 0
        self.__vitcomp = 0
        self.__resp = ''
        self.__numero_de_jogadores = 0

    
    @staticmethod
    def limpa_tela():
        if platform == 'linux' or platform == 'linux2':
            system('clear')

        else:
            system('cls')

        pass


    def jogada_incorreta(self):
        print('ERRO! Jogada inválida! Tente novamente.')
        input('PRESSIONE [ENTER] PARA CONTINUAR')
        self.decrease_numero_jogada()
        pass


    def jogar_no_tabuleiro(self, posicao: int, remover: str, inserir: str, posicao_inserir: int):
        if (posicao_inserir == posicao):
            self.__tabuleiro[posicao].remove(remover)
            self.__tabuleiro[posicao].insert(posicao, inserir)

        else:
            self.__tabuleiro[posicao].remove(remover)
            self.__tabuleiro[posicao].insert(posicao_inserir, inserir)
        



    def increase_vit_cpu(self):
        self.__vitcomp += 1


    def increase_vit_jogador(self):
        self.__vitjog += 1


    def increase_numero_jogada(self):
        self.__numjog += 1



    def decrease_numero_jogada(self):
        self.__numjog -= 1


    def set_jogadores(self):
        self.__numero_de_jogadores = int(input('>>>>>>>> O JOGO DA VELHA 5000 <<<<<<<\n'
                                '\nQuantos Jogadores vão Jogar? [1/2] '))


    def set_resposta(self):
        self.__resp = input('Deseja jogar novamente? [S/N] ').upper()


    def get_jogada(self, jogada):
        return self.__jogador[jogada]


    def get_jogadores(self):
        return self.__numero_de_jogadores


    def get_resposta(self):
        return self.__resp


    def get_numero_jogada(self):
        return self.__numjog


    def tela_do_final_cpu(self):
        print(f'>>>>> FIM DE JOGO! <<<<<\n'
        f'\n|     PLACAR GERAL:    |\n'
        f'\nCOMPUTADOR: [{self.__vitcomp:^3}]\n'
        f'JOGADOR:    [{self.__vitjog:^3}]\n')
        input('\nPRESSIONE [ENTER] PARA SAIR')


    def tela_do_final_jog(self):
        print(f'>>>>> FIM DE JOGO! <<<<<\n'
        f'\n|     PLACAR GERAL:    |\n'
        f'\nJOGADOR 1:  [{self.__vitjog:^3}]\n'
        f'JOGADOR 2:  [{self.__vitcomp:^3}]\n')
        input('\nPRESSIONE [ENTER] PARA SAIR')
        self.limpa_tela()


    def resetar_tabuleiro(self) -> None:
        self.__tabuleiro = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        self.__numjog = 1
        


    def desenho_do_tabuleiro(self):
        print(f'\n| O JOGO DA VELHA |\n'
            f'\nPlacar: {self.__vitjog} X {self.__vitcomp}\n')
        print(f' {self.__tabuleiro[0][0]} | {self.__tabuleiro[0][1]} | {self.__tabuleiro[0][2]}\n'
            f'---+---+---\n'
            f' {self.__tabuleiro[1][0]} | {self.__tabuleiro[1][1]} | {self.__tabuleiro[1][2]}\n'
            f'---+---+---\n'
            f' {self.__tabuleiro[2][0]} | {self.__tabuleiro[2][1]} | {self.__tabuleiro[2][2]}\n')


    def vertical(self):
        if self.__tabuleiro[0][0] == 'X' and self.__tabuleiro[1][0] == 'X' and self.__tabuleiro[2][0] == 'X':
            return True
        elif self.__tabuleiro[0][1] == 'X' and self.__tabuleiro[1][1] == 'X' and self.__tabuleiro[2][1] == 'X':
            return True
        elif self.__tabuleiro[0][2] == 'X' and self.__tabuleiro[1][2] == 'X' and self.__tabuleiro[2][2] == 'X':
            return True
        elif self.__tabuleiro[0][0] == 'O' and self.__tabuleiro[1][0] == 'O' and self.__tabuleiro[2][0] == 'O':
            return True
        elif self.__tabuleiro[0][1] == 'O' and self.__tabuleiro[1][1] == 'O' and self.__tabuleiro[2][1] == 'O':
            return True
        elif self.__tabuleiro[0][2] == 'O' and self.__tabuleiro[1][2] == 'O' and self.__tabuleiro[2][2] == 'O':
            return True
        else:
            return False


    def horizontal(self):
        if self.__tabuleiro[0][0] == 'X' and self.__tabuleiro[0][1] == 'X' and self.__tabuleiro[0][2] == 'X':
            return True
        elif self.__tabuleiro[1][0] == 'X' and self.__tabuleiro[1][1] == 'X' and self.__tabuleiro[1][2] == 'X':
            return True
        elif self.__tabuleiro[2][0] == 'X' and self.__tabuleiro[2][1] == 'X' and self.__tabuleiro[2][2] == 'X':
            return True
        elif self.__tabuleiro[0][0] == 'O' and self.__tabuleiro[0][1] == 'O' and self.__tabuleiro[0][2] == 'O':
            return True
        elif self.__tabuleiro[1][0] == 'O' and self.__tabuleiro[1][1] == 'O' and self.__tabuleiro[1][2] == 'O':
            return True
        elif self.__tabuleiro[2][0] == 'O' and self.__tabuleiro[2][1] == 'O' and self.__tabuleiro[2][2] == 'O':
            return True
        else:
            return False


    def diagonal(self):
        if self.__tabuleiro[0][0] == 'X' and self.__tabuleiro[1][1] == 'X' and self.__tabuleiro[2][2] == 'X':
            return True
        elif self.__tabuleiro[0][2] == 'X' and self.__tabuleiro[1][1] == 'X' and self.__tabuleiro[2][0] == 'X':
            return True
        elif self.__tabuleiro[0][0] == 'O' and self.__tabuleiro[1][1] == 'O' and self.__tabuleiro[2][2] == 'O':
            return True
        elif self.__tabuleiro[0][2] == 'O' and self.__tabuleiro[1][1] == 'O' and self.__tabuleiro[2][0] == 'O':
            return True
        else:
            return False


    def empate(self):
        for v in self.__tabuleiro:
            for c in v:
                if c.isnumeric():
                    return False
        else:
            return True


    def verificação(self):
        if self.vertical():
            return True
        elif self.horizontal():
            return True
        elif self.diagonal():
            return True
        else:
            return False


    def jogada(self, x):
        for c in self.__tabuleiro:
            for pos, d in enumerate(c):
                if d.isnumeric() and d == x and self.__numjog % 2 == 1:
                    self.__jogador.append(d)
                    c.remove(d)
                    c.insert(pos, 'X')
                    return True
                elif d.isnumeric() and d == x and self.__numjog % 2 == 0:
                    c.remove(d)
                    c.insert(pos, 'O')
                    return True
        else:
            return False


    def quase_lá_cpu(self):
        if self.__tabuleiro[0][0] == 'O' and self.__tabuleiro[0][2] == 'O' and self.__tabuleiro[0][1] != 'X':
            self.__tabuleiro[0].remove('2')
            self.__tabuleiro[0].insert(1, 'O')
            return True

        elif self.__tabuleiro[0][0] == 'O' and self.__tabuleiro[2][0] == 'O' and self.__tabuleiro[1][0] != 'X':
            self.__tabuleiro[1].remove('4')
            self.__tabuleiro[1].insert(0, 'O')
            return True

        elif self.__tabuleiro[0][0] == 'O' and self.__tabuleiro[2][2] == 'O' and self.__tabuleiro[1][1] != 'X':
            self.__tabuleiro[1].remove('5')
            self.__tabuleiro[1].insert(1, 'O')
            return True

        elif self.__tabuleiro[0][1] == 'O' and self.__tabuleiro[2][1] == 'O' and self.__tabuleiro[1][1] != 'X':
            self.__tabuleiro[1].remove('5')
            self.__tabuleiro[1].insert(1, 'O')
            return True

        elif self.__tabuleiro[1][0] == 'O' and self.__tabuleiro[2][0] == 'O' and self.__tabuleiro[0][0] != 'X':
            self.__tabuleiro[0].remove('1')
            self.__tabuleiro[0].insert(0, 'O')
            return True

        elif self.__tabuleiro[0][2] == 'O' and self.__tabuleiro[2][2] == 'O' and self.__tabuleiro[1][2] != 'X':
            self.__tabuleiro[1].remove('6')
            self.__tabuleiro[1].insert(2, 'O')
            return True

        elif self.__tabuleiro[0][2] == 'O' and self.__tabuleiro[2][0] == 'O' and self.__tabuleiro[1][1] != 'X':
            self.__tabuleiro[1].remove('5')
            self.__tabuleiro[1].insert(1, 'O')
            return True

        elif self.__tabuleiro[1][0] == 'O' and self.__tabuleiro[1][2] == 'O' and self.__tabuleiro[1][1] != 'X':
            self.__tabuleiro[1].remove('5')
            self.__tabuleiro[1].insert(1, 'O')
            return True

        elif self.__tabuleiro[2][0] == 'O' and self.__tabuleiro[2][2] == 'O' and self.__tabuleiro[2][1] != 'X':
            self.__tabuleiro[2].remove('8')
            self.__tabuleiro[2].insert(1, 'O')
            return True

        elif self.__tabuleiro[0][0] == 'O' and self.__tabuleiro[1][0] == 'O' and self.__tabuleiro[2][0] != 'X':
            self.__tabuleiro[2].remove('7')
            self.__tabuleiro[2].insert(0, 'O')
            return True

        elif self.__tabuleiro[1][0] == 'O' and self.__tabuleiro[2][0] == 'O' and self.__tabuleiro[0][0] != 'X':
            self.__tabuleiro[0].remove('1')
            self.__tabuleiro[0].insert(0, 'O')
            return True

        elif self.__tabuleiro[0][0] == 'O' and self.__tabuleiro[1][1] == 'O' and self.__tabuleiro[2][2] != 'X':
            self.__tabuleiro[2].remove('9')
            self.__tabuleiro[2].insert(2, 'O')
            return True

        elif self.__tabuleiro[1][1] == 'O' and self.__tabuleiro[2][2] == 'O' and self.__tabuleiro[0][0] != 'X':
            self.__tabuleiro[0].remove('1')
            self.__tabuleiro[0].insert(0, 'O')
            return True

        elif self.__tabuleiro[1][1] == 'O' and self.__tabuleiro[0][2] == 'O' and self.__tabuleiro[2][0] != 'X':
            self.__tabuleiro[2].remove('7')
            self.__tabuleiro[2].insert(0, 'O')
            return True

        elif self.__tabuleiro[0][1] == 'O' and self.__tabuleiro[1][1] == 'O' and self.__tabuleiro[2][1] != 'X':
            self.__tabuleiro[2].remove('8')
            self.__tabuleiro[2].insert(1, 'O')
            return True

        elif self.__tabuleiro[1][1] == 'O' and self.__tabuleiro[2][1] == 'O' and self.__tabuleiro[0][1] != 'X':
            self.__tabuleiro[0].remove('2')
            self.__tabuleiro[0].insert(1, 'O')
            return True

        elif self.__tabuleiro[0][2] == 'O' and self.__tabuleiro[1][2] == 'O' and self.__tabuleiro[2][2] != 'X':
            self.__tabuleiro[2].remove('9')
            self.__tabuleiro[2].insert(2, 'O')
            return True

        elif self.__tabuleiro[1][2] == 'O' and self.__tabuleiro[2][2] == 'O' and self.__tabuleiro[0][2] != 'X':
            self.__tabuleiro[0].remove('3')
            self.__tabuleiro[0].insert(2, 'O')
            return True

        elif self.__tabuleiro[0][0] == 'O' and self.__tabuleiro[0][1] == 'O' and self.__tabuleiro[0][2] != 'X':
            self.__tabuleiro[0].remove('3')
            self.__tabuleiro[0].insert(2, 'O')
            return True

        elif self.__tabuleiro[0][1] == 'O' and self.__tabuleiro[0][2] == 'O' and self.__tabuleiro[0][0] != 'X':
            self.__tabuleiro[0].remove('1')
            self.__tabuleiro[0].insert(0, 'O')
            return True

        elif self.__tabuleiro[1][0] == 'O' and self.__tabuleiro[1][1] == 'O' and self.__tabuleiro[1][2] != 'X':
            self.__tabuleiro[1].remove('6')
            self.__tabuleiro[1].insert(2, 'O')
            return True

        elif self.__tabuleiro[1][1] == 'O' and self.__tabuleiro[1][2] == 'O' and self.__tabuleiro[1][0] != 'X':
            self.__tabuleiro[1].remove('4')
            self.__tabuleiro[1].insert(0, 'O')
            return True

        elif self.__tabuleiro[2][0] == 'O' and self.__tabuleiro[2][1] == 'O' and self.__tabuleiro[2][2] != 'X':
            self.__tabuleiro[2].remove('9')
            self.__tabuleiro[2].insert(2, 'O')
            return True

        elif self.__tabuleiro[2][1] == 'O' and self.__tabuleiro[2][2] == 'O' and self.__tabuleiro[2][0] != 'X':
            self.__tabuleiro[2].remove('7')
            self.__tabuleiro[2].insert(0, 'O')
            return True


    def quase_lá(self):
        if self.__tabuleiro[0][0] == 'X' and self.__tabuleiro[0][2] == 'X' and self.__tabuleiro[0][1] != 'O':
            self.__tabuleiro[0].remove('2')
            self.__tabuleiro[0].insert(1, 'O')
            return True

        elif self.__tabuleiro[0][0] == 'X' and self.__tabuleiro[2][0] == 'X' and self.__tabuleiro[1][0] != 'O':
            self.__tabuleiro[1].remove('4')
            self.__tabuleiro[1].insert(0, 'O')
            return True

        elif self.__tabuleiro[0][0] == 'X' and self.__tabuleiro[2][2] == 'X' and self.__tabuleiro[1][1] != 'O':
            self.__tabuleiro[1].remove('5')
            self.__tabuleiro[1].insert(1, 'O')
            return True

        elif self.__tabuleiro[0][1] == 'X' and self.__tabuleiro[2][1] == 'X' and self.__tabuleiro[1][1] != 'O':
            self.__tabuleiro[1].remove('5')
            self.__tabuleiro[1].insert(1, 'O')
            return True

        elif self.__tabuleiro[1][0] == 'X' and self.__tabuleiro[2][0] == 'X' and self.__tabuleiro[0][0] != 'O':
            self.__tabuleiro[0].remove('1')
            self.__tabuleiro[0].insert(0, 'O')
            return True

        elif self.__tabuleiro[0][2] == 'X' and self.__tabuleiro[2][2] == 'X' and self.__tabuleiro[1][2] != 'O':
            self.__tabuleiro[1].remove('6')
            self.__tabuleiro[1].insert(2, 'O')
            return True

        elif self.__tabuleiro[0][2] == 'X' and self.__tabuleiro[2][0] == 'X' and self.__tabuleiro[1][1] != 'O':
            self.__tabuleiro[1].remove('5')
            self.__tabuleiro[1].insert(1, 'O')
            return True

        elif self.__tabuleiro[1][0] == 'X' and self.__tabuleiro[1][2] == 'X' and self.__tabuleiro[1][1] != 'O':
            self.__tabuleiro[1].remove('5')
            self.__tabuleiro[1].insert(1, 'O')
            return True

        elif self.__tabuleiro[2][0] == 'X' and self.__tabuleiro[2][2] == 'X' and self.__tabuleiro[2][1] != 'O':
            self.__tabuleiro[2].remove('8')
            self.__tabuleiro[2].insert(1, 'O')
            return True

        elif self.__tabuleiro[0][0] == 'X' and self.__tabuleiro[1][0] == 'X' and self.__tabuleiro[2][0] != 'O':
            self.__tabuleiro[2].remove('7')
            self.__tabuleiro[2].insert(0, 'O')
            return True

        elif self.__tabuleiro[1][0] == 'X' and self.__tabuleiro[2][0] == 'X' and self.__tabuleiro[0][0] != 'O':
            self.__tabuleiro[0].remove('1')
            self.__tabuleiro[0].insert(0, 'O')
            return True

        elif self.__tabuleiro[0][0] == 'X' and self.__tabuleiro[1][1] == 'X' and self.__tabuleiro[2][2] != 'O':
            self.__tabuleiro[2].remove('9')
            self.__tabuleiro[2].insert(2, 'O')
            return True

        elif self.__tabuleiro[1][1] == 'X' and self.__tabuleiro[2][2] == 'X' and self.__tabuleiro[0][0] != 'O':
            self.__tabuleiro[0].remove('1')
            self.__tabuleiro[0].insert(0, 'O')
            return True

        elif self.__tabuleiro[1][1] == 'X' and self.__tabuleiro[0][2] == 'X' and self.__tabuleiro[2][0] != 'O':
            self.__tabuleiro[2].remove('7')
            self.__tabuleiro[2].insert(0, 'O')
            return True

        elif self.__tabuleiro[0][1] == 'X' and self.__tabuleiro[1][1] == 'X' and self.__tabuleiro[2][1] != 'O':
            self.__tabuleiro[2].remove('8')
            self.__tabuleiro[2].insert(1, 'O')
            return True

        elif self.__tabuleiro[1][1] == 'X' and self.__tabuleiro[2][1] == 'X' and self.__tabuleiro[0][1] != 'O':
            self.__tabuleiro[0].remove('2')
            self.__tabuleiro[0].insert(1, 'O')
            return True

        elif self.__tabuleiro[0][2] == 'X' and self.__tabuleiro[1][2] == 'X' and self.__tabuleiro[2][2] != 'O':
            self.__tabuleiro[2].remove('9')
            self.__tabuleiro[2].insert(2, 'O')
            return True

        elif self.__tabuleiro[1][2] == 'X' and self.__tabuleiro[2][2] == 'X' and self.__tabuleiro[0][2] != 'O':
            self.__tabuleiro[0].remove('3')
            self.__tabuleiro[0].insert(2, 'O')
            return True

        elif self.__tabuleiro[0][0] == 'X' and self.__tabuleiro[0][1] == 'X' and self.__tabuleiro[0][2] != 'O':
            self.__tabuleiro[0].remove('3')
            self.__tabuleiro[0].insert(2, 'O')
            return True

        elif self.__tabuleiro[0][1] == 'X' and self.__tabuleiro[0][2] == 'X' and self.__tabuleiro[0][0] != 'O':
            self.__tabuleiro[0].remove('1')
            self.__tabuleiro[0].insert(0, 'O')
            return True

        elif self.__tabuleiro[1][0] == 'X' and self.__tabuleiro[1][1] == 'X' and self.__tabuleiro[1][2] != 'O':
            self.__tabuleiro[1].remove('6')
            self.__tabuleiro[1].insert(2, 'O')
            return True

        elif self.__tabuleiro[1][1] == 'X' and self.__tabuleiro[1][2] == 'X' and self.__tabuleiro[1][0] != 'O':
            self.__tabuleiro[1].remove('4')
            self.__tabuleiro[1].insert(0, 'O')
            return True

        elif self.__tabuleiro[2][0] == 'X' and self.__tabuleiro[2][1] == 'X' and self.__tabuleiro[2][2] != 'O':
            self.__tabuleiro[2].remove('9')
            self.__tabuleiro[2].insert(2, 'O')
            return True

        elif self.__tabuleiro[2][1] == 'X' and self.__tabuleiro[2][2] == 'X' and self.__tabuleiro[2][0] != 'O':
            self.__tabuleiro[2].remove('7')
            self.__tabuleiro[2].insert(0, 'O')
            return True


    def jogada_cpu(self, x):
        for pos, v in enumerate(self.__tabuleiro):
            for d, c in enumerate(v):
                if c == x:
                    self.__tabuleiro[pos].remove(c)
                    self.__tabuleiro[pos].insert(d, 'O')
                    return True
        else:
            return False
