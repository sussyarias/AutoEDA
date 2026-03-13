import streamlit as st
import pandas as pd
import os

def read_uploaded_file(file):
    ext = file.name.split(".")[-1].lower()
    if ext == 'csv':
        return pd.read_csv(file)
    else:
        return pd.read_excel(file)

st.set_page_config(
    page_title="Automatic Data Analysis",
    layout= "wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get help": None,
        "Report a bug": None,
        "About" : "An ntelligent app for a rapid exploratory data analysis"
    }
)

def load_css():
    base_dir = os.path.dirname(__file__)
    css_path = os.path.join(base_dir, "styles", "main.css")

    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()
    
def render_header():
    base_dir = os.path.dirname(__file__)
    header_path = os.path.join(base_dir, "components", "header.html")

    with open(header_path) as f:
        st.markdown(f.read(), unsafe_allow_html=True)

render_header()

st.sidebar.markdown("### Upload files")

archivos = st.sidebar.file_uploader(
    "Upload one or many files (CSV or Excel)",
    type=["csv", "xls", "xlsx"],
    accept_multiple_files=True
)

st.sidebar.markdown("---")

with st.sidebar.expander("Visualization options", expanded=False):
    show_index = st.checkbox("Show row index", value=False)
    max_rows = st.slider("Max rows to display", 5, 200, 30, 5)

st.sidebar.markdown("---")
st.sidebar.caption("Advice: if your file is large, try uploading a sample first.")