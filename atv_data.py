# Gabriel Vieira, Juliana Moreira, Massuello Quaresma
import time

while True:
    print("=======================")
    print("1. Criar Turma")
    print("2. Adicionar Professor")
    print("3. Adicionar Estudante")
    print("4. Adicionar Nota")
    print("5. Consultar Nota")
    print("6. Salvar Nota ")
    print("7. Sair")

    opcao = int(input("Escolha uma opção: "))
    match opcao:
        case 1:
            print("Você selecionou: Criar uma turma \n")
            time.sleep(2)
        case 2:
            print("Você selecionou: Criar professor \n")
            time.sleep(2)
        case 3:
            print("Você selecionou: Adicionar um estudante \n")
            time.sleep(2)
        case 4:
            print("Você selecionou: Adicionar uma nota \n")
            time.sleep(2)
        case 5:
            print("Você selecionou: Consultar uma nota \n")
            time.sleep(2)
        case 6:
            print("Você selecionou: Salvar nota \n")
            time.sleep(2)
        case 7: 
            print("Saindo...")
            time.sleep(2)
            break
        case _:
            print("Você não digitou uma opção válida! \n")
