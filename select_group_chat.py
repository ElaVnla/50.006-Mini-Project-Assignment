import streamlit as st


st.title("Select Group Chats to catch up on")
#st.write("multi select option here")

# select group chats to catch up on
selected_chats = st.multiselect("Select group chats to catch up on", ["1D Group 4", "Dance exco", "Family"])

# make button layout ncie nice

col1, col2, col3 = st.columns([1,1,2])

with col1:
    if st.button("back", key="back_button"):
        st.switch_page("homescreen.py")

with col3:
    vers = st.radio(
        "debugging purposes",
        ["V1: plain", "V2: JSON cards", "V3: + prompt rules"],
        key="version_picker",
    )

with col2:
    if st.button("catch up", key="catchup_button"):
        if len(selected_chats) == 0:
            st.warning("Please select at least one group chat to catch up on.")
        else:
            #st.write("catching up on selected group chats: " + ", ".join(selected_chats))
            st.session_state["selected_chats"] = selected_chats
            st.session_state["version"] = vers 
            st.switch_page("catchup.py")

    