#def deixar maiucuslo(frase):
#print("frase.upper()")





def menu():
    palavra=input("\ndigite a string:")
    while True:
        print("\t\t---MENU---\t\t")
        print("1-tranformaçao de caixa")
        print("2-fatiamente e inversao")
        print("3-substituiçao e remoçoes")
        print("4-contagens e buscas")
        print("5-verificaçoes de conteudo")
        print("6-conversao para lista")
        print("7-divisao e junçao de palavras")
        print("0-sair")
        op=int(input("\ndigite a opçao acima: "))



def menu_transformaçao_De_caixa():
    while True:
        print("\t\t---menu transformaçao---\t\t")
        print("1-maiusculo")
        print("2-minusculo")
        print("3-capitalizar")
        print("4-estilo texto")
        print("0-sair")
        op=int(input("\ndigite a opçao acima:"))




def menu_fatiamento_e_inversao():
    while True:
        print("\t\t---menu de fatiamento e inversao---\t\t")
        print("1-mostrar como acessar a partes da string")
        print("2-inverter a ordem")
        print("0-sair")
        op=int(input("\ndigite uma opçao acima: "))



def menu_substituiçao_e_remoçoes():
    while True:
        print("\t\t---menu de substituiçao---\t\t")
        print("1-trocar caractere")
        print("2-eliminar letras especificas")
        print("0-sair")
        op=int(input("\ndigite sua opçao acima:"))


def menu_contagens_e_buscas():
     while True:
        print("\t\t---menu de contagens---\t\t")
        print("1-contar quantas vezes uma caractere aparece em uma string")
        print("2-encontrar posiçao")
        print("0-sair")
        op=int(input("\ndigite sua opçao acima:"))


def menu_verificaçoes_de_conteudo():
     while True:
        print("\t\t---menu de verificaçao---\t\t")
        print("1-descobri se a string é composta so por letras,numeros,espaços:")
        print("0-sair")
        op=int(input("\ndigite sua opçao acima:"))


def menu_conversao_para_lista():
     while True:
        print("\t\t---menu de verificaçao---\t\t")
        print("1-trasnformar a string em uma lista de caractere")
        #transforma a string em um vetor 
        print("0-sair")
        op=int(input("\ndigite sua opçao acima:"))


def menu_divisao_e_junçao_de_palavras():
     while True:
        print("\t\t---menu de verificaçao---\t\t")
        print("1-separar a frase em palavras e uni-las de forma diferentes")
        print("0-sair")
        op=int(input("\ndigite sua opçao acima:"))
