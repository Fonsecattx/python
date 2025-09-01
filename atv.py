
lista_status=[]
lista_responsavel=[]
lista_titulo=[]

def menu():
    while True:
        print("\t\tMENU\t\t")
        print("1-adicionar tarefas ")
        print("2-listar tarefas ")
        print("3-atualizar tarefas")
        print("4-remover tarefas ")
        print("5-filtrar tarefas por status ")
        op=int(input("\ndigite uma opçao acima: "))

        if op==1: 
            adicionar()
        elif op ==2:
            listar()
        elif op ==3:
            atualizar()





def adicionar():
    while True: 
        print("\t\tMENU ADICIONAR\t\t")
        ti=input("digite seu titulo: ")
        res=input("digite o nome do seu rsponsavel: ")
        sta=input("\ndigite seu status inicial: ")
        lista_titulo.append(ti)
        lista_responsavel.append(res)
        lista_status.append(sta)
        print("\ntarefa adicionanda")
        op=int(input("\n1-continuar cadastrando\n0-sair\n"))
        if op==1:
            continue
        elif op==0:
            break
        else:
            print("numero invalido")



def listar():
    for indice,conteudo in enumerate(lista_titulo):
        print(f"\nID: {indice}\n NOME: \n{conteudo}\n RESPONSAVEL:\n {lista_responsavel}\n STATUS:\n{lista_status}")
  

def atualizar():
    print("\t\tMENU ALTERAR\t\t")
    op=int(input("escolha quem voce deseja alterar\n1-status\n2-responsavel"))
    if op==1:
        for status in enumerate(lista_status):
            alt=input("\ndigite o status que deseja alterar: ")
            if alt==status:
                novo_status=input("digite o seu novo status: ")
                lista_status.append(novo_status)
                print("\n Status aletrado com sucesso ")
                break
    elif op ==2:
        for responvavel in enumerate(lista_responsavel): 
            alt=input("digite o nome do responavel que deseja alterar:  ")
            if alt==responvavel:
                novo_responsavel=input("digite o seu novo nome do responsavel:  ")
                lista_responsavel.append(novo_responsavel)
                print("\n responsavel alterado com sucesso: ")
                break
    else:
        print("numero invalido")  


def remover():
    print("\t\tMENU DE REMOVER\t\t")
    id=int(input("digite o id da taerefa: "))

menu()