import os
import torch
import ffmpeg
import whisper
import streamlit as st
from config import extensoes, PASTA_SAIDA
from utils import converter_para_wav

# ===============================
# CONFIGURAÇÃO DA PÁGINA
# ===============================
st.set_page_config(
    page_title="Tee",
    page_icon='assets/hot-tea.png',
    layout="wide"
)

# ===============================
# CONFIGURAÇÃO DE DIRETÓRIOS
# ===============================

os.makedirs(PASTA_SAIDA, exist_ok=True)

# ===============================
# TÍTULO
# ===============================
st.title("Transcreva suas entrevistas!")
st.markdown("---")

# ===============================
# UPLOAD DE ARQUIVOS
# ===============================

entrevistas = st.file_uploader(
    "Selecione os áudios",
    type=extensoes,
    accept_multiple_files=True,
    help="Recomendo transcrever uma por vez!"
)

tamanho_do_modelo = st.selectbox(
    "Modelo Whisper",
    ["base", "small", "medium", "large"],
    help="Leve em consideração a memória do seu computador!"
)

# ===============================
# BOTÃO DE TRANSCRIÇÃO
# ===============================

if st.button("Transcrever", type="primary", use_container_width=True):

    if not entrevistas:
        st.error("Nenhum arquivo selecionado.")
        st.stop()

    exp = st.expander("Ver detalhes da transcrição")

    exp.info("Carregando modelo…")
    model = whisper.load_model(tamanho_do_modelo)

    # ===============================
    # LOOP SOBRE OS ARQUIVOS
    # ===============================

    for arquivo in entrevistas:

        nome_base = ".".join(arquivo.name.split(".")[:-1])

        # caminhos de saída
        txt_path = os.path.join(PASTA_SAIDA, f"{nome_base}.txt")
        wav_path = os.path.join(PASTA_SAIDA, f"{nome_base}_CONVERTIDO.wav")

        # salvar arquivo temporário
        temp_path = os.path.join(PASTA_SAIDA, arquivo.name)
        with open(temp_path, "wb") as f:
            f.write(arquivo.read())

        exp.info(f"Convertendo para WAV: **\"{arquivo.name}\"**…")

        # evitar conflito com WAV antigo
        if os.path.exists(wav_path):
            os.remove(wav_path)

        # converter para WAV
        convertido = converter_para_wav(temp_path, wav_path)
        if convertido is None:
            exp.error("Erro ao converter para WAV!")
            st.stop()

        os.remove(temp_path)  # excluir original carregado

        exp.info(f"Transcrevendo: **\"{nome_base}.wav\"**…")

        # Detecta automaticamente se o modelo pode usar fp16
        if torch.cuda.is_available():
            major, minor = torch.cuda.get_device_capability(0)
            suporta_fp16 = major >= 7  # Turing (7.0) ou mais recente
        else:
            suporta_fp16 = False
            #st.write(f"FP16 ativo: {suporta_fp16}")

        resultado = model.transcribe(
            convertido,
            language="pt",
            fp16=suporta_fp16
        )

        # salvar transcrição
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(resultado["text"])

        exp.markdown("---")
        exp.success(f"Transcrição salva: `{txt_path}`")
        exp.success(f"Áudio (WAV) salvo: `{wav_path}`")
