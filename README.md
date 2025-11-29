<div align="center">
    <a href="https://www.flaticon.com/free-icon/hot-tea_5702410?term=tea&page=1&position=17&origin=style&related_id=5702410">
        <img src="assets/hot-tea.png" width="150px">
    </a>
</div>

# **Tee — Transcritor e Editor de Entrevistas**

## **O que é o app**

O ***Tee*** é uma aplicação desenvolvida para facilitar a transcrição e revisão de entrevistas, especialmente quando você trabalha com arquivos longos, pesados ou quando plataformas online impõem limites de uso.
**Ele realiza transcrição localmente, no seu próprio computador, sem depender de serviços pagos ou restritivos.**

O aplicativo foi pensado para estudantes, pesquisadores, profissionais de humanidades e qualquer pessoa que precise transformar gravações de entrevistas em texto de forma prática e acessível.

*Obs: o app foi desenvolvido pensando em entrevistas, mas serve para transcrição e edição de áudios, no fim das contas. Então, o app é tanto [**Tee 🇩🇪** quanto **Tea 🇺🇸**](https://pbs.twimg.com/media/EAwpkNHXYAA1-gc.jpg)*

---

## **Como funciona**

A interface é construída em [Streamlit](https://streamlit.io/), e o processamento se divide em duas etapas principais, acessíveis pelo menu lateral:

### **1. Transcrever**

* Envie arquivos de áudio (preferencialmente `.wav`, mas outros formatos são aceitos).
* O app converte automaticamente o áudio para WAV mono 16 kHz, garantindo boa compatibilidade com o modelo [**Whisper**](https://github.com/openai/whisper).
* Escolha o modelo de transcrição (`base`, `small`, `medium`, `large`).
  Modelos maiores produzem transcrições melhores, mas demandam mais memória.
* O resultado é salvo como `.txt` na pasta **`transcricoes/`**.

### **2. Editar**

* Abra qualquer transcrição salva.
* Visualize o texto original e revise manualmente.
* Use o modo clássico ou o modo com rótulos, marcando quem está falando.
* O áudio convertido fica disponível para escuta durante a revisão.
* O texto revisado é salvo como um novo arquivo.

---

## **Instalação**

### 🔧 Dependências

Você precisará ter instalado:

* [Python](https://www.python.org/downloads/)
* [FFmpeg](https://www.ffmpeg.org/)
* Repositório clonado localmente

### 🛠 Como rodar o app

1. Crie um ambiente virtual
   `python -m venv venv`

2. Ative o ambiente virtual

   * Windows: `venv\Scripts\activate`
   * Linux/macOS: `source venv/bin/activate`

3. Instale as dependências
   `pip install -r requirements.txt`

   Que incluem:

   ```txt
   torch
   streamlit
   ffmpeg-python
   openai-whisper
   streamlit-annotation-tools
   ```

4. Execute o app
   `streamlit run Home.py`

*Caso queira mais informações, verifique os arquivos `tutorial_windows.md` e/ou `tutorial_windows.pdf`.*

---

#### ⚙️ **Configuração OPCIONAL do Streamlit (`.streamlit/config.toml`)**

Para permitir o envio de arquivos grandes no aplicativo (até **5 GB**, por exemplo), é necessário ajustar o limite de upload padrão do Streamlit.
Essa configuração não fica dentro da pasta do projeto *necessariamente*: ela pode ser feita na pasta global do Streamlit correspondente ao usuário do sistema. Assim, todos seus aplicativos no Streamlit receberão essa configuração.

Crie (ou edite) o arquivo:

##### 📌 **Linux e macOS**

O arquivo fica em:

```
~/.streamlit/config.toml
```

Crie a pasta, caso não exista:

```bash
mkdir -p ~/.streamlit
```

Edite ou crie o arquivo:

```bash
nano ~/.streamlit/config.toml
```

E adicione:

```toml
[server]
maxUploadSize = 5000
```

---

##### 📌 **Windows**

O arquivo fica em:

```
%userprofile%\.streamlit\config.toml
```

Para criar ou editar:

1. Aperte **Win + R**
2. Digite:

   ```
   %userprofile%\.streamlit
   ```
3. Crie (se não existir) o arquivo `config.toml`
4. Insira:

```toml
[server]
maxUploadSize = 5000
```

---

##### ✔️ Após a configuração

Basta abrir novamente o aplicativo com:

```
streamlit run Home.py
```

O Streamlit passará a aceitar uploads de até 5 GB em qualquer projeto executado no sistema.

---

## **Créditos da imagem**

*Ícone:*
[Hot tea icon by Andy Horvath](https://www.flaticon.com/free-icon/hot-tea_5702410?term=tea&page=1&position=17&origin=style&related_id=5702410)

---

## 📄 **Licença**

Este projeto é distribuído sob a licença **GNU Affero General Public License v3.0 (AGPL-3.0)**.

Você pode:

* Usar, copiar e modificar o código.
* Criar trabalhos derivados.
* Compartilhar o projeto com outras pessoas.
* Utilizar o projeto também para fins comerciais.

Contanto que:

* **Dê o devido crédito ao autor**.
* **Mantenha a mesma licença (AGPL-3.0) em quaisquer versões modificadas**.
* **Disponibilize o código-fonte de qualquer aplicação que utilize este projeto, inclusive quando executada por meio de rede** (requisito específico da AGPL).

📘 Licença completa:
[https://www.gnu.org/licenses/agpl-3.0.html](https://www.gnu.org/licenses/agpl-3.0.html)

---

**Copyright (c) 2025 Arthur Lima
([Github](https://github.com/tutzlima) | [Lattes](http://lattes.cnpq.br/2709096118053654))**

---
