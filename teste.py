tarefas = []

def mostrar_menu():
    print("\n==== MENU ====")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Marcar tarefa como concluída")
    print("4 - Remover tarefa")
    print("5 - Sair")

def adicionar_tarefa():
    nome = input("Digite a descrição da tarefa: ")
    tarefa = {"nome": nome, "concluida": False}
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    print("\n==== TAREFAS ====")
    for i, tarefa in enumerate(tarefas):
        status = "✅" if tarefa["concluida"] else "❌"
        print(f"{i + 1}. {tarefa['nome']} [{status}]")

def marcar_concluida():
    listar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa que deseja marcar como concluída: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefas[indice]["concluida"] = True
            print("Tarefa marcada como concluída!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Digite um número válido.")

def remover_tarefa():
    listar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa que deseja remover: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefas.pop(indice)
            print("Tarefa removida com sucesso!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Digite um número válido.")

def main():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_tarefa()
        elif escolha == "2":
            listar_tarefas()
        elif escolha == "3":
            marcar_concluida()
        elif escolha == "4":
            remover_tarefa()
        elif escolha == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

main()
