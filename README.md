# Catch Up

Catch Up helps you catch up on busy group chats without scrolling through hundreds of unread messages. Tap the floating **✨ Catch up** button on the chat list, pick one or more group chats, and a local **Gemma 4** model (via Ollama) turns the unread messages into short cards:

- **Asked you** – someone asked Ella (the user) to do something
- **Agreed** – the group clearly agreed on a plan
- **Suggested, not agreed** – someone proposed something, but the group did not agree
- **Task** – someone other than Ella agreed to do something
- **Deadline** – a due date or time limit

Each card shows what it changed from (if the plan changed) and a **Show messages** button so you can check the original messages before acting. Everything runs locally: no cloud APIs are used.

The chats in `data/` are made-up WhatsApp-style chats for a student named Ella (a 1D project group, a dance CCA exco and her family).

## How to run

1. **Install Ollama** from https://ollama.com and make sure it is running.

2. **Download the models**
   ```
   ollama pull gemma4:e4b
   ollama pull gemma4:e2b
   ```
   `gemma4:e4b` is the main model. `gemma4:e2b` is only used by version V4.

3. **Set up Python** (Python 3.10+), from the project folder:
   ```
   python -m venv venv
   ```
   Activate it:
   - Windows: `venv\Scripts\activate`
   - macOS / Linux: `source venv/bin/activate`

   Then install the packages:
   ```
   pip install streamlit ollama
   ```

4. **Start the app**
   ```
   streamlit run app.py
   ```
   The app opens at http://localhost:8501.

5. **Use it**
   - Tap **Catch up** on the chat list.
   - Select one or more group chats.
   - Choose a version under "For testing purposes" (V3 is the final version).
   - Tap **Catch up** and wait. Each chat takes about 1–3 minutes on a laptop.
   - Tap **Show messages** on a card to see where it came from, or **Rerun analysis with Gemma** to run it again.

The raw Gemma output and the time taken for each chat are printed in the terminal.

### Versions

| Version | What it does |
|---|---|
| V1: plain | Plain prompt, free-text summary |
| V2: JSON cards | JSON cards at temperature 0 |
| V3: + prompt rules | V2 + stricter prompt rules (final version) |
| V4: smaller model (e2b) | V3 prompt on `gemma4:e2b`, to test speed |

### Troubleshooting

- **Connection error to Ollama:** check `ollama list` works. If you are behind a system proxy, `gemma.py` already uses `trust_env=False` to connect to `127.0.0.1:11434` directly.
- **Old results showing:** results are cached per version and chat. Use **Rerun analysis with Gemma** to clear them.

## For testing verification

Below are the decisions, tasks, requests and deadlines in each chat's **unread** messages (based on the `last_read` times in `data/chats.json`). Use this checklist to see whether the model detects each item, labels it with the right type, and avoids the items under "Should NOT appear".

### 1D Group 4 (unread after 18:00)

**Should appear**
1. **Deadline:** Report and video due Sunday 11:59pm
2. **Agreed:** Meeting Friday 4pm on Zoom (changed from Thu 2pm in school → Fri 3pm Zoom)
3. **Task:** Priya does slides 1–4 and 12
4. **Task:** Jia Hui does slides 6–11
5. **Task:** John does slide 15 (changed from slide 12)
6. **Task:** Marcus does slides 13–14 and the intro video
7. **Asked you:** Priya asked Ella to do the user flow diagram
8. **Asked you:** Marcus asked Ella to update slide 5 with the new user flow before Friday
9. **Asked you:** The group wants Ella to do the persona slides ("the one who did the interviews la, she can do it") — an indirect reference, used as a deliberate failure test
10. **Suggested:** Survey with 10 people (not agreed)
11. **Suggested:** Book a room on Saturday to record the video (nobody agreed)

**Nice to have:** Priya did the intro part; report outline is in the drive.

**Should NOT appear**
- Marcus booking a room for Thursday (cancelled: "no need room")
- "ella's interviews were damn good" as its own card (a compliment, not a request)
- Small talk: food, aircon, lecture slides, football, cat

### Dance exco (unread after 20:00)

**Should appear**
1. **Agreed:** Practice Wednesday 7pm, same hall (changed from Tuesday 7pm)
2. **Agreed / Deadline:** Performance on 28 Nov at the auditorium
3. **Agreed:** Costume budget $150 (changed from $200)
4. **Task:** Ryan collects the costumes on Saturday at the Jurong shop (changed from Ella)
5. **Task:** Wei Ling fixes the music cut at 2:10
6. **Asked you:** Aisyah asked Ella to confirm the auditorium booking by Friday (needs her email, urgent)
7. **Suggested:** New formation for the chorus ("maybe, we see on tues")

**Should NOT appear**
- Ella collecting the costumes (cancelled: "ella dont need")
- $200 budget or Tuesday practice as separate cards
- Small talk: K-pop MV, photo, sore legs, prata, shoes, music file share

### Family (unread after 21:00)

**Should appear**
1. **Agreed:** Sunday 12pm lunch at Ah Ma's house (changed from Saturday 7pm dinner)
2. **Task:** Dad buys the fruits
3. **Asked you:** Jayden (backed by Mum) asked Ella to help with his math homework tomorrow night
4. **Asked you:** Dad asked Ella to buy wholemeal bread on the way home tomorrow
5. **Optional:** Bring an umbrella tomorrow (a reminder for everyone, not only Ella)

**Should NOT appear**
- Milo (Dad said "no milo")
- Saturday dinner as a separate card
- Getting a dog (both parents said no)
- Small talk: lost umbrella, dog photo, Ah Ma cooked, sleep early

## Project structure

```
app.py                 # page navigation
homescreen.py          # chat list with the floating Catch up button
select_group_chat.py   # pick group chats + version
catchup.py             # results page
cards.py               # how each card is displayed
chat_data.py           # reads the chats and finds unread messages
gemma.py               # prompts and Ollama calls (V1–V4)
chat_list.py           # chat list shown on the homescreen
style.py               # CSS for the floating button
data/                  # made-up chats + last_read times
```
