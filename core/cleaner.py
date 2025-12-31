import re
from utils.helpers import save_text


def clean_text(text, keep_paragraphs=True, debug_save=True):
    if keep_paragraphs:
        # ganti page break \f dengan newline
        text = text.replace("\f", "\n")
        # hapus spasi berlebih tapi tetap jaga newline
        text = re.sub(r"[ \t]+", " ", text)  # normalize spasi/tab
        text = re.sub(r"\n+", "\n", text)  # normalize multiple newline jadi satu
    else:
        text = text.replace("\f", " ")  # replace page break
        text = re.sub(r"\s+", " ", text)  # normalize whitespace

    text = text.strip()

    if debug_save:
        save_text("./outputs/2_cleaned/output.txt", text)
    return text
