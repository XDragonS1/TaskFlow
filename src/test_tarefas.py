from tarefas import *

def test_criar():
    tarefas.clear()
    criar("Python")
    assert listar() == ["Python"]

def test_editar():
    tarefas.clear()
    criar("Git")
    editar(0, "GitHub")
    assert listar()[0] == "GitHub"

def test_excluir():
    tarefas.clear()
    criar("Teste")
    excluir(0)
    assert listar() == []