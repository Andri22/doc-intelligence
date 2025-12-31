from core.ingest import extract_text
from core.cleaner import clean_text
from core.chunker import chunk_text
from core.summarizer import summary_text
from core.analyzer import analyze_sentiment_topics
import streamlit as st

st.set_page_config(page_title="ABC", layout="wide")
st.title("🤖 AI Content Analyzer & Summarizer")
st.caption("Analyze, summarize, and understand content instantly with AI.")

for key, default in {
    "chunks": None,
    "summary": None,
    "analysis": None,
    "summary_done": False,
    "last_file": None,
}.items():
    st.session_state.setdefault(key, default)


def reset_state(current_file=None):
    st.session_state.update(
        {
            "chunks": None,
            "summary": None,
            "analysis": None,
            "summary_done": False,
            "last_file": current_file,
        }
    )


# ======================
# Sidebar
# ======================
with st.sidebar:
    st.header("📂 Upload Document")
    uploaded_file = st.file_uploader("Pilih file PDF", type=["pdf"], key="uploader")

st.write("KEY SESSION:")
st.write(list(st.session_state.keys()))


current_file = uploaded_file.name if uploaded_file else None
if current_file != st.session_state["last_file"]:
    reset_state(current_file)


# ======================
# Summary option
# ======================
summary_type = st.selectbox(
    "Pilih tipe ringkasan:", ["bullet", "detailed", "executive"], key="mode"
)

if uploaded_file:
    st.info(f"📄 File uploaded: {uploaded_file.name}")

    # Preprocess hanya sekali
    if st.session_state.get("chunks") is None:
        with st.spinner("Membaca & membersihkan dokumen..."):
            raw = extract_text(uploaded_file)
            clean = clean_text(raw)
            st.session_state["chunks"] = chunk_text(clean)

    # Tombol summary (muncul setelah upload)
    if st.button("📝 Process Summary"):
        with st.spinner("Membuat summary..."):
            st.session_state["summary"] = summary_text(
                summary_type, st.session_state["chunks"]
            )
            st.session_state["summary_done"] = True

else:
    st.warning("Silakan upload PDF terlebih dahulu.")


# ======================
# Summary Output (TIDAK DI-NIMPA)
# ======================
if st.session_state["summary"]:
    st.subheader("📌 Summary")
    st.text_area(label="Summary Result", value=st.session_state["summary"], height=300)

# ======================
# Sentiment Button (muncul SETELAH summary)
# ======================
if st.session_state["summary_done"]:
    if st.button("📊 Analyze Sentiment"):
        with st.spinner("Menganalisis sentiment & topik..."):
            st.session_state["analysis"] = analyze_sentiment_topics(
                st.session_state["chunks"]
            )

# ======================
# Sentiment Output (AREA TERPISAH)
# ======================
# if st.session_state["analysis"]:
#     st.subheader("📈 Sentiment & Topic Analysis")
#     st.text_area(
#         label="Sentiment Analysis Result",
#         value=st.session_state["analysis"],
#         height=250,
#     )
if st.session_state["analysis"]:
    analysis = st.session_state["analysis"]

    st.subheader("📈 Sentiment Analysis")

    for i, item in enumerate(analysis, 1):
        st.markdown(f"### Section {i}")
        st.markdown(f"**Sentiment:** {item['sentiment']}")

        st.markdown("**Topics:**")
        for t in item["topics"]:
            st.markdown(f"- {t}")
