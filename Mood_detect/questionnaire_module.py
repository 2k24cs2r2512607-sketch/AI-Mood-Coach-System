# -------------------------------
# Questionnaire Module
# -------------------------------

# Question Bank (Balanced 3-3-3)
QUESTION_BANK = [

    # --- Overloaded ---
    ("I feel mentally tired even after resting.", "Overloaded"),
    ("I find myself scrolling without actually reading anything.", "Overloaded"),
    ("My brain feels foggy or hard to focus.", "Overloaded"),

    # --- Negative ---
    ("I am enjoying things less than I usually do.", "Negative"),
    ("I feel more irritated or sad than usual today.", "Negative"),
    ("I feel like staying alone and avoiding everyone.", "Negative"),

    # --- Positive ---
    ("I feel capable of finishing my tasks today.", "Positive"),
    ("I am feeling grateful or happy about something.", "Positive"),
    ("I feel calm and physically energetic right now.", "Positive"),
]


# -------------------------------
# Input Validation
# -------------------------------
def get_valid_boolean():
    while True:
        ans = input("👉 Enter True or False (T/F): ").strip().lower()
        if ans in ("true", "t"):
            return True
        elif ans in ("false", "f"):
            return False
        else:
            print("❌ Invalid input. Please type True or False.\n")


# -------------------------------
# Questionnaire Mood Detection
# -------------------------------
def questionnaire_mood():
    """
    Runs mood questionnaire and
    returns detected mood.
    """

    scores = {
        "Overloaded": 0,
        "Negative": 0,
        "Positive": 0
    }

    print("\n" + "="*40)
    print("🧠 MOOD QUESTIONNAIRE")
    print("Answer honestly with True or False")
    print("="*40 + "\n")

    for i, (question, mood_type) in enumerate(QUESTION_BANK, start=1):
        print(f"{i}. {question}")
        if get_valid_boolean():
            scores[mood_type] += 1

    # Decision Logic
    max_score = max(scores.values())

    if max_score == 0:
        return "Neutral"

    winners = [mood for mood, score in scores.items() if score == max_score]

    if len(winners) > 1:
        # Priority: Overloaded > Negative > Positive
        if "Overloaded" in winners:
            return "Overloaded"
        elif "Negative" in winners:
            return "Negative"
        return "Mixed"

    return winners[0]