import streamlit as st

from cards import show_card
from data.fake_testresults import fake_results
from chat_data import get_unread
from gemma import v1_summarize, v2_summarize

st.title("Results of Catching Up on Selected Group Chats")

selected_chats = st.session_state.get("selected_chats", [])
#st.write("You have selected the following group chats to catch up on:")
#st.write(selected_chats) 

if len(selected_chats) == 0:
    st.write("No group chats selected.")

# Version 1: Plain show of summary for each groupchat based on gemma result

# for chat_name in selected_chats:
#     st.subheader(chat_name)

#     cards = fake_results.get(chat_name, [])
#     if len(cards) == 0:
#         st.write("Nothing important found.")

#     for card in cards:
#         show_card(card)

for chat_name in selected_chats:
    st.subheader(chat_name)
    unreadmsges = get_unread(chat_name)

    #key = "v1"+chat_name
    key = "v2_"+chat_name
    if key not in st.session_state:
        with st.spinner("Analyzing messages with Gemma..."):
            #result = v1_summarize(unreadmsges)
            result = v2_summarize(unreadmsges)
            st.session_state[key] = result

    cards, raw, seconds = st.session_state[key]
    st.caption(str(len(unreadmsges)) + " unread messages. Analysis time: " + str(seconds) + " seconds.")

    # with st.container(border=True):
    #     st.markdown(summary)

    if cards is None:
        st.write("Error parsing Gemma output. Raw output:")
        st.code(raw)
    elif len(cards) == 0:
        st.write("Nothing important found.")
    else:
        for card in cards:
            show_card(card)

col1,col2 = st.columns(2)
with col1:
    # rerun analysis with gemma
    if st.button("Rerun analysis with Gemma", key="rerun_analysis_button"):
        # for chat_name in selected_chats:
        #     unreadmsges = get_unread(chat_name)
        #     result = v1_summarize(unreadmsges)
        #     st.session_state["v1"+chat_name] = result
        # st.experimental_rerun()
        for chat_name in selected_chats:
            # if "v1"+chat_name in st.session_state:
            #     del st.session_state["v1"+chat_name]
            if "v2_"+chat_name in st.session_state:
                del st.session_state["v2_"+chat_name]
        st.rerun()

with col2:
    if st.button("Back to Home", key="back_to_home_button"):
        st.switch_page("homescreen.py")