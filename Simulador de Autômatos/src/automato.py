#!/usr/bin/env python

'''
    A classe Automato possui campos e métodos que representam autômatos finitos determinísticos
    e autômatos finitos não-determinísticos.
'''

from estado import Estado #importação da classe Estado

__author__ = "Alisson Jaques"
__copyright__ = "Copyright 2021, Projeto Autômatos"
__credits__ = ["Alisson Jaques"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Alisson Jaques"
__email__ = "alissson.1651712@discente.uemg.br"
__status__ = "Protótipo"

class Automato:
    """
        A classe Automato possui campos e métodos que representam um autômato finito determinístico (AFD)
        ou um autômato finito não determinístico (AFN).
    """
    def __init__(self, alfabeto, estadoInicial, estadoDeAceitacao, transicoes):
        """
            O construtor para classe Automato que recebe um alfabeto, um estado inicial, um vetor de estados de aceitações e
            um vetor de transições, inicializando os campos da classe com os mesmos.
            
            :parâmetro alfabeto: o alfabeto do autômato
            :parâmetro estadoInicial: o estado inicial do autômato
            :parâmetro estadoDeAceitação: o vetor de estados de aceitação
            :parâmetro transicoes: o vetor de transições
        """
        self.__estados = [];
        self.__alfabeto = alfabeto
        self.__estadoInicial = estadoInicial
        self.__estadoDeAceitacao = estadoDeAceitacao
        self.__transicoes = transicoes

    @property
    def estados(self):
        """
            O método estados faz um get do vetor de estados, encapsulado na classe Automato.
            :retorno: o vetor de estados encapsulado no autômato
        """
        return self.__estados

    def ehEstadoDeAceitacao(self, estado):
        """
            O método ehEstadoDeAceitacao recebe como argumento o estado e verifica se o mesmo é um dos 
            estados de aceitação do autômato.
            
            :parâmetro estado: o estado do autômato
            :retorno: o valor booleano true, se o estado for de aceitação, ou false, caso contrário.
        """
        if(estado in self.__estadoDeAceitacao): # se o estado atual for de aceitação
            return True # retorna true
        else: # senão
            return False # retorna false

    def configuraEstados(self):
        """
            O método configuraEstados percorre o vetor de transições e preenche o vetor de 
            estados, com os novos estados criados. Cada novo estado possui uma ou mais regras de 
            transição associada a ele, bem como a informação de este ser um estado de aceitação ou
            não.            
        """
        for estado, transicao in self.__transicoes.items(): # enquanto não percorrer todo o vetor de transições, faça:
            newEstado = Estado(estado, self.ehEstadoDeAceitacao(estado),
                              self.__alfabeto, transicao) # cria um novo objeto estado
            self.estados.append(newEstado) # preenche o indice atual do vetor de estados com o novo objeto

    def buscaEstado(self, nome):
        """
            O método buscaEstado busca um estado no vetor de estados.
            :parâmetro nome: o nome do estado
            :retorno: o estado correspondente à busca
        """
        for estado in self.__estados: # enquanto não percorrer todo o vetor de estados, faça:
            if(estado.nome == nome): # se achar o estado procurado
                return estado # retorna o estado encontrado

    def aceitaCadeia(self, cadeia):
        """
            O método aceitaCadeia recebe como argumento uma cadeia de caracteres e verifica se essa
            cadeia faz parte ou não do alfabeto do autômato.
            :parâmetro cadeia: a cadeia a ser lida pelo autômato
            :retorno: true se a acadeia pertencer ao alfabeto, false caso contrário
        """
        for simbolo in cadeia: # enquanto não percorrer todos os caracteres da cadeia, faça:
            if simbolo not in self.__alfabeto: # se a cadeia tiver símbolos que não pertencem ao alfabeto do autômato
                return False # retorna falso
        return True # senão, retorna true

    def testaAutomato(self, cadeia):
        """
            O método testaAutomato recebe como argumento uma cadeia de caracteres e verifica se essa cadeia
            é ou não aceita pelo autômato, informando no terminal essa informação.
            :parâmetro cadeia: a cadeia a ser lida pelo autômato
        """
        cadeia = list(cadeia)

        if(self.aceitaCadeia(cadeia)): # se a cadeia pertencer ao autômato
            estados = [] # declara um vetor de estados
            estadoDeAceitacao = self.buscaEstado(self.__estadoInicial) # seta o estado de aceitação com o estado inicial

            estados.append(estadoDeAceitacao.nome) # inseri no vetor de estados o estado inicial

            for simbolo in cadeia: # enquanto não percorrer todos os símbolos da cadeia, faça:
                estadoDeAceitacao = self.buscaEstado(estadoDeAceitacao.move(simbolo)) # o estado de aceitação recebe um novo estado a partir da leitura do símbolo da cadeia
                estados.append(estadoDeAceitacao.nome) # guarda o novo estado no vetor de estados

            estados = " -> ".join(estados)
            print("\nEstados Visitados: " + estados) # imprimi no terminal os estados visitados, na sequência da leitura

            if estadoDeAceitacao.ehEstadoDeAceitacao: # se o último estado gravado for um estado de aceitação
                print("\nO autômato aceita a cadeia informada!\n") # informa no terminal que o autômato aceita a cadeia
            else: # senão
                print("\nO autômato não aceita a cadeia informada!\n") # informa no terminal que o autômato não aceita a cadeia
        else: # senão
            print(
                "\nA cadeia informada não pertence ao alfabeto do autômato!\n") # informa no terminal que a cadeia não pertence ao alfabeto do autômato

    def __str__(self):
        """
            O método  _str_ retorna uma string que representa o conteúdo do vetor de transições,
            ou seja, retorna as transições ocorridas no autômato, formatadas. Este método pode ser 
            chamado em scripts Python.
            : retorno: uma string que representa as transições ocorridas no autômato
        """
        transicoes = [] # declara o vetor string de transições
        for x, y in self.__transicoes.items(): # enquanto não percorrer todo o vetor de transições, encapsulado na classe, faça:
            transicao = x + ":" + str(y) # a variável local transicao recebe uma transição formatada
            transicoes.append(transicao) # a variável local é armazenada no vetor de string
        trancictions = "\n".join(transicao) # o vetor transictions recebe o conteúdo da variável local e o formata em um padrão específico
        return trancictions # retorna o vetor com os campos formatados

    def __repr__(self):
        """
            O método _repr_ não possui argumentos e retorna as transições ocorridas no autômato, formatadas.
            Este método é útil em chamadas de impressão, no console do Python.
            : retorno: uma string com os valores do vetor de transições formatados
        """
        return self.__str__()
