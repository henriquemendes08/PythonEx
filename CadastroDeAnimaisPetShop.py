# Exercício proposto: Cadastro de Animais em um Pet Shop Menu:
# Adicionar animal
# Listar animais
# Atualizar status de banho (sim/não)
# Remover animal
# Sair
# Cada animal cadastrado deve ter: nome espécie (ex: cachorro, gato, etc.) já tomou banho? (sim ou não)
animais = []
def menu():
    print('Bem-vindo ao Petshop')
    print('')
    print('1- Adicionar animal')
    print('2 - Listar animais')
    print('3 - Status de banho')
    print('4 - Remover animal')
    print('5 - Sair')

def adicionar_animal():
    nome = input('Nome Do animal:')
    especie = input("Especie:")
    banho = input("Já tomou banho: (S/N)")

    if banho.lower().startswith("s"):
        tomou_banho = "sim"
    elif banho.lower().startswith("n"):
        tomou_banho = "não"
    else:
        print('Opção inválida. Animal não cadastrado.')
        return
    
    animal = {
        "nome": nome,
        "especie": especie,
        "banho": tomou_banho 
    }

    animais.append(animal)
    print('Animal cadastrado com sucesso!') 
    
def listar_animais():
    if not animais:
         print('Animal não foi encontrado no sistema')
         return

    nome_animal = input('Qual o nome do animal:')
    encontrado = False
    for animal in animais:
        if nome_animal.lower() == animal["nome"].lower():
            encontrado == True
            print(f'As informaçoes do animal {animal["nome"]}:')
            print(f'A especie:{animal["especie"]}')
            print(f'  Banho: {animal["banho"]}')
            break
           

def status_banho(): 
    nome_animal = input('Digite o nome do animal: ')
    encontrado = False
    for animal in animais:
        if nome_animal.lower() == animal["nome"].lower():
            encontrado = True
            print(f'Banho atual: {animal["banho"]}')
            alterar = input('Deseja trocar o status de banho? (S/N): ')
            if alterar.lower().startswith('s'):
                novo_status = input('Novo status de banho (S/N): ')
                if novo_status.lower().startswith('s'):
                    animal["banho"] = "sim"
                elif novo_status.lower().startswith('n'):
                    animal["banho"] = "não"
                else:
                    print('Entrada inválida. Status não alterado.')
                    return
                print('Informações atualizadas.')
            break


def remover_animal():
    encontrar_animal = input('Qual o nome do animal:')
    encontrado = False
    for animal in animais:
        if encontrar_animal.lower() == animal["nome"].lower():
            encontrado = True
            animais.remove(animal)
            print(f'Animal "{animal["nome"]}" removido com sucesso.')
            break
        else:
            print("Animal não encontrado.")



def main():
    while True:
        menu()
        opcao = input('Escolha uma opção')
        if opcao == "1":
            adicionar_animal()
        elif opcao == "2":
            listar_animais()
        elif opcao == "3":
            status_banho() 
        elif opcao == "4":
            remover_animal()
        elif opcao == "5":
            print("Saindo do progama")
            break

main()

