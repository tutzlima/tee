# Tee no Windows 10/11

## ✅ **1. Instalar o Python mais recente (versão estável)**

*(Python é o programa que vai permitir rodar o aplicativo.)*

### **Passo a passo**

1. Abra o navegador (Chrome, Edge ou Firefox).
2. Acesse o link:
   **[https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)**
3. Na página, procure o botão **Download Python 3.x.x** (é um botão amarelo).
4. Clique nele. O arquivo vai começar a baixar.
5. Quando terminar o download, clique duas vezes no arquivo para abrir.

### **Parte IMPORTANTÍSSIMA**

Na primeira tela da instalação, marque a caixinha:

✔ **Add Python to PATH**
*(Fica no canto inferior da janela.)*

Se não marcar isso, nada vai funcionar depois.

6. Clique em **Install Now**.
7. Espere a instalação terminar (pode levar 1 ou 2 minutos).
8. Clique em **Close**.

---

### **Como testar se deu certo**

1. Aperte **Win + R** no teclado.
2. Digite **cmd** e aperte Enter.
3. No terminal preto que abrir, digite:

```
python --version
```

Se aparecer algo como `Python 3.x.x`, está tudo certo.

Se der erro, significa que o Python não entrou no PATH. Nesse caso, reinstale e veja se marcou a caixinha.

---

## ✅ **2. Instalar o FFmpeg (necessário para áudio/vídeo)**

*(Isso permite que o app transforme, leia ou trate arquivos de áudio e vídeo.)*

### **Baixar e preparar**

1. Baixe aqui:
   **[https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip)**
2. Vá até a pasta onde o arquivo foi salvo (geralmente “Downloads”).
3. Clique com o botão direito no arquivo `.zip` e escolha **Extrair tudo**.
4. Após extrair, vai aparecer uma pasta com um nome grande.
   Renomeie essa pasta para:

```
ffmpeg
```

5. Agora mova essa pasta para o disco C:.

Para isso:

* Abra o Explorer
* Vá em **Este Computador**
* Entre no **Disco Local (C:)**
* Clique e arraste a pasta **ffmpeg** para dentro do C:.

Ao final, o caminho deve ficar assim:

```
C:\ffmpeg
```

---

### **Colocar o FFmpeg no PATH (para funcionar em qualquer lugar)**

1. Aperte **Win + R**.
2. Digite:

```
sysdm.cpl
```

3. Aperte **Enter** → abrirá a janela “Propriedades do Sistema”.
4. Vá na aba **Avançado**.
5. Clique no botão **Variáveis de Ambiente**.
6. Na parte de baixo da janela (Variáveis do Sistema), role até encontrar **Path**.
7. Clique em **Path** → depois **Editar**.
8. Clique em **Novo**.
9. Cole isto:

```
C:\ffmpeg\bin
```

10. Confirme tudo clicando em **OK** nas janelas.

---

### **Testar se o FFmpeg está funcionando**

Abra o **cmd** e digite:

```
ffmpeg -version
```

Se aparecer um monte de texto técnico, está funcionando.
Se der erro, confira se você colocou exatamente:

```
C:\ffmpeg\bin
```

no Path (sem barra extra, sem espaço).

---

## ✅ **3. Baixar o projeto**

Você pode escolher entre duas formas:

---

### **Opção 1 — Baixar o arquivo .zip (mais fácil)**

1. Entre na página do projeto no GitHub.
2. Clique no botão **Code** (verde).
3. Escolha **Download ZIP**.
4. Depois de baixar, clique com o botão direito → **Extrair tudo**.
5. Você terá uma pasta com todos os arquivos do projeto.

---

### **Opção 2 — Clonar o repositório (para quem já criou conta no GitHub)**

1. Crie uma conta em: [https://github.com](https://github.com)
2. Instale o Git (se ainda não tiver).
3. No GitHub, copie o link do repositório.
4. No cmd, digite:

```
git clone LINK_DO_REPOSITÓRIO_AQUI
```

---

#### 🗂 **Importante sobre a pasta do projeto**

Dentro dela deve existir:

* `Home.py`
* `requirements.txt`
* outras pastas e arquivos do projeto

Se o arquivo `requirements.txt` **não** estiver lá, nada da próxima etapa vai funcionar.

---

## ✅ **4. Instalar as dependências (requirements.txt)**

*(São os “componentes” que seu projeto precisa para rodar.)*

### **Abrir o terminal na pasta certa**

1. Abra a pasta do projeto (a que contém o Home.py e o requirements.txt).
2. Clique **na barra de endereço** do Windows (onde aparece algo como `C:\Users\...`).
3. Apague o texto e digite:

```
cmd
```

4. Aperte **Enter**.
   Vai abrir um terminal *já dentro da pasta certa*.

---

### **Atualizar o pip**

No terminal, digite:

```
python -m pip install --upgrade pip
```

Espere terminar.

---

### **Instalar dependências**

Digite:

```
pip install -r requirements.txt
```

Isso pode levar alguns minutos, dependendo dos pacotes.

Se aparecer várias linhas baixando coisas → está funcionando.

---

### **Se der erro aqui**

Geralmente é um destes motivos:

* requirements.txt está na pasta errada
* Python não foi instalado corretamente
* pip não foi atualizado

Se der erro 2 ou 3 vezes, vale sugerir instalar as dependências uma por uma (separadamente).

---

## ❇️ **5. Rodar o aplicativo**

### ⚙️ **Configuração OPCIONAL do Streamlit (`.streamlit/config.toml`)**

Para permitir o envio de arquivos grandes no aplicativo (até **5 GB**, por exemplo), é necessário ajustar o limite de upload padrão do Streamlit.
Essa configuração não fica dentro da pasta do projeto *necessariamente*: ela pode ser feita na pasta global do Streamlit correspondente ao usuário do sistema. Assim, todos seus aplicativos no Streamlit receberão essa configuração.

Crie (ou edite) o arquivo:

#### 📌 **Linux e macOS**

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

#### 📌 **Windows**

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

#### ✔️ Após a configuração

Basta abrir novamente o aplicativo com:

```
streamlit run Home.py
```

O Streamlit passará a aceitar uploads de até 5 GB em qualquer projeto executado no sistema.

---

### **O que acontece agora**

* O navegador deve abrir automaticamente com a interface do app.
* Se não abrir, o terminal mostra um link parecido com:

```
http://localhost:8501
```

Copie e cole no navegador.

Se a porta estiver ocupada, o Streamlit muda para outra (ele avisa no terminal).

---