import streamlit as st
from frontend.front_home import apresentacao

# ===============================
# CONFIGURAÇÃO DA PÁGINA
# ===============================
st.set_page_config(
    page_title="Tee",
    page_icon='assets/hot-tea.png',
    layout="wide"
)

# ===============================
# LOGO CENTRALIZADO
# ===============================
# Dividindo a página em 3 colunas para centralizar a imagem
col1, col2, col3 = st.columns(3)

with col2:
    st.image('assets/hot-tea.png', width=200)

# ===============================
# CRÉDITOS DA IMAGEM
# ===============================
# Expander para evitar poluir a interface e ainda manter a referência obrigatória
with st.expander("Créditos da imagem"):
    st.write(
        "Hot tea icons created by Andy Horvath: "
        "https://www.flaticon.com/free-icon/hot-tea_5702410?term=tea&page=1&position=17&origin=style&related_id=5702410"
    )

# ===============================
# APRESENTAÇÃO DO APLICATIVO
# ===============================
st.markdown('---')
st.title("Tee: *transcritor e editor para entrevistas!*")

# Conteúdo importado do módulo frontend.front_home
apresentacao
