
class Tarefa:
    def __init__(self, id, titulo, descricao, concluida, prioridade, data_de_criacao, data_de_conclusao=None, categoria=None):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = concluida
        self.prioridade = prioridade
        self.data_de_criacao = data_de_criacao
        self.data_de_conclusao = data_de_conclusao
        self.categoria = categoria
    
    def concluir(self, data_de_conclusao):
        self.concluida = True
        self.data_de_conclusao = data_de_conclusao