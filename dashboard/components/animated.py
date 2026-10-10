"""Animated HTML dashboard tab."""

from pathlib import Path
import streamlit.components.v1 as components

HTML_FILE = Path(__file__).parent.parent.parent / "docs" / "index.html"


def render():
    html = HTML_FILE.read_text(encoding="utf-8")
    components.html(html, height=2600, scrolling=True)