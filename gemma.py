import time
import ollama
import json

model = "gemma4:e4b"
client = ollama.Client(host="http://127.0.0.1:11434", trust_env=False)

#v1: plain prompt
# pass the whole chat to the model and simply ask to summarize it.

def v1_summarize(chat):
    #chat here should already have the unread msges
    chattxt = ""
    for msg in chat:
        chattxt = chattxt + msg["sender"] + ": " + msg["text"] + "\n"

    prompt = "Here are unread messages from a group chat. \n" \
    " Please summarize the messages, and provide a summary of the key points " \
    "\n and any actionable items."

    start_time = time.time()
    response = client.chat(
        model=model,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": chattxt}
        ],
    )
    seconds = time.time() - start_time
    summary = response["message"]["content"]
    wordcnt = len(summary.split())
    return summary, seconds, wordcnt

def v2_summarize(chat):
    # turn msg into json cards as the output
    chattxt = ""
    for msg in chat:
        chattxt = chattxt + msg["sender"] + ": " + msg["text"] + "\n"

    prompt = """

You are helping Ella catch up on the unread messages in a group chat. Read these messages and reply
ONLY with JSOn in this exact format:

{"Cards": [
{"type": "asked_you, agreed, suggested, task or deadline",
"text": "one short sentence, under 30 words",
"changed_from": "the previous plan if it changed, or otherwise this should be empty",
"source": ["the exact message(s) that this came from, written as Name: message"]
}]
}

Skip any messages that are not important, like small talks, memes. 

Messages:
""" + chattxt

    start_time = time.time()
    response = client.chat(
        model=model,
        messages=[{"role": "system", "content": prompt}],
        format="json",
        options={"temperature": 0},
    )

    seconds = time.time() - start_time
    raw = response["message"]["content"]

    print("\n===== GEMMA RAW OUTPUT =====")
    print(raw)
    print("===== took", round(seconds), "seconds =====")

    # turn json into python data
    try:
        # if model switches to lowercase prcaution
        data = json.loads(raw)
        if "Cards" in data:
            cards = data["Cards"]
        elif "cards" in data:
            cards = data["cards"]
    except Exception as e:
        print("Error parsing JSON from Gemma output:", e)
        cards = None

    return cards, raw, seconds

def v3_summarize(chat):
    # turn msg into json cards as the output
    chattxt = ""
    for msg in chat:
        chattxt = chattxt + msg["sender"] + ": " + msg["text"] + "\n"

    prompt = """

You are helping Ella catch up on the unread messages in a group chat. Read these messages and reply
ONLY with JSON in this exact format:

{"cards": [
  {"type": "...", "text": "...", "changed_from": "...", "source": ["..."]}
]}

Card types (Use exactly one of these for "type"):
- "asked_you" - if the message is asking Ella to do something
- "agreed" - the group clearly said yes to the plan (e.g: "okay", "can", "confirmed")
- "suggested" - someone suggested a plan or proposed something, but the group did not agree or replied with either doubt or sarcasm
- "task" - Someone who is not Ella who agreed to do something or do a task.
- "deadline" - if the message contains a due date or a time limit for submitting or finishing something.

Criteria to take note:
1. Make ONE card per topic and show only the LATEST version. if any plan changes, put the earlier plan in "changed_from" and do not make any separate cards for old plans.
include only the messages in the "source" field that show the final decision and requests.
2. Include every final decision, deadline and task for the group and not only just things for Ella.
3. For tasks, only say who will do it if the message says so. 
4. Only use information in the messages. Do not add deadlines, priorities, tasks or other information that nobody mentioned in the message.
5. write the short text description in third person e.g "Marcus asked Ella..."
6. if there are no earlier plan, leave the "changed_from" to "" (an empty string).
7. Skip small talks and memes. 
8. Different requests must be separate cards and every request to Ella must be its own "asked_you" card

Messages:
""" + chattxt

    start_time = time.time()
    response = client.chat(
        model=model,
        messages=[{"role": "system", "content": prompt}],
        format="json",
        options={"temperature": 0},
    )

    seconds = time.time() - start_time
    raw = response["message"]["content"]

    print("\n===== GEMMA RAW OUTPUT =====")
    print(raw)
    print("===== took", round(seconds), "seconds =====")

    # turn json into python data
    try:
        # if model switches to lowercase prcaution
        data = json.loads(raw)
        if "Cards" in data:
            cards = data["Cards"]
        elif "cards" in data:
            cards = data["cards"]
        else:
            cards = None
    except Exception as e:
        print("Error parsing JSON from Gemma output:", e)
        cards = None

    return cards, raw, seconds

# focus on latecy

def v4_summarize(chat):
    # turn msg into json cards as the output
    chattxt = ""
    for msg in chat:
        chattxt = chattxt + msg["sender"] + ": " + msg["text"] + "\n"

    prompt = """

You are helping Ella catch up on the unread messages in a group chat. Read these messages and reply
ONLY with JSON in this exact format:

{"cards": [
  {"type": "...", "text": "...", "changed_from": "...", "source": ["..."]}
]}

Card types (Use exactly one of these for "type"):
- "asked_you" - if the message is asking Ella to do something
- "agreed" - the group clearly said yes to the plan (e.g: "okay", "can", "confirmed")
- "suggested" - someone suggested a plan or proposed something, but the group did not agree or replied with either doubt or sarcasm
- "task" - Someone who is not Ella who agreed to do something or do a task.
- "deadline" - if the message contains a due date or a time limit for submitting or finishing something.

Criteria to take note:
1. Make ONE card per topic and show only the LATEST version. if any plan changes, put the earlier plan in "changed_from" and do not make any separate cards for old plans.
include only the messages in the "source" field that show the final decision and requests.
2. Include every final decision, deadline and task for the group and not only just things for Ella.
3. For tasks, only say who will do it if the message says so. 
4. Only use information in the messages. Do not add deadlines, priorities, tasks or other information that nobody mentioned in the message.
5. write the short text description in third person e.g "Marcus asked Ella..."
6. if there are no earlier plan, leave the "changed_from" to "" (an empty string).
7. Skip small talks and memes. 
8. Different requests must be separate cards and every request to Ella must be its own "asked_you" card

Messages:
""" + chattxt

    start_time = time.time()
    response = client.chat(
        model="gemma4:e2b",
        messages=[{"role": "system", "content": prompt}],
        format="json",
        options={"temperature": 0},
    )

    seconds = time.time() - start_time
    raw = response["message"]["content"]

    print("\n===== GEMMA RAW OUTPUT =====")
    print(raw)
    print("===== took", round(seconds), "seconds =====")

    # turn json into python data
    try:
        # if model switches to lowercase prcaution
        data = json.loads(raw)
        if "Cards" in data:
            cards = data["Cards"]
        elif "cards" in data:
            cards = data["cards"]
        else:
            cards = None
    except Exception as e:
        print("Error parsing JSON from Gemma output:", e)
        cards = None

    return cards, raw, seconds