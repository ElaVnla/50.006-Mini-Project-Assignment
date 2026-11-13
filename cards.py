import streamlit as st

labels = {
    "asked_you": ":blue[**Asked you**]",
    "agreed":    ":green[**Agreed**]",
    "suggested": ":gray[**Suggested, not agreed**]",
    "task":      ":violet[**Task**]",
    "deadline":  ":orange[**Deadline**]",
}


def show_card(card):

    # cardtype = card.get("type", "")
    # text = card.get("text", "")
    # changed_from = card.get("changed_from", "")
    # source = card.get("source", [])
    # verified = card.get("verified", True)

    cardtype = card.get("type", "")
    cardtype = cardtype.lower().replace(" ", "_")
    text = card.get("text", "")
    changed_from = card.get("changed_from", "")
    source = card.get("source", [])
    verified = card.get("verified", True) 


    with st.container(border=True):

        # if the check failed, show a warning label instead
        if verified:
            st.markdown(labels.get(cardtype, "**" + cardtype + "**"))
        else:
            st.markdown(":orange[**Couldn't verify**]")

        # AI-written text in italics
        st.markdown("*" + text + "*")

        # show the old plan if it changed
        if changed_from != "":
            st.caption("Changed from: " + changed_from)

        # Show messages: expands to show the original messages
        with st.expander("Show messages"):
            for message in source:
                st.write(message)