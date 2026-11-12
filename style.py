import streamlit as st


def add_style():
    st.markdown("""
    <style>
    .st-key-catchup_button {
        position: fixed;
        bottom: 40px;
        right: 40px;
        z-index: 999;
        width: auto;
    }
    .st-key-catchup_button button {
        border-radius: 30px;
        background-color: #1D9E75;
        color: white;
        border: none;
        padding: 10px 20px;
    }
    </style>
    """, unsafe_allow_html=True)