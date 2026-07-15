from tarefas import *

while True:

    print("\nTASKFLOW")

    print("1-Criar")
    print("2-Listar")
    print("3-Editar")
    print("4-Excluir")
    print("5-Sair")

    op = input("Escolha: ")

    if op == "1":
        criar(input("Título: "))

    elif op == "2":
        print(listar())

    elif op == "3":
        editar(int(input("Índice: ")), input("Novo: "))

    elif op == "4":
        excluir(int(input("Índice: ")))

    elif op == "5":
        break