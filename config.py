import os

# ===============================
# EXTENSÕES DISPONÍVEIS
# ===============================

extensoes = ["mp3", "wav", "ogg"]

# ===============================
# CONFIGURAÇÃO DE DIRETÓRIOS
# ===============================

DIRETORIO_BASE = os.getcwd()
PASTA_SAIDA = os.path.join(DIRETORIO_BASE, "transcricoes")
