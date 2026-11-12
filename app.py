import streamlit as st

from chat_data import load_chats


st.set_page_config(page_title="Chat App", page_icon=":speech_balloon:", layout="wide")

# load pages
homescreenpage = st.Page("homescreen.py", title="Home", icon=":material/home:")
Selectgroupchatpage = st.Page("select_group_chat.py", title="Select Group Chat", icon=":material/auto_awesome:")

page = st.navigation([homescreenpage, Selectgroupchatpage], position="hidden")
page.run()
