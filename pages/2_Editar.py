import os
import streamlit as st
from streamlit_annotation_tools import text_labeler
from config import extensoes, PASTA_SAIDA
from utils import carregar_audio, reconstruir_conversa

# ===============================
# CONFIGURAÇÃO DA PÁGINA
# ===============================
st.set_page_config(
    page_title="Tee",
    page_icon='assets/hot-tea.png',
    layout="wide"
)

# ===============================
#  CONFIGURAÇÃO INICIAL
# ===============================

os.makedirs(PASTA_SAIDA, exist_ok=True)

st.title("Edite suas transcrições!")

# Lista os TXT disponíveis para edição
arquivos = [f for f in os.listdir(PASTA_SAIDA) if f.endswith(".txt")]

if not arquivos:
    st.info("Nenhuma transcrição disponível ainda.")
    st.stop()

# Duas formas de revisão
revisao_classica, revisao_rotular = st.tabs(["Revisão clássica", "Revisão com rótulos"])

# Sidebar → seleção de arquivo
arquivo_escolhido = st.sidebar.selectbox("Selecione um arquivo", arquivos)
st.sidebar.markdown('---')

nome_base = ".".join(arquivo_escolhido.split(".")[:-1])

caminho_txt = os.path.join(PASTA_SAIDA, arquivo_escolhido)
caminho_audio = os.path.join(PASTA_SAIDA, f"{nome_base}_CONVERTIDO.wav")
caminho_revisado = os.path.join(PASTA_SAIDA, f"{nome_base}_REVISADO.txt")

# Carrega texto original
with open(caminho_txt, "r", encoding="utf-8") as f:
    original = f.read()

# ===============================
#  GESTÃO DE SESSION_STATE
# ===============================

key_original = f"original_{arquivo_escolhido}"
key_editado = f"editado_{arquivo_escolhido}"

# Mantém estado entre renderizações
if key_original not in st.session_state:
    st.session_state[key_original] = original

if key_editado not in st.session_state:
    if os.path.exists(caminho_revisado):
        # Usa versão revisada, se existir
        with open(caminho_revisado, "r", encoding="utf-8") as f:
            st.session_state[key_editado] = f.read()
    else:
        st.session_state[key_editado] = original

# ===============================
#  REVISÃO CLÁSSICA
# ===============================
with revisao_classica:

    if st.sidebar.checkbox('Mostrar transcrição original?', value=False):

        col1, col2 = st.columns(2)

        # Transcrição original
        with col1:
            st.subheader("Transcrição")
            st.text_area(
                "",
                value=st.session_state[key_original],
                height=450,
                key=key_original
            )

        # Versão revisável
        with col2:
            st.subheader("Revisão")
            revisado = st.text_area(
                "",
                value=st.session_state[key_editado],
                height=450,
                key=key_editado
            )

    else:
        # Apenas revisão
        st.subheader("Revisão")
        revisado = st.text_area(
            "",
            value=st.session_state[key_editado],
            height=450,
            key=key_editado
        )

    # Salvar revisão clássica
    st.markdown("---")
    if st.button("Salvar revisão clássica", width="stretch"):
        with open(caminho_revisado, "w", encoding="utf-8") as f:
            f.write(st.session_state[key_editado])

        st.success(f"Arquivo salvo como `{caminho_revisado}`")

# ===============================
#  REVISÃO COM ROTULAÇÃO
# ===============================
with revisao_rotular:

    rotulos = text_labeler(st.session_state[key_original])

    st.markdown("---")
    if st.button("Salvar revisão rotulada", width="stretch"):

        texto_reconstruido = reconstruir_conversa(
            rotulos,
            st.session_state[key_original]
        )

        caminho_saida_rotulos = os.path.join(
            PASTA_SAIDA,
            f"{nome_base}_ROTULADO.txt"
        )

        with open(caminho_saida_rotulos, "w", encoding="utf-8") as f:
            f.write(texto_reconstruido)

        st.success(f"Arquivo salvo como `{caminho_saida_rotulos}`")

        # Mostra texto reconstruído
        with st.expander("Resultado rotulado:"):
            st.text_area("", texto_reconstruido, height=300)

# ===============================
#  PLAYER DE ÁUDIO
# ===============================

if os.path.exists(caminho_audio):
    # Reproduz automaticamente se o WAV existir
    audio_bytes = carregar_audio(caminho_audio)
    st.sidebar.audio(audio_bytes)

else:
    # Permite upload alternativo
    with st.sidebar.expander(' '):
        audio_bruto = st.file_uploader(
            "Selecione o áudio adequado (wav)",
            type=extensoes,
            accept_multiple_files=False
        )

    if audio_bruto is not None:
        audio_bytes = audio_bruto.read()
        st.sidebar.audio(audio_bytes)
    else:
        st.sidebar.warning("Áudio não encontrado. Você pode buscar uma pasta:")
