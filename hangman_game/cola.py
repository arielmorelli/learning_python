# coding=utf-8

"""
    Esse arquivo tem a finalidade de servir de ~cola~ para o desenvolvimento
do desafio, assim como exemplificar o uso de algumas funcionalidades
que não abordaremos diretamente.

"""

import logging
import math

class Cola(object):
    def numbers_and_aritmetics_operations(self):
        exponecial = 2**3           # 2^3 = 8
        integer_division = 9/2      # 4
        float_division = 9.0/2.0    # 4.5
        floor_division = 9.0//2.0   # 4.0

    def comparison_operators(self):
        print (2 == 2)              # True
        print (2 != 2)              # False
        print (2 <> 3)              # True
        print (3 > 1)               # True
        print (4 < 3)               # False

    def strings_and_console(self):
        abc = "abcdefghijklmnopqrstuvwxyz"
        print (abc[0])              # Exibirá a letra 'a'
        print (abc[2:5])            # Exibirá de a[2] até a[4]
        print (abc[1:5:2])          # Exibirá de a[1] até a[4] de duas em duas letras
        print (abc[::-1])           # Exibirá a  lista de trás pra frente
        print (abc[:5])             # Exibirá de a[0] até a[4]
        print ('repeticao'*5)       # Escreverá a palavra 'repeticao' 5 vezes
        print ('conca' + 'tenacao') # Faz uniao das palavras
        print ('a' in abc)          # Retornará True caso a letra 'a' esteja na string abc
        print ('O numero %d é maior que %.3f.' % (10,5.5))
        print (
        """
            Tudo o que estiver aqui no meio será printado com a mesma formatação.
        Isso pode ser útil pra escrever um comentário grande, ou descrever algo complexo. (Mas é preciso utilizar com cuidado pra não deixar o código ilegível ou confuso)
        """
        )

    def configuring_and_using_log(self):
        """
        DEBUG : Vai exibir todas as mensagens
        INFO
        WARNING
        ERROR
        CRITICAL
        """
        logging.basicConfig(format='[%(asctime)s] - %(levelname)s: %(message)s', level=logging.DEBUG, filename="aprendendo.log")
        logger = logging.getLogger(__name__)

        logger.debug("Apenas um debug")
        logger.info("Uma informação que ajuda muito")
        logger.warning("Um aviso! Fica esperto!")
        logger.error("Erroooou!!!")
        logger.critical("TÁ PEGANDO FOGO, BICHO!")

    def variable_scope(self):
        a = 10
        for i in range(0,4):
            x = a*i
            print (x)
            result = x
        print ("Resultado final: %d" % result)

    def loops(self):
        list = range(0,10)          # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in list:
            print (i)

        odd_numbers = [x for x in range(0,11) if x % 2 == 1]
        print (odd_numbers)         # [1, 3, 5, 7, 9]

        squares = [ x**2 for x in range(0,6)]
        print (squares)             # [0, 1, 4, 9, 16, 25]

        array = [1,2,4,5,6]
        while(len(array)):
            print (array.pop())

    @staticmethod
    def static_method():
        print ("Estamos em um método estático!")

if __name__ == '__main__':
    cola = Cola()
    cola.numbers_and_aritmetics_operations()
    cola.comparison_operators()
    cola.strings_and_console()
    cola.configuring_and_using_log()
    cola.variable_scope()
    Cola.static_method()
    cola.loops()
