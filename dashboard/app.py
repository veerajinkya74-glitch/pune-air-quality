"""
Seamedu Air Quality Pune — Streamlit Dashboard
================================================
Slim entry point. All tab logic lives in dashboard/components/.
Run with: streamlit run dashboard/app.py
"""

import sys
from pathlib import Path
import warnings

# Ensure project root is on the path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

import streamlit as st
from src.data_loader import load_daily_aqi, load_hourly_pollutants
from dashboard.components import (
    animated,
    aqi_trend,
    seasonal,
    correlations,
    year_over_year,
    hourly_analysis,
    forecast,
    sidebar,
)

warnings.filterwarnings("ignore")

# ====================== PAGE CONFIG ======================
st.set_page_config(
    page_title="Pune Air Quality | Seamedu Awards 2026",
    layout="wide",
    page_icon="🌬️",
)

st.markdown(
    """
    <style>
        :root {
            --bg: #071b2d;
            --panel: #0d243d;
            --panel-soft: #12304d;
            --primary: #42d392;
            --primary-strong: #1ecf8a;
            --secondary: #8ec5ff;
            --text: #eaf6ff;
            --muted: #b7d2ea;
            --border: rgba(142, 197, 255, 0.18);
            --shadow: rgba(0, 0, 0, 0.22);
        }

        .stApp {
            background: linear-gradient(135deg, #071b2d 0%, #0b1f38 35%, #12324d 100%);
            color: var(--text);
        }

        .stApp > div {
            background: transparent;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 1500px;
        }

        h1, h2, h3, h4, h5, h6 {
            color: var(--text) !important;
            letter-spacing: 0.02em;
        }

        .stTitle {
            color: var(--text) !important;
            font-size: 2.5rem !important;
            font-weight: 800 !important;
            margin-bottom: 0.2rem !important;
        }

        .stMarkdown {
            color: var(--muted);
        }

        .stCaption {
            color: var(--secondary) !important;
            font-size: 0.95rem !important;
        }

        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, rgba(11,31,56,0.98) 0%, rgba(15,35,58,0.98) 100%);
            border-right: 1px solid var(--border);
        }

        [data-testid="stSidebar"] .stMarkdown,
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] div {
            color: var(--text) !important;
        }

        [data-testid="stSidebar"] section {
            background: rgba(255,255,255,0.01);
            border-radius: 14px;
        }

        .stTabs [role="tablist"] {
            background: rgba(15,35,58,0.75);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 0.35rem;
            gap: 0.35rem;
        }

        .stTabs [role="tab"] {
            color: var(--muted) !important;
            border-radius: 10px;
            padding: 0.7rem 1rem;
            font-weight: 600;
        }

        .stTabs [role="tab"][aria-selected="true"] {
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-strong) 100%);
            color: #062334 !important;
            box-shadow: 0 8px 20px rgba(30, 207, 138, 0.22);
        }

        div[data-testid="stVerticalBlock"] > div {
            background: rgba(18,48,77,0.75);
            border: 1px solid var(--border);
            border-radius: 16px;
            box-shadow: 0 8px 24px var(--shadow);
        }

        .stDataFrame, .stPlotlyChart, .stAltairChart, .stVegaLiteChart {
            border-radius: 16px;
            overflow: hidden;
            border: 1px solid var(--border);
        }

        .css-1d391kg, .css-1n8t7l5 {
            background: transparent;
        }

        button, .stDownloadButton > button, .stButton > button {
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-strong) 100%);
            color: #062334;
            border: none;
            border-radius: 10px;
            font-weight: 700;
            box-shadow: 0 8px 18px rgba(30, 207, 138, 0.18);
        }

        .stButton > button:hover {
            filter: brightness(1.05);
            box-shadow: 0 10px 22px rgba(30, 207, 138, 0.28);
        }

        .stMetric {
            background: rgba(255,255,255,0.02);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 0.8rem 1rem;
        }

        .stMetric > div {
            color: var(--text) !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🌬️ Pune Air Quality Analysis (2017–2024) + 2025–2026 Forecast")
st.markdown("**Data Analytics Excellence Award** – Seamedu Awards 2026")
st.caption("Live Interactive Dashboard | Built with Python, Plotly & Streamlit")

# ====================== LOAD DATA ======================
@st.cache_data
def load_data():
    daily = load_daily_aqi()
    hourly = load_hourly_pollutants()
    return daily, hourly

daily, hourly = load_data()

# ====================== TABS ======================
tab0, tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Animated Dashboard",
    "📈 AQI Trend",
    "📊 Seasonal Analysis",
    "🔥 Pollutant Correlations",
    "📅 Year-over-Year",
    "⏰ Hourly PM2.5 vs PM10",
    "🔮 2025–2026 Forecast",
])

with tab0:
    animated.render()

with tab1:
    aqi_trend.render(daily)

with tab2:
    seasonal.render(daily)

with tab3:
    correlations.render(hourly)

with tab4:
    year_over_year.render(daily)

with tab5:
    hourly_analysis.render(hourly)

with tab6:
    forecast.render(daily)

# ====================== SIDEBAR ======================
sidebar.render()

st.caption("Dashboard ready")
