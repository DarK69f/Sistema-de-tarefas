prioridades_validas = ["urgente", "alta", "média", "baixa"]
status_validos = ["pendente", "fazendo", "concluído"]
origens_validas = ["email", "telefone", "chamado do sistema"]
 
 
Tarefas = []
 
 
def add_tarefa(titulo, prioridade, status, origemTarefa):
    tarefinhas = {
        "Título": titulo, "Prioridade": prioridade, "Status": status, "Origem": origemTarefa
    } 
    Tarefas.append(tarefinhas)
 
 
def atualizar_tarefa():
    if not Tarefas:
        print("Não há tarefas para atualizar!\n")
        return
 
 
    print("\nTarefas disponíveis:")
    for i, tarefa in enumerate(Tarefas):
            print(f"[{i}] Título: {tarefa['Título']}, Prioridade: {tarefa['Prioridade']}, Status: {tarefa['Status']}, Origem: {tarefa['Origem']}")
 
 
    try:
            indice = int(input("\nDigite o número da tarefa que deseja atualizar: "))
            tarefa = Tarefas[indice]
    except (ValueError, IndexError):
            print("❌ Índice inválido.")
            return
 
 
    print("\nO que deseja atualizar?")
    print("Título - [1]")
    print("Prioridade - [2]")
    print("Status - [3]")
    print("Origem - [4]")
    escolha = input(": ")
 
 
    if escolha == "1":
        novo_titulo = input("Novo título: ")
        tarefa["Título"] = novo_titulo
    elif escolha == "2":
        prioridades_validas = ["urgente", "alta", "média", "baixa"]
        while True:
            nova_prioridade = input("Nova prioridade (Urgente, Alta, Média, Baixa): ").lower()
            if nova_prioridade in prioridades_validas:
                tarefa["Prioridade"] = nova_prioridade
                break
            else:
                print("❌ Prioridade inválida.")
    elif escolha == "3":
            status_validos = ["pendente", "fazendo", "concluído"]
            while True:
                novo_status = input("Novo status (Pendente, Fazendo, Concluído): ").lower()
                if novo_status in status_validos:
                    tarefa["Status"] = novo_status
                    break
                else:
                    print("❌ Status inválido.")
    elif escolha == "4":
        origens_validas = ["email", "telefone", "chamado do sistema"]
        while True:
            nova_origem = input("Nova origem (Email, Telefone, Chamado do sistema): ").lower()
            if nova_origem in origens_validas:
                tarefa["Origem"] = nova_origem
                break
            else:
                print("❌ Origem inválida.")
    else:
        print("❌ Opção inválida.")
 
 
        print("\n✅ Tarefa atualizada com sucesso!\n")

def mostrarTarefas():
    print("\nSiga a lista das tarefas: 👇")
    for tarefas in Tarefas:
        print(f"\nTítulo: {tarefas['Título']}, Prioridade: {tarefas['Prioridade']}, Status: {tarefas['Status']}, Origem: {tarefas['Origem']}")

def ProcessoAddTarefa():
    print("Defina o título da tarefa: ")
    titulo = str(input(""))
    while True:
        prioridade = input("\nDefina a prioridade da tarefa ('Urgente, Alta, Média ou Baixa'): \n").lower()
        if prioridade in prioridades_validas:
            break
        else:
            print("❌ Prioridade inválida. Tente novamente.")
    while True:
        status = input("\nDefina o status da tarefa ('Pendente, Fazendo ou Concluído'): \n").lower()
        if status in status_validos:
            break
        else:
            print("❌ Status inválido. Tente novamente.")
    while True:
        origemTarefa = input("\nDefina a origem da tarefa ('Email, Telefone, Chamado do sistema'): \n").lower()
        if origemTarefa in origens_validas:
            break
        else:
            print("❌ Origem inválida. Tente novamente.")
 
    add_tarefa(titulo, prioridade, status, origemTarefa)
 
 
 
while True:
 
 
    print("=====================================================")
    print("                  Menu de Tarefas                    ")
    print("=====================================================")
    print("Adicionar tarefa - [1]")
    print("atualizar tarefas - [2]")
    print("visualizar tarefas - [3]")
    print("sair - [4]\n")
    try:
        interacao = int(input(": "))
    except (ValueError, IndexError):
        print("\n ❌ Opção inválida!\n")
 
 
    match interacao:
        case 1:
            ProcessoAddTarefa()
        case 2:
            atualizar_tarefa()
        case 3:
            if not Tarefas:
                print("\nNão há tarefas por enquanto, digite '1' para adicionar uma tarefa nova!!\n")
            else:
                mostrarTarefas()
        case 4:
            break
        case _:
            print("\n❌ Opção inválida!\n")