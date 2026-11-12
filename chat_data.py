import json
from datetime import datetime
## functions ----------------------

## read message from the chat json file
def read_chat(filename):
    messages = []

    # read the chat file
    with open("data/" + filename, encoding="utf-8") as f:
        msgline = f.readlines()

    # check each line to extract the msg
    for eachline in msgline:
        line = eachline.strip()

        if " - " in line and ": " in line:
            sender, txt = line.split(": ", 1)
            date_time, rest = sender.split(" - ", 1)
            time = datetime.strptime(date_time, "%d/%m/%y, %H:%M")

            msgdata = {
                "id": len(messages),
                "time": time,
                "sender": sender,
                "text": txt
            }

            # append the msg to the list
            messages.append(msgdata)

    return messages

# Load all chats
def load_chats():
    with open("data/chats.json", encoding="utf-8") as file:
        info = json.load(file)

    me = info["me"]
    chats = []

    # read each chat file and extract messages
    for eachchat in info["chats"]:
        msg = read_chat(eachchat["file"])

        # to show how the ui would realistically look like, we take last message (newest msg)
        # and show it in the chat list area
        last_read = datetime.fromisoformat(eachchat["last_read"])

        unread = []

        for message in msg:
            # get the unreaded msg base on the last_read time in the chats.json
            if message["time"] > last_read and message["sender"] != me:
                unread.append(message)

        eachchat["messages"] = msg
        eachchat["unread"] = unread

        chats.append(eachchat)

    return me, chats
