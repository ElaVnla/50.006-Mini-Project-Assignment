import streamlit as st

from cards import show_card
from data.fake_testresults import fake_results

st.title("Results of Catching Up on Selected Group Chats")

selected_chats = st.session_state.get("selected_chats", [])
#st.write("You have selected the following group chats to catch up on:")
#st.write(selected_chats) 

if len(selected_chats) == 0:
    st.write("No group chats selected.")

for chat_name in selected_chats:
    st.subheader(chat_name)

    cards = fake_results.get(chat_name, [])
    if len(cards) == 0:
        st.write("Nothing important found.")

    for card in cards:
        show_card(card)

if st.button("Back to Home", key="back_to_home_button"):
    st.switch_page("homescreen.py")