fake_results = {
    "1D Group 4": [
        {
            "type": "asked_you",
            "text": "Marcus asked you to update slide 5 with the new user flow before Fri",
            "changed_from": "",
            "source": ["Marcus: @Ella can u update slide 5 with the new user flow before fri?"],
            "verified": True,
        },
        {
            "type": "agreed",
            "text": "Meeting: Fri 4pm on Zoom",
            "changed_from": "Thu 2pm in school, then Fri 3pm Zoom",
            "source": [
                "Marcus: also fri 3pm can shift to 4pm? i got prof consult at 3",
                "Marcus: ok fri 4pm zoom final",
            ],
            "verified": True,
        },
        {
            "type": "suggested",
            "text": "Do a survey with 10 people",
            "changed_from": "",
            "source": ["Marcus: maybe we also do a survey with 10 ppl?", "John: 10 ppl a lot leh"],
            "verified": True,
        },
        {
            "type": "deadline",
            "text": "Report and video due Sun 11.59pm",
            "changed_from": "",
            "source": ["Marcus: report due sun 11.59pm, video also sun"],
            "verified": True,
        },
        {
            "type": "agreed",
            "text": "Priya will book the room for Sat",
            "changed_from": "",
            "source": ["Priya: someone book room for sat to record video pls"],
            "verified": False,   # nobody actually agreed, so this should be flagged
        },
    ],
    "Dance exco": [
        {
            "type": "asked_you",
            "text": "Aisyah asked you to confirm the auditorium booking by Fri",
            "changed_from": "",
            "source": ["Aisyah: @Ella can u confirm the auditorium booking for the performance by fri? need ur email"],
            "verified": True,
        },
        {
            "type": "agreed",
            "text": "Practice: Wed 7pm, same hall",
            "changed_from": "Tue 7pm",
            "source": ["Aisyah: wait tues cannot, hall booked by another club", "Wei Ling: ok wed 7pm confirmed, same hall"],
            "verified": True,
        },
    ],
    "Family": [
        {
            "type": "agreed",
            "text": "Lunch: Sun 12pm at Ah Ma's house",
            "changed_from": "Sat dinner 7pm",
            "source": ["Mum: ah ma say sat she not free, change to sun lunch 12pm instead"],
            "verified": True,
        },
    ],
}