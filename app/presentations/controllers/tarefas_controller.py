from datetime import datetime


class TarefasController:
    def __init__(self, servico_tarefas, view):
        self.servico_tarefas = servico_tarefas
        self.view = view

    def listar_tarefas(self):
        tarefas = self.servico_tarefas.listar_tarefas()
        self.view.mostrar_tarefas(tarefas)

    def criar_tarefa(self, titulo, descricao, prioridade, data_de_criacao):
        nova_tarefa = self.servico_tarefas.criar_tarefa(titulo, descricao, prioridade, data_de_criacao)
        print(f"Tarefa criada: {nova_tarefa.titulo}")
        
    def concluir_tarefa(self, id_tarefa):
        data_de_conclusao = datetime.now() 
        self.servico_tarefas.concluir_tarefa(id_tarefa, data_de_conclusao)
        print(f"Tarefa {id_tarefa} concluída com sucesso!")
        
    def listar_tarefas_por_estado(self, estado):
        tarefas = self.servico_tarefas.listar_tarefas_por_estado(estado)
        self.view.mostrar_tarefas(tarefas)

    def editar_tarefa(self, id_tarefa, titulo=None, descricao=None, prioridade=None):
        self.servico_tarefas.editar_tarefa(id_tarefa, titulo, descricao, prioridade)
        print(f"Tarefa {id_tarefa} editada com sucesso!")
        
    def listar_tarefas_por_prioridade(self, nome_prioridade):
        tarefas = self.servico_tarefas.listar_tarefas_por_prioridade(nome_prioridade)
        self.view.mostrar_tarefas(tarefas)    
        
    def deletar_tarefa(self, id_tarefa):
        self.servico_tarefas.deletar_tarefa(id_tarefa)
        print(f"Tarefa {id_tarefa} deletada com sucesso!")
        
    def atualizar_prioridade(self, id_tarefa, nova_prioridade):
        self.servico_tarefas.atualizar_prioridade(id_tarefa, nova_prioridade)
        print(f"Prioridade da Tarefa {id_tarefa} atualizada para {nova_prioridade.nome}!")
        
    def listar_tarefas_por_categoria(self, nome_categoria):
        tarefas = self.servico_tarefas.listar_tarefas_por_categoria(nome_categoria)
        self.view.mostrar_tarefas(tarefas)