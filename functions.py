resultado = ''
numjog = 1
tabuleiro = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
jogador = list()
vitjog = 0
vitcomp = 0
resp = ''


def desenho_do_tabuleiro():
    print(f'\n| O JOGO DA VELHA |\n'
          f'\nPlacar: {vitjog} X {vitcomp}\n')
    print(f' {tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]}\n'
          f'---+---+---\n'
          f' {tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]}\n'
          f'---+---+---\n'
          f' {tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]}\n')


def vertical():
    if tabuleiro[0][0] == 'X' and tabuleiro[1][0] == 'X' and tabuleiro[2][0] == 'X':
        return True
    elif tabuleiro[0][1] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[2][1] == 'X':
        return True
    elif tabuleiro[0][2] == 'X' and tabuleiro[1][2] == 'X' and tabuleiro[2][2] == 'X':
        return True
    elif tabuleiro[0][0] == 'O' and tabuleiro[1][0] == 'O' and tabuleiro[2][0] == 'O':
        return True
    elif tabuleiro[0][1] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[2][1] == 'O':
        return True
    elif tabuleiro[0][2] == 'O' and tabuleiro[1][2] == 'O' and tabuleiro[2][2] == 'O':
        return True
    else:
        return False


def horizontal():
    if tabuleiro[0][0] == 'X' and tabuleiro[0][1] == 'X' and tabuleiro[0][2] == 'X':
        return True
    elif tabuleiro[1][0] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[1][2] == 'X':
        return True
    elif tabuleiro[2][0] == 'X' and tabuleiro[2][1] == 'X' and tabuleiro[2][2] == 'X':
        return True
    elif tabuleiro[0][0] == 'O' and tabuleiro[0][1] == 'O' and tabuleiro[0][2] == 'O':
        return True
    elif tabuleiro[1][0] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[1][2] == 'O':
        return True
    elif tabuleiro[2][0] == 'O' and tabuleiro[2][1] == 'O' and tabuleiro[2][2] == 'O':
        return True
    else:
        return False


def diagonal():
    if tabuleiro[0][0] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[2][2] == 'X':
        return True
    elif tabuleiro[0][2] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[2][0] == 'X':
        return True
    elif tabuleiro[0][0] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[2][2] == 'O':
        return True
    elif tabuleiro[0][2] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[2][0] == 'O':
        return True
    else:
        return False


def empate():
    for v in tabuleiro:
        for c in v:
            if c.isnumeric():
                return False
    else:
        return True


def verificação():
    if vertical():
        return True
    elif horizontal():
        return True
    elif diagonal():
        return True
    else:
        return False


def jogada(x):
    for c in tabuleiro:
        for pos, d in enumerate(c):
            if d.isnumeric() and d == x and numjog % 2 == 1:
                jogador.append(d)
                c.remove(d)
                c.insert(pos, 'X')
                return True
            elif d.isnumeric() and d == x and numjog % 2 == 0:
                c.remove(d)
                c.insert(pos, 'O')
                return True
    else:
        return False


def quase_lá_cpu(x):
    if x[0][0] == 'O' and x[0][2] == 'O' and x[0][1] != 'X':
        tabuleiro[0].remove('2')
        tabuleiro[0].insert(1, 'O')
        return True

    elif x[0][0] == 'O' and x[2][0] == 'O' and x[1][0] != 'X':
        tabuleiro[1].remove('4')
        tabuleiro[1].insert(0, 'O')
        return True

    elif x[0][0] == 'O' and x[2][2] == 'O' and x[1][1] != 'X':
        tabuleiro[1].remove('5')
        tabuleiro[1].insert(1, 'O')
        return True

    elif x[0][1] == 'O' and x[2][1] == 'O' and x[1][1] != 'X':
        tabuleiro[1].remove('5')
        tabuleiro[1].insert(1, 'O')
        return True

    elif x[1][0] == 'O' and x[2][0] == 'O' and x[0][0] != 'X':
        tabuleiro[0].remove('1')
        tabuleiro[0].insert(0, 'O')
        return True

    elif x[0][2] == 'O' and x[2][2] == 'O' and x[1][2] != 'X':
        tabuleiro[1].remove('6')
        tabuleiro[1].insert(2, 'O')
        return True

    elif x[0][2] == 'O' and x[2][0] == 'O' and x[1][1] != 'X':
        tabuleiro[1].remove('5')
        tabuleiro[1].insert(1, 'O')
        return True

    elif x[1][0] == 'O' and x[1][2] == 'O' and x[1][1] != 'X':
        tabuleiro[1].remove('5')
        tabuleiro[1].insert(1, 'O')
        return True

    elif x[2][0] == 'O' and x[2][2] == 'O' and x[2][1] != 'X':
        tabuleiro[2].remove('8')
        tabuleiro[2].insert(1, 'O')
        return True

    elif x[0][0] == 'O' and x[1][0] == 'O' and x[2][0] != 'X':
        tabuleiro[2].remove('7')
        tabuleiro[2].insert(0, 'O')
        return True

    elif x[1][0] == 'O' and x[2][0] == 'O' and x[0][0] != 'X':
        tabuleiro[0].remove('1')
        tabuleiro[0].insert(0, 'O')
        return True

    elif x[0][0] == 'O' and x[1][1] == 'O' and x[2][2] != 'X':
        tabuleiro[2].remove('9')
        tabuleiro[2].insert(2, 'O')
        return True

    elif x[1][1] == 'O' and x[2][2] == 'O' and x[0][0] != 'X':
        tabuleiro[0].remove('1')
        tabuleiro[0].insert(0, 'O')
        return True

    elif x[1][1] == 'O' and x[0][2] == 'O' and x[2][0] != 'X':
        tabuleiro[2].remove('7')
        tabuleiro[2].insert(0, 'O')
        return True

    elif x[0][1] == 'O' and x[1][1] == 'O' and x[2][1] != 'X':
        tabuleiro[2].remove('8')
        tabuleiro[2].insert(1, 'O')
        return True

    elif x[1][1] == 'O' and x[2][1] == 'O' and x[0][1] != 'X':
        tabuleiro[0].remove('2')
        tabuleiro[0].insert(1, 'O')
        return True

    elif x[0][2] == 'O' and x[1][2] == 'O' and x[2][2] != 'X':
        tabuleiro[2].remove('9')
        tabuleiro[2].insert(2, 'O')
        return True

    elif x[1][2] == 'O' and x[2][2] == 'O' and x[0][2] != 'X':
        tabuleiro[0].remove('3')
        tabuleiro[0].insert(2, 'O')
        return True

    elif x[0][0] == 'O' and x[0][1] == 'O' and x[0][2] != 'X':
        tabuleiro[0].remove('3')
        tabuleiro[0].insert(2, 'O')
        return True

    elif x[0][1] == 'O' and x[0][2] == 'O' and x[0][0] != 'X':
        tabuleiro[0].remove('1')
        tabuleiro[0].insert(0, 'O')
        return True

    elif x[1][0] == 'O' and x[1][1] == 'O' and x[1][2] != 'X':
        tabuleiro[1].remove('6')
        tabuleiro[1].insert(2, 'O')
        return True

    elif x[1][1] == 'O' and x[1][2] == 'O' and x[1][0] != 'X':
        tabuleiro[1].remove('4')
        tabuleiro[1].insert(0, 'O')
        return True

    elif x[2][0] == 'O' and x[2][1] == 'O' and x[2][2] != 'X':
        tabuleiro[2].remove('9')
        tabuleiro[2].insert(2, 'O')
        return True

    elif x[2][1] == 'O' and x[2][2] == 'O' and x[2][0] != 'X':
        tabuleiro[2].remove('7')
        tabuleiro[2].insert(0, 'O')
        return True


def quase_lá(x):
    if x[0][0] == 'X' and x[0][2] == 'X' and x[0][1] != 'O':
        tabuleiro[0].remove('2')
        tabuleiro[0].insert(1, 'O')
        return True

    elif x[0][0] == 'X' and x[2][0] == 'X' and x[1][0] != 'O':
        tabuleiro[1].remove('4')
        tabuleiro[1].insert(0, 'O')
        return True

    elif x[0][0] == 'X' and x[2][2] == 'X' and x[1][1] != 'O':
        tabuleiro[1].remove('5')
        tabuleiro[1].insert(1, 'O')
        return True

    elif x[0][1] == 'X' and x[2][1] == 'X' and x[1][1] != 'O':
        tabuleiro[1].remove('5')
        tabuleiro[1].insert(1, 'O')
        return True

    elif x[1][0] == 'X' and x[2][0] == 'X' and x[0][0] != 'O':
        tabuleiro[0].remove('1')
        tabuleiro[0].insert(0, 'O')
        return True

    elif x[0][2] == 'X' and x[2][2] == 'X' and x[1][2] != 'O':
        tabuleiro[1].remove('6')
        tabuleiro[1].insert(2, 'O')
        return True

    elif x[0][2] == 'X' and x[2][0] == 'X' and x[1][1] != 'O':
        tabuleiro[1].remove('5')
        tabuleiro[1].insert(1, 'O')
        return True

    elif x[1][0] == 'X' and x[1][2] == 'X' and x[1][1] != 'O':
        tabuleiro[1].remove('5')
        tabuleiro[1].insert(1, 'O')
        return True

    elif x[2][0] == 'X' and x[2][2] == 'X' and x[2][1] != 'O':
        tabuleiro[2].remove('8')
        tabuleiro[2].insert(1, 'O')
        return True

    elif x[0][0] == 'X' and x[1][0] == 'X' and x[2][0] != 'O':
        tabuleiro[2].remove('7')
        tabuleiro[2].insert(0, 'O')
        return True

    elif x[1][0] == 'X' and x[2][0] == 'X' and x[0][0] != 'O':
        tabuleiro[0].remove('1')
        tabuleiro[0].insert(0, 'O')
        return True

    elif x[0][0] == 'X' and x[1][1] == 'X' and x[2][2] != 'O':
        tabuleiro[2].remove('9')
        tabuleiro[2].insert(2, 'O')
        return True

    elif x[1][1] == 'X' and x[2][2] == 'X' and x[0][0] != 'O':
        tabuleiro[0].remove('1')
        tabuleiro[0].insert(0, 'O')
        return True

    elif x[1][1] == 'X' and x[0][2] == 'X' and x[2][0] != 'O':
        tabuleiro[2].remove('7')
        tabuleiro[2].insert(0, 'O')
        return True

    elif x[0][1] == 'X' and x[1][1] == 'X' and x[2][1] != 'O':
        tabuleiro[2].remove('8')
        tabuleiro[2].insert(1, 'O')
        return True

    elif x[1][1] == 'X' and x[2][1] == 'X' and x[0][1] != 'O':
        tabuleiro[0].remove('2')
        tabuleiro[0].insert(1, 'O')
        return True

    elif x[0][2] == 'X' and x[1][2] == 'X' and x[2][2] != 'O':
        tabuleiro[2].remove('9')
        tabuleiro[2].insert(2, 'O')
        return True

    elif x[1][2] == 'X' and x[2][2] == 'X' and x[0][2] != 'O':
        tabuleiro[0].remove('3')
        tabuleiro[0].insert(2, 'O')
        return True

    elif x[0][0] == 'X' and x[0][1] == 'X' and x[0][2] != 'O':
        tabuleiro[0].remove('3')
        tabuleiro[0].insert(2, 'O')
        return True

    elif x[0][1] == 'X' and x[0][2] == 'X' and x[0][0] != 'O':
        tabuleiro[0].remove('1')
        tabuleiro[0].insert(0, 'O')
        return True

    elif x[1][0] == 'X' and x[1][1] == 'X' and x[1][2] != 'O':
        tabuleiro[1].remove('6')
        tabuleiro[1].insert(2, 'O')
        return True

    elif x[1][1] == 'X' and x[1][2] == 'X' and x[1][0] != 'O':
        tabuleiro[1].remove('4')
        tabuleiro[1].insert(0, 'O')
        return True

    elif x[2][0] == 'X' and x[2][1] == 'X' and x[2][2] != 'O':
        tabuleiro[2].remove('9')
        tabuleiro[2].insert(2, 'O')
        return True

    elif x[2][1] == 'X' and x[2][2] == 'X' and x[2][0] != 'O':
        tabuleiro[2].remove('7')
        tabuleiro[2].insert(0, 'O')
        return True


def jogada_cpu(x):
    for pos, v in enumerate(tabuleiro):
        for d, c in enumerate(v):
            if c == x:
                tabuleiro[pos].remove(c)
                tabuleiro[pos].insert(d, 'O')
                return True
    else:
        return False
