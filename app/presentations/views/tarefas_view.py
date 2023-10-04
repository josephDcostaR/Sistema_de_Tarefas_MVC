
class TarefasView:
    def mostrar_tarefas(self, tarefas):
        print("Tarefas:")
        for tarefa in tarefas:
            print(f"{tarefa.titulo} - {'Concluída' if tarefa.concluida else 'Pendente'} - Prioridade: {tarefa.prioridade} - Criada em: {tarefa.data_de_criacao}")