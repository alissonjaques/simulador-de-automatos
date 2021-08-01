#!/usr/bin/env python

"""
    A função main permite a execução desse projeto. Ela demonstra usos da classe Automato e Estado.
    Esta função representa um programa de computador que recebe um arquivo contendo um autômato e testa
    cadeias nesse autômato.
"""

import json # importação do autômato criado pelo usuário
from automato import Automato # importação da classe Automato

__author__ = "Alisson Jaques"
__copyright__ = "Copyright 2021, Projeto Autômatos"
__credits__ = ["Alisson Jaques"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Alisson Jaques"
__email__ = "alissson.1651712@discente.uemg.br"
__status__ = "Protótipo"

def main():
    """
        O método main não possui argumentos e representa um programa de computador que testa cadeias de autômatos, representados em um
        arquivo.
    """
    def lerAutomato():
        """
            O método lerAutomato não recebe argumentos, ele lê o arquivo, inserido pelo usuário, e cria variáveis correspondentes aos 
            conteúdos deste arquivo. Finalizado este processo, este método retorna um autômato que representa o autômato inserido pelo usuário.
            : retorno: o autômato correspondente ao arquivo inserido pelo usuário 
        """
        with open('InsiraSeuAutomatoAqui\\seuAutomato.json') as file:
            automatoJson = json.load(file) # a variável automatoJson representa o arquivo de autômato

        # variáveis auxiliares são criadas e inicializadas com os dados correspondentes do arquivo
        alfabeto = automatoJson["alfabeto"]
        estadoInicial = automatoJson["estadoInicial"]
        estadoDeAceitacao = automatoJson["estadoDeAceitacao"]
        transicoes = automatoJson["transicoes"]

        newAutomato = Automato(alfabeto, estadoInicial, estadoDeAceitacao, transicoes) # cria um objeto autômato, passando ao construtor desse objeto
                                                                                       # as variáveis auxiliares declaradas e inicializas anteriormente
        newAutomato.configuraEstados() # configura o vetor de estados do objeto newAutomato

        return newAutomato # retorna o autômato criado

    while True: # enquanto for verdadeiro, faça:
        print("**************************************** Simulador de Autômatos *******************************************")
        print("-----------------------------------------------------------------------------------------------------------")
        # solicita ao usuário que escolha uma opção
        print("Escolha uma das seguintes opções: \n\n1 - Ler Manual \n2 - Testar Cadeia no Automâto\n3 - Encerrar o Programa")
        print("-----------------------------------------------------------------------------------------------------------")
     
        opcaoEscolhida = int(input("Opção escolhida: ")) # inicializa a variável escolha com o dado fornecido:

        if opcaoEscolhida == 1: # se o usuário escolher ler o manual, faça:         
            print("-----------------------------------------------------------------------------------------------------------")
            print("Este Simulador de Autômatos possibilita a manipulação de autômato finitos determinísticos e não determinísticos.\n")
            print("Para poder testar cadeia nos autômatos é necessário inserir um autômato no sistema, na pasta coloqueAquiSeuAutomato.\n")
            print("O autômato deve ser descrito em um arquivo.json (há alguns exemplos na pasta mencionada anteriormente) no mesmo padrão\n")
            print("dos exemplos. A documentação do software pode ser gerada pelo console do computador. A ideia é que você utilize essa\n")
            print("ferramenta para auxílio no estudo da teoria dos autômatos. A ferramenta foi criada considerando as boas práticas de\n")
            print("desenvolvimento e permite extenções para melhorias. Ótimos estudos!")
            print("-----------------------------------------------------------------------------------------------------------")
        elif opcaoEscolhida == 2: # se o usuário escolher testar cadeias no autômato, faça:
            cadeiaInformada = input(
                "Informe uma cadeia: ") # solicita ao usuário que entre com uma cadeia
            automato = lerAutomato() # configura o objeto autômato com o arquivo, criado pelo usuário
            automato.testaAutomato(cadeiaInformada) # testa a cadeia informada no autômato
            print("-----------------------------------------------------------------------------------------------------------")
        elif opcaoEscolhida == 3: # se o usuário escolher encerrar o programa, faça:
            print("\nPrograma Encerrado.") # informa no terminal que o programa foi encerrado
            break;
        else: # senão
            print("\nOpção inválida, tente novamente!")
            
    print("-----------------------------------------------------------------------------------------------------------")
    print("***********************************************************************************************************")
if __name__ == "__main__":
    main()
