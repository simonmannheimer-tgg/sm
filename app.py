import streamlit as st

st.set_page_config(
    page_title="TGG Schema Implementation Guide",
    page_icon="🏷",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Remove default Streamlit padding
st.markdown("""
<style>
    .block-container { padding: 0 !important; }
    header { display: none !important; }
    #MainMenu { display: none !important; }
    footer { display: none !important; }
</style>
""", unsafe_allow_html=True)

with open("schema_tool.html", "r", encoding="utf-8") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=920, scrolling=False)
