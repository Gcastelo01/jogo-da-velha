class Tabuleiro:
    def __init__(self) -> None:
        self.tabuleiro = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        self.resultado = ''
        self.numjog = 1
        self.jogador = list()
        self.vitjog = 0
        self.vitcomp = 0
        self.resp = ''


    def tela_do_final_cpu(self):
        print(f'>>>>> FIM DE JOGO! <<<<<\n'
        f'\n|     PLACAR GERAL:    |\n'
        f'\nCOMPUTADOR: [{self.vitcomp:^3}]\n'
        f'JOGADOR:    [{self.vitjog:^3}]\n')
        input('\nPRESSIONE [ENTER] PARA SAIR')


    def tela_do_final_jog(self):
        print(f'>>>>> FIM DE JOGO! <<<<<\n'
        f'\n|     PLACAR GERAL:    |\n'
        f'\nJOGADOR 1:  [{self.vitjog:^3}]\n'
        f'JOGADOR 2:  [{self.vitcomp:^3}]\n')
        input('\nPRESSIONE [ENTER] PARA SAIR')



    def resetar_tabuleiro(self) -> None:
        self.tabuleiro = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        self.numjog = 1
        


    def desenho_do_tabuleiro(self):
        print(f'\n| O JOGO DA VELHA |\n'
            f'\nPlacar: {self.vitjog} X {self.vitcomp}\n')
        print(f' {self.tabuleiro[0][0]} | {self.tabuleiro[0][1]} | {self.tabuleiro[0][2]}\n'
            f'---+---+---\n'
            f' {self.tabuleiro[1][0]} | {self.tabuleiro[1][1]} | {self.tabuleiro[1][2]}\n'
            f'---+---+---\n'
            f' {self.tabuleiro[2][0]} | {self.tabuleiro[2][1]} | {self.tabuleiro[2][2]}\n')


    def vertical(self):
        if self.tabuleiro[0][0] == 'X' and self.tabuleiro[1][0] == 'X' and self.tabuleiro[2][0] == 'X':
            return True
        elif self.tabuleiro[0][1] == 'X' and self.tabuleiro[1][1] == 'X' and self.tabuleiro[2][1] == 'X':
            return True
        elif self.tabuleiro[0][2] == 'X' and self.tabuleiro[1][2] == 'X' and self.tabuleiro[2][2] == 'X':
            return True
        elif self.tabuleiro[0][0] == 'O' and self.tabuleiro[1][0] == 'O' and self.tabuleiro[2][0] == 'O':
            return True
        elif self.tabuleiro[0][1] == 'O' and self.tabuleiro[1][1] == 'O' and self.tabuleiro[2][1] == 'O':
            return True
        elif self.tabuleiro[0][2] == 'O' and self.tabuleiro[1][2] == 'O' and self.tabuleiro[2][2] == 'O':
            return True
        else:
            return False


    def horizontal(self):
        if self.tabuleiro[0][0] == 'X' and self.tabuleiro[0][1] == 'X' and self.tabuleiro[0][2] == 'X':
            return True
        elif self.tabuleiro[1][0] == 'X' and self.tabuleiro[1][1] == 'X' and self.tabuleiro[1][2] == 'X':
            return True
        elif self.tabuleiro[2][0] == 'X' and self.tabuleiro[2][1] == 'X' and self.tabuleiro[2][2] == 'X':
            return True
        elif self.tabuleiro[0][0] == 'O' and self.tabuleiro[0][1] == 'O' and self.tabuleiro[0][2] == 'O':
            return True
        elif self.tabuleiro[1][0] == 'O' and self.tabuleiro[1][1] == 'O' and self.tabuleiro[1][2] == 'O':
            return True
        elif self.tabuleiro[2][0] == 'O' and self.tabuleiro[2][1] == 'O' and self.tabuleiro[2][2] == 'O':
            return True
        else:
            return False


    def diagonal(self):
        if self.tabuleiro[0][0] == 'X' and self.tabuleiro[1][1] == 'X' and self.tabuleiro[2][2] == 'X':
            return True
        elif self.tabuleiro[0][2] == 'X' and self.tabuleiro[1][1] == 'X' and self.tabuleiro[2][0] == 'X':
            return True
        elif self.tabuleiro[0][0] == 'O' and self.tabuleiro[1][1] == 'O' and self.tabuleiro[2][2] == 'O':
            return True
        elif self.tabuleiro[0][2] == 'O' and self.tabuleiro[1][1] == 'O' and self.tabuleiro[2][0] == 'O':
            return True
        else:
            return False


    def empate(self):
        for v in self.tabuleiro:
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
        for c in self.tabuleiro:
            for pos, d in enumerate(c):
                if d.isnumeric() and d == x and self.numjog % 2 == 1:
                    self.jogador.append(d)
                    c.remove(d)
                    c.insert(pos, 'X')
                    return True
                elif d.isnumeric() and d == x and self.numjog % 2 == 0:
                    c.remove(d)
                    c.insert(pos, 'O')
                    return True
        else:
            return False


    def quase_lá_cpu(self):
        if self.tabuleiro[0][0] == 'O' and self.tabuleiro[0][2] == 'O' and self.tabuleiro[0][1] != 'X':
            self.tabuleiro[0].remove('2')
            self.tabuleiro[0].insert(1, 'O')
            return True

        elif self.tabuleiro[0][0] == 'O' and self.tabuleiro[2][0] == 'O' and self.tabuleiro[1][0] != 'X':
            self.tabuleiro[1].remove('4')
            self.tabuleiro[1].insert(0, 'O')
            return True

        elif self.tabuleiro[0][0] == 'O' and self.tabuleiro[2][2] == 'O' and self.tabuleiro[1][1] != 'X':
            self.tabuleiro[1].remove('5')
            self.tabuleiro[1].insert(1, 'O')
            return True

        elif self.tabuleiro[0][1] == 'O' and self.tabuleiro[2][1] == 'O' and self.tabuleiro[1][1] != 'X':
            self.tabuleiro[1].remove('5')
            self.tabuleiro[1].insert(1, 'O')
            return True

        elif self.tabuleiro[1][0] == 'O' and self.tabuleiro[2][0] == 'O' and self.tabuleiro[0][0] != 'X':
            self.tabuleiro[0].remove('1')
            self.tabuleiro[0].insert(0, 'O')
            return True

        elif self.tabuleiro[0][2] == 'O' and self.tabuleiro[2][2] == 'O' and self.tabuleiro[1][2] != 'X':
            self.tabuleiro[1].remove('6')
            self.tabuleiro[1].insert(2, 'O')
            return True

        elif self.tabuleiro[0][2] == 'O' and self.tabuleiro[2][0] == 'O' and self.tabuleiro[1][1] != 'X':
            self.tabuleiro[1].remove('5')
            self.tabuleiro[1].insert(1, 'O')
            return True

        elif self.tabuleiro[1][0] == 'O' and self.tabuleiro[1][2] == 'O' and self.tabuleiro[1][1] != 'X':
            self.tabuleiro[1].remove('5')
            self.tabuleiro[1].insert(1, 'O')
            return True

        elif self.tabuleiro[2][0] == 'O' and self.tabuleiro[2][2] == 'O' and self.tabuleiro[2][1] != 'X':
            self.tabuleiro[2].remove('8')
            self.tabuleiro[2].insert(1, 'O')
            return True

        elif self.tabuleiro[0][0] == 'O' and self.tabuleiro[1][0] == 'O' and self.tabuleiro[2][0] != 'X':
            self.tabuleiro[2].remove('7')
            self.tabuleiro[2].insert(0, 'O')
            return True

        elif self.tabuleiro[1][0] == 'O' and self.tabuleiro[2][0] == 'O' and self.tabuleiro[0][0] != 'X':
            self.tabuleiro[0].remove('1')
            self.tabuleiro[0].insert(0, 'O')
            return True

        elif self.tabuleiro[0][0] == 'O' and self.tabuleiro[1][1] == 'O' and self.tabuleiro[2][2] != 'X':
            self.tabuleiro[2].remove('9')
            self.tabuleiro[2].insert(2, 'O')
            return True

        elif self.tabuleiro[1][1] == 'O' and self.tabuleiro[2][2] == 'O' and self.tabuleiro[0][0] != 'X':
            self.tabuleiro[0].remove('1')
            self.tabuleiro[0].insert(0, 'O')
            return True

        elif self.tabuleiro[1][1] == 'O' and self.tabuleiro[0][2] == 'O' and self.tabuleiro[2][0] != 'X':
            self.tabuleiro[2].remove('7')
            self.tabuleiro[2].insert(0, 'O')
            return True

        elif self.tabuleiro[0][1] == 'O' and self.tabuleiro[1][1] == 'O' and self.tabuleiro[2][1] != 'X':
            self.tabuleiro[2].remove('8')
            self.tabuleiro[2].insert(1, 'O')
            return True

        elif self.tabuleiro[1][1] == 'O' and self.tabuleiro[2][1] == 'O' and self.tabuleiro[0][1] != 'X':
            self.tabuleiro[0].remove('2')
            self.tabuleiro[0].insert(1, 'O')
            return True

        elif self.tabuleiro[0][2] == 'O' and self.tabuleiro[1][2] == 'O' and self.tabuleiro[2][2] != 'X':
            self.tabuleiro[2].remove('9')
            self.tabuleiro[2].insert(2, 'O')
            return True

        elif self.tabuleiro[1][2] == 'O' and self.tabuleiro[2][2] == 'O' and self.tabuleiro[0][2] != 'X':
            self.tabuleiro[0].remove('3')
            self.tabuleiro[0].insert(2, 'O')
            return True

        elif self.tabuleiro[0][0] == 'O' and self.tabuleiro[0][1] == 'O' and self.tabuleiro[0][2] != 'X':
            self.tabuleiro[0].remove('3')
            self.tabuleiro[0].insert(2, 'O')
            return True

        elif self.tabuleiro[0][1] == 'O' and self.tabuleiro[0][2] == 'O' and self.tabuleiro[0][0] != 'X':
            self.tabuleiro[0].remove('1')
            self.tabuleiro[0].insert(0, 'O')
            return True

        elif self.tabuleiro[1][0] == 'O' and self.tabuleiro[1][1] == 'O' and self.tabuleiro[1][2] != 'X':
            self.tabuleiro[1].remove('6')
            self.tabuleiro[1].insert(2, 'O')
            return True

        elif self.tabuleiro[1][1] == 'O' and self.tabuleiro[1][2] == 'O' and self.tabuleiro[1][0] != 'X':
            self.tabuleiro[1].remove('4')
            self.tabuleiro[1].insert(0, 'O')
            return True

        elif self.tabuleiro[2][0] == 'O' and self.tabuleiro[2][1] == 'O' and self.tabuleiro[2][2] != 'X':
            self.tabuleiro[2].remove('9')
            self.tabuleiro[2].insert(2, 'O')
            return True

        elif self.tabuleiro[2][1] == 'O' and self.tabuleiro[2][2] == 'O' and self.tabuleiro[2][0] != 'X':
            self.tabuleiro[2].remove('7')
            self.tabuleiro[2].insert(0, 'O')
            return True


    def quase_lá(self):
        if self.tabuleiro[0][0] == 'X' and self.tabuleiro[0][2] == 'X' and self.tabuleiro[0][1] != 'O':
            self.tabuleiro[0].remove('2')
            self.tabuleiro[0].insert(1, 'O')
            return True

        elif self.tabuleiro[0][0] == 'X' and self.tabuleiro[2][0] == 'X' and self.tabuleiro[1][0] != 'O':
            self.tabuleiro[1].remove('4')
            self.tabuleiro[1].insert(0, 'O')
            return True

        elif self.tabuleiro[0][0] == 'X' and self.tabuleiro[2][2] == 'X' and self.tabuleiro[1][1] != 'O':
            self.tabuleiro[1].remove('5')
            self.tabuleiro[1].insert(1, 'O')
            return True

        elif self.tabuleiro[0][1] == 'X' and self.tabuleiro[2][1] == 'X' and self.tabuleiro[1][1] != 'O':
            self.tabuleiro[1].remove('5')
            self.tabuleiro[1].insert(1, 'O')
            return True

        elif self.tabuleiro[1][0] == 'X' and self.tabuleiro[2][0] == 'X' and self.tabuleiro[0][0] != 'O':
            self.tabuleiro[0].remove('1')
            self.tabuleiro[0].insert(0, 'O')
            return True

        elif self.tabuleiro[0][2] == 'X' and self.tabuleiro[2][2] == 'X' and self.tabuleiro[1][2] != 'O':
            self.tabuleiro[1].remove('6')
            self.tabuleiro[1].insert(2, 'O')
            return True

        elif self.tabuleiro[0][2] == 'X' and self.tabuleiro[2][0] == 'X' and self.tabuleiro[1][1] != 'O':
            self.tabuleiro[1].remove('5')
            self.tabuleiro[1].insert(1, 'O')
            return True

        elif self.tabuleiro[1][0] == 'X' and self.tabuleiro[1][2] == 'X' and self.tabuleiro[1][1] != 'O':
            self.tabuleiro[1].remove('5')
            self.tabuleiro[1].insert(1, 'O')
            return True

        elif self.tabuleiro[2][0] == 'X' and self.tabuleiro[2][2] == 'X' and self.tabuleiro[2][1] != 'O':
            self.tabuleiro[2].remove('8')
            self.tabuleiro[2].insert(1, 'O')
            return True

        elif self.tabuleiro[0][0] == 'X' and self.tabuleiro[1][0] == 'X' and self.tabuleiro[2][0] != 'O':
            self.tabuleiro[2].remove('7')
            self.tabuleiro[2].insert(0, 'O')
            return True

        elif self.tabuleiro[1][0] == 'X' and self.tabuleiro[2][0] == 'X' and self.tabuleiro[0][0] != 'O':
            self.tabuleiro[0].remove('1')
            self.tabuleiro[0].insert(0, 'O')
            return True

        elif self.tabuleiro[0][0] == 'X' and self.tabuleiro[1][1] == 'X' and self.tabuleiro[2][2] != 'O':
            self.tabuleiro[2].remove('9')
            self.tabuleiro[2].insert(2, 'O')
            return True

        elif self.tabuleiro[1][1] == 'X' and self.tabuleiro[2][2] == 'X' and self.tabuleiro[0][0] != 'O':
            self.tabuleiro[0].remove('1')
            self.tabuleiro[0].insert(0, 'O')
            return True

        elif self.tabuleiro[1][1] == 'X' and self.tabuleiro[0][2] == 'X' and self.tabuleiro[2][0] != 'O':
            self.tabuleiro[2].remove('7')
            self.tabuleiro[2].insert(0, 'O')
            return True

        elif self.tabuleiro[0][1] == 'X' and self.tabuleiro[1][1] == 'X' and self.tabuleiro[2][1] != 'O':
            self.tabuleiro[2].remove('8')
            self.tabuleiro[2].insert(1, 'O')
            return True

        elif self.tabuleiro[1][1] == 'X' and self.tabuleiro[2][1] == 'X' and self.tabuleiro[0][1] != 'O':
            self.tabuleiro[0].remove('2')
            self.tabuleiro[0].insert(1, 'O')
            return True

        elif self.tabuleiro[0][2] == 'X' and self.tabuleiro[1][2] == 'X' and self.tabuleiro[2][2] != 'O':
            self.tabuleiro[2].remove('9')
            self.tabuleiro[2].insert(2, 'O')
            return True

        elif self.tabuleiro[1][2] == 'X' and self.tabuleiro[2][2] == 'X' and self.tabuleiro[0][2] != 'O':
            self.tabuleiro[0].remove('3')
            self.tabuleiro[0].insert(2, 'O')
            return True

        elif self.tabuleiro[0][0] == 'X' and self.tabuleiro[0][1] == 'X' and self.tabuleiro[0][2] != 'O':
            self.tabuleiro[0].remove('3')
            self.tabuleiro[0].insert(2, 'O')
            return True

        elif self.tabuleiro[0][1] == 'X' and self.tabuleiro[0][2] == 'X' and self.tabuleiro[0][0] != 'O':
            self.tabuleiro[0].remove('1')
            self.tabuleiro[0].insert(0, 'O')
            return True

        elif self.tabuleiro[1][0] == 'X' and self.tabuleiro[1][1] == 'X' and self.tabuleiro[1][2] != 'O':
            self.tabuleiro[1].remove('6')
            self.tabuleiro[1].insert(2, 'O')
            return True

        elif self.tabuleiro[1][1] == 'X' and self.tabuleiro[1][2] == 'X' and self.tabuleiro[1][0] != 'O':
            self.tabuleiro[1].remove('4')
            self.tabuleiro[1].insert(0, 'O')
            return True

        elif self.tabuleiro[2][0] == 'X' and self.tabuleiro[2][1] == 'X' and self.tabuleiro[2][2] != 'O':
            self.tabuleiro[2].remove('9')
            self.tabuleiro[2].insert(2, 'O')
            return True

        elif self.tabuleiro[2][1] == 'X' and self.tabuleiro[2][2] == 'X' and self.tabuleiro[2][0] != 'O':
            self.tabuleiro[2].remove('7')
            self.tabuleiro[2].insert(0, 'O')
            return True


    def jogada_cpu(self, x):
        for pos, v in enumerate(self.tabuleiro):
            for d, c in enumerate(v):
                if c == x:
                    self.tabuleiro[pos].remove(c)
                    self.tabuleiro[pos].insert(d, 'O')
                    return True
        else:
            return False
