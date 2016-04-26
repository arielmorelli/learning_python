# coding=utf-8

"""

HangmanGame - Guess the word suggesting letters based on a clue.

O objetivo desse "desafio" é repassar os ensinamentos sobre a Sintaxe Básica Python.
O que vai ser repassado nesse desafio:
-Números, operações aritméticas e variáveis
-Strings e exibição no console
-Fluxo de controle e condições
-Laços de repetição (For e While)
-Funções
-Vazamento de escopo

Como padrão, o nome de variáveis, classes e funções estão em INGLÊS; porém os comentários e "tarefas" estão em
PORTUGUÊS para facilitar o entedimento.

"""


import os
import string
import sys
import random
from hangman_game import HangmanGame

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

    word, clue = random.choice(base_dict.items())

    game = HangmanGame(word, clue)

    while not game.is_over():
        print_current_round(game)  # Função já definida que imprime na tela o jogo atual baseado na quantidade de vidas

        character = read_one_char()
        while character in game.list_of_letters:
            print "A letra {} ja foi digitada.".format(character)
            character = read_one_char()  # Função já definida usada pra ler uma letra do teclado

        game.list_of_letters.append(character)

        if not game.has_letter(character):
            game.lives -= 1

    sys.exit(0)  # acabou como queriamos


def print_current_round(current_game):
    """ Print the game itself
    :param current_game: the game that will be printed
    """
    os.system('clear')
    print "Dica:", current_game.clue

    print current_game.get_stage_draw()

    for letter in current_game.word:
        if letter in current_game.list_of_letters:
            print ' ' + letter,
        else:
            print ' _',

    print ''

    print ','.join(current_game.list_of_letters)


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
    run_game()
    sys.exit(0)
