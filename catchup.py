import streamlit as st

st.title("Results of Catching Up on Selected Group Chats")

selected_chats = st.session_state.get("selected_chats", [])
st.write("You have selected the following group chats to catch up on:")
st.write(selected_chats) 
if st.button("Back to Home", key="back_to_home_button"):
    st.switch_page("homescreen.py")