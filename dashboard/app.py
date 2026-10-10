"""
Seamedu Air Quality Pune - Streamlit app
Shows the animated dashboard (docs/index.html) as the whole page.
Run with: streamlit run dashboard/app.py
"""

from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Pune Air Quality | Seamedu Awards 2026",
    layout="wide",
    page_icon="🌬️",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        header, footer, [data-testid="stSidebar"], [data-testid="collapsedControl"],
        [data-testid="stToolbar"] { display: none !important; }
        .stApp { background: #12171c; }
        .block-container { padding: 0 !important; max-width: 100% !important; }
        iframe { border: 0; }
    </style>
    """,
    unsafe_allow_html=True,
)

HTML_FILE = Path(__file__).parent.parent / "docs" / "index.html"
components.html(HTML_FILE.read_text(encoding="utf-8"), height=3300, scrolling=True)