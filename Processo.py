class Processo:
    tempo_chegada = 0
    prioridade = 0
    tempo_execucao = 0
    tamanho = 0
    impressora = 0
    scanner = 0
    modem = 0
    cd = 0
    tInicio = 0
    tFim = 0
    tTotalProcesso = 0
    tTotalSuspenso = 0
    estado = 0
    id = 0

    def __init__(self, tempo_chegada, prioridade, tempo_execucao, tamanho, impressora, scanner, modem, cd, tInicio, tFim, tTotalProcesso, tTotalSuspenso, estado, id):
        self.tempo_chegada = tempo_chegada
        self.prioridade = prioridade
        self.tempo_execucao = tempo_execucao
        self.tamanho = tamanho
        self.impressora = impressora
        self.scanner = scanner
        self.modem = modem
        self.cd = cd
        self.tInicio = tInicio
        self.tFim = tFim
        self.tTotalProcesso = tTotalProcesso
        self.tTotalSuspenso = tTotalSuspenso
        self.estado = estado
        self.id = id

