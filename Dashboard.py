import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""
def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to Streamlit! 👋")

    st.sidebar.success("Select a demo above.")
    custom_css()
    st.markdown(
        """

    """
    )

def custom_css():
    css = """
    <style>
    .sidebar .sidebar-content {
        background-color: #9c77b9;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Inject the custom CSS



if __name__ == "__main__":
    run()