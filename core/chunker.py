from utils.helpers import save_text


def chunk_text(text, chunk_size=3000, debug_save=True):
    if len(text.split()) <= 1000:
        if debug_save:
            save_text("outputs/3_chunks/output.txt", text)
        return [text]  # teks pendek, tidak perlu chunking

    # chunk per karakter
    chunks = [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]
    delimiter = "\n\n---CHUNK---\n\n"
    if debug_save:
        save_text("outputs/3_chunks/output.txt", delimiter.join(chunks))
    return chunks
