#Gabriel Sposito Conciani

#Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  fazer  um  programa,  usando  a
#linguagem de programação que desejar, que seja capaz de validar expressões de lógica propisicional
#escritas em latex e definir se são expressões gramaticalmente corretas. Você validará apenas a forma
#da expressão (sintaxe).
#A entrada será fornecida por um arq de textos que será carregado em L de comando,
#com a seguinte formatação:
#1. Na primeira L deste arq existe um número inteiro que informa quantas expressões
#lógicas estão no arq.
#2. Cada uma das Ls seguintes somarém uma expressão lógica que deve ser validada.
#A saída do seu programa será no terminal padrão do sistema e Cituirá de uma L de saída
#para cada expressão lógica de entrada somarendo ou a palavra valida ou a palavra inválida e nada mais.
#Gramática:
#Formula=Cante|prop|FormulaUnaria|FormulaBinaria.
#Cante="T"|"F".
#prop=[a−z0−9]+
#FormulaUnaria=AbreParen OperadorUnario Formula FechaParen
#FormulaBinaria=AbreParen OperatorBinario Formula Formula FechaParen
#AbreParen="("
#FechaParen=")"
#OperatorUnario="¬"
#OperatorBinario="∨"|"∧"|"→"|"↔"
#Cada  expressão  lógica  avaliada  pode  ter  qualquer  combinação  das  operações  de  negação,
#conjunção, disjunção, implicação e bi-implicação sem limites na combiação de preposições e operações.
#Os valores lógicos True e False estão representados na gramática e, como tal, podem ser usados em
#qualquer expressão de entrada.
#Para  validar  seu  trabalho,  você  deve  incluir  no  repl.it,  no  mínimo  três  arqs  somarendo
#números  diferentes  de  expressões  proposicionais.  O  professor  irá  incluir  um  arq  de  testes  extra
#para validar seu trabalho. Para isso, caberá ao professor incluir o arq no seu repl.it e rodar o seu
#programa carregando o arq de testes.

#Bibliotecas usadas
from pylatexenc.latex2text import LatexNodes2Text
import re

#Menu para abrir arquivos
print('''Qual arquivo deverá ser analisado?''')
print('Texto1')
#para abrir Arquivo 1
print('Texto2')
#para abrir Arquivo 2
print('Texto3')
#para abrir Arquivo 3   

op = str(input('Nome do arquivo escolhido: '))
#Abre o arquivo
arq = open(op + ".txt", 'r')
#Operadores
L = int(arq.readline())
#Operadores

def organiza(F):
    #Organiza a expressão em uma lista
    if F.count('\n') != 0:
        #Remove o \n
        F = re.sub(r'\n', '', F)
        #Remove o \n
    else:
        pass
    return F

#Operadores
ParentesesAberto = '('
C = ('T', 'F')
Unario = '¬'
Binario = ('∧', '↔', '∨', '→')
ParentesesFechado = ')'


def Pro(caractere):
    #Verifica se é uma proposição válida
    
    l = list(map(chr, range(97, 123)))
    #Letras minúsculas
    ln = list(map(chr, range(48, 58)))
    #Números

    if caractere in l:
        #Verifica se é uma letra
        return True
    elif caractere in ln:
        #Verifica se é um número
        return True
    else:
        #Se não for uma letra ou um número
        return False


def FU(caractere):
    #Verifica se o operador unário é válido
    
    if caractere == Unario:
        #Verifica se é um operador unário
        if caractere in Simbolo1s[-2]:
            #Verifica se o operador unário está na posição correta
            return False
        else:
            #Verifica se o operador unário está na posição correta
            return True


def FB(caractere):
    #Verifica se o operador binário é válido
    
    if caractere in Binario:
        #Verifica se é um operador binário
        if caractere in Simbolo1s[-2]:
            #Verifica se o operador binário está na posição correta
            return False
        else:
            #Verifica se o operador binário está na posição correta
            return True


def I(Simbolo1s, Sta):
    
    NumeroParenteses = 0
    #Conta o número de parenteses
    Numero = None
    #Conta o número de letras e números
    for i, caractere in enumerate(Simbolo1s):
        if F == "\n":
            exit()
            return True
        if Sta == "VerificaParenteses": 
            #Verifica se os parenteses estão corretos

            if caractere == ParentesesAberto: 
                #Verifica se o parenteses está aberto
                Sta = "VerificaOperador"
                NumeroParenteses += 1
                continue
            elif caractere in C:
                #Verifica se é um valor lógico
                if len(Simbolo1s) == 1:
                    return True
                else:
                    #Se não for o último caractere
                    return False
            else:
                #Se não for um valor lógico
                return False
        
        if Sta == "VerificaOperador":
            #Verifica se o operador é válido

            if FU(caractere):
                #Verifica se o operador unário é válido
                Sta = "Unario"
                Numero = True
                continue
            elif FB(caractere):
                #Verifica se o operador binário é válido
                Sta = "Binario"
                Numero = False
                continue
            else:
                # Verifica se o operador é válido
                return False

        if Sta == "Unario":
            #Verifica se o operador unário é válido

            if caractere == ParentesesAberto:
                #Verifica se o parenteses está aberto
                Sta = "VerificaOperador"
                NumeroParenteses += 1
                continue

            if Pro(caractere):
                #Verifica se é uma letra ou número
                Sta = "Simbolo1"
                continue

            if caractere == ParentesesFechado:
                #Verifica se o parenteses está fechado
                Sta = "VerificaParentesesFechado"
                NumeroParenteses -= 1
                continue

            if caractere in C:
                #Verifica se é um valor lógico
                Sta = "VerificaParentesesFechado"
                continue

            else:
                #Se não for um valor lógico
                return False

        if Sta == "Binario":
            #Verifica se o operador binário é válido

            if caractere == ParentesesAberto:
                #Verifica se o parenteses está aberto
                Sta = "VerificaOperador"
                NumeroParenteses += 1
                continue

            if Pro(caractere):
                #Verifica se é uma letra ou número
                Sta = "Simbolo1"
                continue

            if caractere == ParentesesFechado:
                #Verifica se o parenteses está fechado
                Sta = "VerificaParentesesFechado"
                NumeroParenteses -= 1
                continue

            if caractere in C:
                #Verifica se é um valor lógico
                Sta = "Binario"
                continue

        if Sta == "Simbolo1":
            #Verifica se o primeiro símbolo é válido

            if caractere != ParentesesFechado:
                #Verifica se o parenteses está fechado

                if caractere not in list(map(chr, range(48, 58))):
                    #Verifica se é um número

                    if caractere in list(map(chr, range(97, 123))):
                        #Verifica se é uma letra
                        if Numero is True and s[i].isspace() is True:
                            #Verifica se é um número
                            return False
                        continue
                    else:
                        #Se não for uma letra
                        return False
                else:
                    #Se não for um número
                    Sta = "Simbolo2"

            else:
                #Se não for um parenteses fechado
                Sta = "VerificaParentesesFechado"

        if Sta == "Simbolo2":
            #Verifica se o segundo símbolo é válido

            if caractere != ParentesesFechado:
                #Verifica se o parenteses está fechado

                if caractere not in list(map(chr, range(97, 123))):
                    #Verifica se é uma letra
                    
                    if list(map(chr, range(48, 58))):
                        #Verifica se é um número
                        continue
                    else:
                        #Se não for um número
                        return False
                else:
                    #Se não for uma letra
                    Sta = "Simbolo1"

            else:
                #Se não for um parenteses fechado
                Sta = "VerificaParentesesFechado"

        if Sta == "VerificaParentesesFechado":
            #Verifica se o parenteses está fechado

            if caractere == ParentesesAberto:
                #Verifica se o parenteses está aberto
                Sta = "VerificaOperador"
                NumeroParenteses += 1
                continue

            elif caractere == ParentesesFechado:
                #Verifica se o parenteses está fechado
                Sta = "VerificaParentesesFechado"
                Numero = None
                NumeroParenteses -= 1
                if caractere in Simbolo1s[-1]:
                    # Verifica se o parenteses está na posição correta
                    if NumeroParenteses == 0:
                        #Verifica se o número de parenteses está correto
                        return True
                else:
                    #Se não estiver na posição correta
                    continue

            elif Pro(caractere):
                #Verifica se é uma letra ou número
                Sta = "Simbolo1"

            else:
                #Se não for uma letra ou número
                return False




while L > 0:
    #Verifica se o número de linhas é maior que 0
    Sta = "VerificaParenteses"
    #Verifica se os parenteses estão corretos
    NumeroParenteses = 0
    #Conta o número de parenteses
    F = arq.readline()
    #Lê a linha
    s = LatexNodes2Text().latex_to_text(organiza(F))
    #Organiza a linha
    Simbolo1s = re.findall(r'\S', s)
    #Separa os símbolos
    Simbolo1Binario = Simbolo1s.count(Unario)
    #Conta o número de operadores unários
    Simbolo1sParentesesAberto = Simbolo1s.count(ParentesesAberto)
    #Conta o número de parenteses abertos
    Simbolo1sParentesesFechados = Simbolo1s.count(ParentesesFechado)
    #Conta o número de parenteses fechados
    Simbolo1sBinario = Simbolo1s.count(Binario)
    #Conta o número de operadores binários
    if NumeroParenteses == 0 and I(Simbolo1s, Sta):
        #Verifica se o número de parenteses está correto
        if Simbolo1Binario > 3:
            #Verifica se o número de operadores unários é maior que 3
            if Simbolo1sParentesesAberto and Simbolo1sParentesesFechados == Simbolo1Binario and Simbolo1sBinario == 0:
                #Verifica se o número de parenteses está correto
                print("Inválida")
        else:
            #Se não for maior que 3
            print("Válida")
    else:
        #Se não estiver correto
        print("Inválida")
    L -= 1
    #Decrementa o número de linhas