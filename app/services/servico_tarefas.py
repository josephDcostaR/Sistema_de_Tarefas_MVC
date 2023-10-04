
from app.domain.entities.tarefa import Tarefa

class ServicoTarefas:
    def __init__(self, repositorio_tarefas):
        self.repositorio_tarefas = repositorio_tarefas

    def criar_tarefa(self, titulo, descricao, prioridade, data_de_criacao, categoria=None):
        nova_tarefa = Tarefa(len(self.repositorio_tarefas.listar_tarefas()) + 1, titulo, descricao, False, prioridade, data_de_criacao, categoria=categoria)
        self.repositorio_tarefas.adicionar_tarefa(nova_tarefa)
        return nova_tarefa

    def listar_tarefas(self):
        return self.repositorio_tarefas.listar_tarefas()
    
    def concluir_tarefa(self, id_tarefa):
        tarefa = self.repositorio_tarefas.obter_tarefa(id_tarefa)
        if tarefa:
            tarefa.concluida = True
            
    def listar_tarefas_por_estado(self, estado):
        return [tarefa for tarefa in self.repositorio_tarefas.listar_tarefas() if tarefa.concluida == estado]

    def editar_tarefa(self, id_tarefa, titulo=None, descricao=None, prioridade=None):
        tarefa = self.repositorio_tarefas.obter_tarefa(id_tarefa)
        if tarefa:
            if titulo:
                tarefa.titulo = titulo
            if descricao:
                tarefa.descricao = descricao
            if prioridade:
                tarefa.prioridade = prioridade
                
    def listar_tarefas_por_prioridade(self, nome_prioridade):
        return [tarefa for tarefa in self.repositorio_tarefas.listar_tarefas() if tarefa.prioridade == nome_prioridade]


    def concluir_tarefa(self, id_tarefa, data_de_conclusao):
        tarefa = self.repositorio_tarefas.obter_tarefa(id_tarefa)
        if tarefa:
            tarefa.concluir(data_de_conclusao)
            
    def deletar_tarefa(self, id_tarefa):
        self.repositorio_tarefas.deletar_tarefa(id_tarefa)
            
    def atualizar_prioridade(self, id_tarefa, nova_prioridade):
        tarefa = self.repositorio_tarefas.obter_tarefa(id_tarefa)
        if tarefa:
            tarefa.prioridade = nova_prioridade  