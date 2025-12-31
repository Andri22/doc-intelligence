import os


def save_text(path: str, text: str):
    """Simpan teks string ke file, buat folder otomatis"""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf8") as f:
        f.write(text)


# def save_bytes(path: str, data: bytes):
#     """Simpan bytes ke file, buat folder otomatis"""
#     os.makedirs(os.path.dirname(path), exist_ok=True)
#     with open(path, "wb") as f:
#         f.write(data)


def load_text(path: str) -> str:
    """
    Baca teks dari file dan kembalikan sebagai string.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File {path} tidak ditemukan")

    with open(path, "r", encoding="utf8") as f:
        return f.read()


def call_llm(client, text):
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": text}],
        model="llama-3.3-70b-versatile",
    )
    return chat_completion.choices[0].message.content


# from utils.groq_client import call_groq_llm
# from utils.helpers import call_llm, save_text


def safe_call_llm(client, prompt, retries=3):
    """
    Memanggil LLM dengan error handling.
    Jika gagal, retry beberapa kali.
    """
    for attempt in range(retries):
        try:
            response = call_llm(client, prompt)
            return response
        except Exception as e:
            print(f"[Attempt {attempt + 1}] LLM API failed: {e}")
    # fallback jika semua retry gagal
    return "Error: Unable to get response from LLM."


def count_tokens(text: str) -> int:
    """
    Hitung token kasar (1 kata ≈ 1 token)
    """
    return len(text.split())
