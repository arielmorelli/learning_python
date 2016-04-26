# coding=utf-8


class HangmanGame(object):
    def __init__(self, word, clue):
        self.word = word
        self.clue = clue
        self.lives = 6
        self.list_of_letters = []

    def has_letter(self, letter):
        """Verify if a letter exist in the word. Return a bool"""
        # TODO: escrever o código verifica se existe a letra na palavra a ser adivinhada.
        # Caso existe, retorne True, caso contrário, False

        raise NotImplemented('método "has_letter" não foi implementado ainda!')

    def is_over(self, letter):
        """Verify if the game is over. Return a bool"""
        # TODO: Verificar se todas as letras foram descobertas ou as vidas restantes chegaram a 0
        raise NotImplemented('método "is_over" não foi implementado ainda!')

    def get_stage_draw(self):
        """Return a simple draw to represent the current stage of the game."""
        stage = dict()
        stage[0] = """
         _________
        |         |
        |         0
        |        /|\\
        |        / \\
        |
        |
        """
        stage[1] = """
         _________
        |         |
        |         0
        |        /|\\
        |        /
        |
        |
        """
        stage[2] = """
         _________
        |         |
        |         0
        |        /|\\
        |
        |
        |
        """
        stage[3] = """
         _________
        |         |
        |         0
        |        /|
        |
        |
        |
        """
        stage[4] = """
         _________
        |         |
        |         0
        |         |
        |
        |
        |
        """
        stage[5] = """
         _________
        |         |
        |         0
        |
        |
        |
        |
        """
        stage[6] = """
         _________
        |         |
        |
        |
        |
        |
        |
        """
        return stage[self.lives]
