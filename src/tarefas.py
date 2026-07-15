tarefas = []

def criar(titulo):
    tarefas.append(titulo)

def listar():
    return tarefas

def editar(indice, titulo):
    tarefas[indice] = titulo