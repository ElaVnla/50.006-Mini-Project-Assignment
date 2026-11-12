import streamlit as st

from chat_data import load_chats


st.set_page_config(page_title="Chat App", page_icon=":speech_balloon:", layout="wide")

# static data for the 3 chats
# this example fake chat data is generated from claude to be use to display the chat in the home page interface
chats = [
    {"name": "1D Group 4", "last_sender": "John", "last_text": "gn", "time": "01:25", "unread": 108},
    {"name": "Dance exco", "last_sender": "Ryan", "last_text": "gn", "time": "00:40", "unread": 88},
    {"name": "Family", "last_sender": "Dad", "last_text": "gn", "time": "23:45", "unread": 50},
    {"name": "Mum", "last_sender": "Mum", "last_text": "ok see you", "time": "Yesterday", "unread": 0}
]

st.title("Your designated messaging app")

for chat in chats:

    with st.container(border=True):

        col1, col2 = st.columns([5, 1])

        with col1:
            st.write("**" + chat["name"] + "**")
            st.write(chat["last_sender"] + ": " + chat["last_text"])

        with col2:
            st.write(chat["time"])

            if chat["unread"] > 0:
                st.write(":green-background[" + str(chat["unread"]) + "]")