# coding=utf-8


class HangmanGame(object):
    def __init__(self, word, clue):
        self.word = word
        self.clue = clue
        self.lives = 6
        self.list_of_letters = []

    def has_letter(self, letter):
        """ Verify if a letter exist in the word. Return a bool
        :param letter: letter that will be analyzed
        :return bool: return if the word has letter or no
        """
        return letter in self.word

    def is_over(self):
        """Verify if the game is over
        :return bool: return if game is over or no
        """
        if self.lives == 0:
            return True
        elif not set(self.word)-set(self.list_of_letters):
            return True
        else:
            return False

    def get_stage_draw(self):
        """List of draws
        :return string: return the current draw (ascii draw)
        """
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
