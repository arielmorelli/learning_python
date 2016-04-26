# coding=utf-8

"""

HangmanGame - Guess the word suggesting letters based on a clue.

O objetivo desse "desafio" é repassar os ensinamentos sobre a Sintaxe Básica Python.
O que vai ser repassado nesse desafio:
-Números, operações aritméticas e variáveis
-Strings e exibição no console
-Fluxo de controle e condições
-Laços de repetição (For e While)
-Funções x Métodos
-Vazamento de escopo - Não tem nada disso :/

Como padrão, o nome de variáveis, classes e funções estão em INGLÊS; porém os comentários e "tarefas" estão em
PORTUGUÊS para facilitar o entedimento.

"""


# TODO: importar a classe HangmanGame

import os
import string
import sys


base_dict = dict()
base_dict['monica'] = 'Famosa personagem de Mauricio de Sousa'
base_dict['magali'] = 'Famosa personagem de Mauricio de Sousa'
base_dict['cascao'] = 'Famoso personagem de Mauricio de Sousa'
base_dict['cebolinha'] = 'Famoso personagem de Mauricio de Sousa'
base_dict['casa'] = 'Tipica contrução de cidades'
base_dict['predio'] = 'Tipica contrução de cidades'
base_dict['carro'] = 'Veículo comum em cidades'
base_dict['onibus'] = 'Veículo comum em cidades'


def run_game():
    """
    Os TODOs são para facilitar o desenvolvimente,
    sintam-se a vontade para criar o código do jeito que acharem melhor
    """
    raise NotImplemented('Não foi implementado ainda!')

    # Variáveis 'word' e 'clue'= # TODO: escolher uma das opções do dicionário de opções e salvar sua chave e valor em variáveis

    game = None  # TODO: Iniciar o objeto game como sendo um HangmanGame. Passando como argumento a palavra e a dica ('word' e 'clue')

    print_current_round(game)  # Função já definida que imprime na tela o jogo atual baseado na quantidade de vidas

    character = read_one_char()  # Função já definida usada pra ler uma letra do teclado

    # TODO: Verificar se a letra ainda não foi digitada

    # TODO: Salvar na lista de letras usaddas

    # TODO: Verificar se a letra digitado existe na palavra (usar método has_letter do objeto do jogo - IMPLEMENTAR)

    # TODO: Caso existe:

    # TODO: Caso não existe: Diminuir a vida em 1

    # TODO: Verificar se o jogo já acabou

    # TODO: rodar enquanto o jogo, previamente instanciado, não estiver acabado (verificar is_over)

    sys.exit(0)  # acabou como queriamos


def print_current_round(current_game):
    """ Print the game itself
    :param current_game: the game that will be printed
    """
    os.system('clear')
    print "Dica:", current_game.clue

    print current_game.get_stage_draw()

    # TODO: imprimir de todos os valores que existem dentro da palavra - caso letra não tenha ido, imprimir '_' no lugar. Separar por espaços (usar for)
    print 'aqui vai o espaço de letras já reveladas e não reveladas'

    # TODO: imprimir todas as letras já tentadas
    print 'aqui vai a lista de letras que já foram tentadas' # pular uma linha


def read_one_char():
    """Return a valid asciii character.
    :return String: char
    """
    char = raw_input('Letra:')
    while len(char) > 1 or char not in string.ascii_letters:
        print 'Valor inválido. Por favor digiter uma letra sem nenhum tipo de acentuação. Valor digitado:', char
        char = raw_input('Letra:')
    return char


if __name__ == '__main__':
    print 'Falta chamar o método certo ;)'
    sys.exit(0)
