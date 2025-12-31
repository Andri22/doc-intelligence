import pymupdf
from utils.helpers import save_text


def extract_text(file_pdf, debug_save=True):
    """
    file: Streamlit uploaded_file (io.BytesIO)
    return: semua teks PDF
    """
    try:
        # buka dari bytes stream
        pdf = pymupdf.open(stream=file_pdf.read(), filetype="pdf")
    except Exception as e:
        raise ValueError(f"Failed to open PDF: {e}")

    text = ""
    for page in pdf:
        text += page.get_text() + "\n"

    if debug_save:
        save_text("./outputs/1_extracted/output.txt", text)

    return text
