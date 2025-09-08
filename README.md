
Lista_tarefas = []
Responsaveis = []
Status = []
Tarefas_pendentes = []
Tarefas_em_andamento = []
Tarefas_concluidas = []


def adicionar_tarefa():
    print("\nAdicionar tarefa") 

    while True:
        titulo = input("Digite o título da tarefa: ").strip()
        if titulo == "":
          print("O título não pode ser vazio tente de novo: ")
        if not titulo.replace(" ", "").isalpha():
         print(" O título não pode conter números ou caracteres especiais. Use apenas letras.\n")
         continue
        
          
        while True:
         responsavel = input("Digite o responsável: ").strip()
         if responsavel == "":
          print("O responsável não pode ser vazio tente de novo")
          continue

         status = "pendente"
         Tarefas_pendentes.append(titulo)

         Lista_tarefas.append(titulo)
         Responsaveis.append(responsavel)
         Status.append(status)

         print(f"Tarefa '{titulo}' adicionada como PENDENTE\n")
         return

def listar_tarefas():
    if len(Lista_tarefas) == 0:
        print("Nenhuma tarefa cadastrada\n")
        return

    print("\t\t\tLista de tarefas")
    print(" \tÍNDICE \t| TÍTULO \t| RESPONSÁVEL \t| STATUS")
    for i in range(len(Lista_tarefas)):
        print(f"\t{i}\t|{Lista_tarefas[i]}\t\t|{Responsaveis[i]}\t\t|{Status[i]}")

def atualizar_tarefa():
    if len(Lista_tarefas) == 0:
        print("Nenhuma tarefa para atualizar\n")
        return

    listar_tarefas()

    while True:
        id_input = input("Digite o índice da tarefa para atualizar ").strip()
        if id_input.isdigit():
            indice = int(id_input)
            if 0 < indice < len(Lista_tarefas):
                break
        print("Índice inválido tente de novo")

    print("1 - Alterar responsável")
    print("2 - Alterar status")

    while True:
        opcao = input("Escolha: ").strip()
        if opcao in ("1", "2"):
            break
        print("Opção inválida tente de novo")

    if opcao == "1":
        while True:
            novo_resp = input("Novo responsável ").strip()
            if novo_resp != "":
                Responsaveis[indice] = novo_resp
                break
            print("O responsável não pode ser vazio tente de novo")

    elif opcao == "2":
        print("Escolha o novo status")
        print("1 - Pendente")
        print("2 - Em andamento")
        print("3 - Concluída")
        while True:
            novo_status = input("Digite a opção ").strip()
            if novo_status == "1":
                Status[indice] = "pendente"
                break
            elif novo_status == "2":
                Status[indice] = "em andamento"
                break
            elif novo_status == "3":
                Status[indice] = "concluída"
                break
            else:
                print("Opção inválida tente de novo")

    print("Tarefa atualizada\n")

def remover_tarefa():
    if len(Lista_tarefas) == 0:
        print("Nenhuma tarefa para remover\n")
        return

    listar_tarefas()

    while True:
        id_input = input("Digite o índice da tarefa para remover ").strip()
        if id_input.isdigit():
            indice = int(id_input)
            if 0 < indice < len(Lista_tarefas):
                break
        print("Índice inválido, tente de novo ")

    print(f"Tarefa {Lista_tarefas[indice]} removida \n")

    Lista_tarefas.pop(indice)
    Responsaveis.pop(indice)
    Status.pop(indice)


def filtrar_tarefas():
    if len(Lista_tarefas) == 0:
        print("Nenhuma tarefa para filtrar\n")
        return

    while True:
        status = input("Digite o status para filtrar (pendente, em andamento, concluida) ").strip().lower()
        if status in ("pendente", "em andamento", "concluída"):
            break
        print("Status inválido tente de novo")

    print(f"\nTarefas com status {status}")
    achou = False
    for i in range(len(Lista_tarefas)):
        if Status[i] == status:
            print(f"{i} | {Lista_tarefas[i]} - {Responsaveis[i]}")
            achou = True
    if not achou:
        print("Nenhuma tarefa encontrada com esse status\n")
    print()

while True:
    print("\n menu")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Atualizar tarefa")
    print("4 - Remover tarefa")
    print("5 - Filtrar tarefas por status")
    print("6 - Sair")

    opcao = input("\nEscolha uma opção:").strip()
    print("-----------------------------------------")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        atualizar_tarefa()
    elif opcao == "4":
        remover_tarefa()
    elif opcao == "5":
        filtrar_tarefas()
    elif opcao == "6":
        print("Saindo...")
        break
    else:
        print("Opção inválida tente de novo\n")
