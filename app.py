import streamlit as st

st.set_page_config(
    page_title="TGG Schema Implementation Guide",
    page_icon=":label:",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    .block-container { padding: 0 !important; max-width: 100% !important; }
    header[data-testid="stHeader"] { display: none !important; }
    #MainMenu, footer { display: none !important; }
    iframe { border: none !important; }
    .stApp { background: #080d17 !important; }
</style>
""", unsafe_allow_html=True)

with open("schema_tool.html", "r", encoding="utf-8") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=900, scrolling=True)
