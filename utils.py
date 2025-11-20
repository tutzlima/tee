import ffmpeg

# ===============================
# CONVERSÃO PARA WAV
# ===============================

def converter_para_wav(input_path, output_path):
    """
    Converte qualquer arquivo de áudio para WAV mono 16 kHz.
    Retorna o caminho convertido se bem-sucedido, ou None se falhar.
    """

    try:
        (
            ffmpeg
            .input(input_path)
            .output(
                output_path,
                ac=1,      # mono
                ar=16000   # 16 kHz
            )
            .overwrite_output()
            .run(capture_stdout=True, capture_stderr=True)
        )
        return output_path

    except ffmpeg.Error as e:
        # Log detalhado útil para debug e transparência
        print("FFmpeg error:", e.stderr.decode("utf-8"))
        return None


# ===============================
# CARREGAR ÁUDIO EM BYTES
# ===============================

def carregar_audio(path):
    """
    Lê áudio e retorna bytes (compatível com st.audio).
    Retorna None caso o arquivo não exista ou não possa ser lido.
    """
    try:
        with open(path, "rb") as f:
            return f.read()
    except FileNotFoundError:
        return None
    except Exception:
        return None


# ===============================
# RECONSTRUIR CONVERSA ROTULADA
# ===============================

def reconstruir_conversa(rotulos, texto_original):
    """
    Recebe rótulos no formato retornado pelo text_labeler e o texto original.
    Retorna um texto final no formato:

        Pessoa: fala 1

        Pessoa: fala 2

    com preservação da ordem com base nos offsets start/end.
    """
    itens = []

    # Achatar os rótulos em uma lista única
    for speaker, spans in rotulos.items():
        for span in spans:
            itens.append({
                "speaker": speaker,
                "start": span["start"],
                "end": span["end"],
                "content": texto_original[span["start"]:span["end"]]
            })

    # Ordenar pelo início do trecho
    itens_ordenados = sorted(itens, key=lambda x: x["start"])

    # Construir texto final
    linhas = []
    for item in itens_ordenados:
        fala = item["content"].strip()
        linhas.append(f"{item['speaker']}: {fala}")

    # Dupla quebra para separar falas visualmente
    return "\n\n".join(linhas)
