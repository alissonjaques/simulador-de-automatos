#!/usr/bin/env python

"""
    A classe Estado possui campos e métodos que representam o estado de um autômato.
"""
__author__ = "Alisson Jaques"
__copyright__ = "Copyright 2021, Projeto Autômatos"
__credits__ = ["Alisson Jaques"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Alisson Jaques"
__email__ = "alissson.1651712@discente.uemg.br"
__status__ = "Protótipo"

class Estado:
    """
        Representa o estado do autômato e possibilida a transição de um estado
        para outro.
    """
    def __init__(self, nome, estado, alfabeto, transicao):
        """
            O construtor para a classe Estado que recebe o nome, o estado, o alfabeto e a transição,
            inicializando os campos da classes com os mesmos.
            
            :parâmetro nome: o nome do estado
            :parâmetro estado: um valor booleano que indica se o estado é ou não de aceitação
            :parâmetro alfabeto: o alfabeto do autômato
            :parâmetro transicao: a transição do estado atual para um estado novo
        """
        self.nome = nome
        self.ehEstadoDeAceitacao = estado
        self.alfabeto = alfabeto
        self.transicao = transicao

    def __str__(self):
        """
            O método _str_ retorna uma string contendo o conteúdo do campo nome, da classe
            Estado. Será sempre útil em chamadas, em scripts Python.
            
            :retorno: o nome do objeto encapsulado
        """
        return self.nome

    def __repr__(self):
        """
            O método _repr_ permite representar o campo nome, do objeto da classe Estado, como uma string.
            Será sempre útil em chamadas, no console do Python.
            
            :retorno: a representação do campo nome, do objeto da classe, como uma string
        """
        return self.__str__()

    def move(self, simbolo):
        """
            O método move recebe um símbolo como parâmetro e retorna o novo estado do
            autômato.
            
            :parâmetro simbolo: o símbolo de entrada no altômato
            :retorno: o novo estado
        """
        return self.transicao[simbolo]
