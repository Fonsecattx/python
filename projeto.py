class tarefa:
    def __init__(self, titulo="", descriçao="", prioridade="baixa", concluida=False, data_vencimento=""):
        self._titulo = titulo
        self._descriçao = descriçao
        self._prioridade = prioridade
        self._concluida = concluida
        self._data_vencimento = data_vencimento

    @property
    def titulo(self):
        return self._titulo
    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo



    def marcar_concluida(self):
        self._concluida = True

    def alterar_prioridade(self, nova_prioridade):
        self._prioridade = nova_prioridade

    def exibir_resumo(self):
        status = "concluída" if self._concluida else "pendente"
        return (
            f"\nTítulo: {self._titulo}"
            f"\nDescrição: {self._descriçao}"
            f"\nPrioridade: {self._prioridade}"
            f"\nStatus: {status}"
            f"\nData de Vencimento: {self._data_vencimento or 'não informado'}"
        )

    def esta_atrasada(self, data_atual):
        if not self._data_vencimento or self._concluida:
            return False
        return data_atual > self._data_vencimento