import streamlit as st

labels = {
    "asked_you": ":blue[**Asked you**]",
    "agreed":    ":green[**Agreed**]",
    "suggested": ":gray[**Suggested, not agreed**]",
    "task":      ":violet[**Task**]",
    "deadline":  ":orange[**Deadline**]",
}


def show_card(card):
    with st.container(border=True):

        # if the check failed, show a warning label instead
        if card["verified"]:
            st.markdown(labels[card["type"]])
        else:
            st.markdown(":orange[**Couldn't verify**]")

        # AI-written text in italics
        st.markdown("*" + card["text"] + "*")

        # show the old plan if it changed
        if card["changed_from"] != "":
            st.caption("Changed from: " + card["changed_from"])

        # Show messages: expands to show the original messages
        with st.expander("Show messages"):
            for message in card["source"]:
                st.write(message)