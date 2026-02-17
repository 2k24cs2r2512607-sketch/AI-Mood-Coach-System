import string
import difflib as df
import random
import json
import sys

# -------------------------------
# Load Mood Database
# -------------------------------
try:
    with open('mood_data.json', 'r') as file:
        mood_database = json.load(file)
except FileNotFoundError:
    print("❌ Error: 'mood_data.json' file not found!")
    sys.exit()
except json.JSONDecodeError:
    print("❌ Error: 'mood_data.json' formatting error.")
    sys.exit()


# -------------------------------
# Constants
# -------------------------------
STOPWORDS = {"i", "am", "the", "a", "is", "are", "to", "feel", "feeling"}

NEGATIONS = {"not", "no", "never", "dont"}

POSITIVE_WORDS = {"good", "positive", "happy", "joyful", "excited",
                  "grateful", "wonderful", "great"}

NEGATIVE_WORDS = {"bad", "sad", "angry", "anxious",
                  "depressed", "terrible", "awful"}

NUMB_WORDS = {"bored", "numb", "nothing", "fine",
              "ok", "meh", "empty", "scrolling",
              "tired", "blank"}


# -------------------------------
# Text Mood Detection Engine
# -------------------------------
def detect_text_mood(tokenized_words):
    """
    Detect mood using rule-based sentiment
    with basic negation handling.
    """

    counts = {"Positive": 0, "Negative": 0, "Overloaded": 0}
    is_negated = False

    for word in tokenized_words:

        # Negation handling
        if word in NEGATIONS or df.get_close_matches(word, NEGATIONS, n=1, cutoff=0.7):
            is_negated = True
            continue

        pos_match = df.get_close_matches(word, POSITIVE_WORDS, n=1, cutoff=0.7)
        neg_match = df.get_close_matches(word, NEGATIVE_WORDS, n=1, cutoff=0.7)
        numb_match = df.get_close_matches(word, NUMB_WORDS, n=1, cutoff=0.7)

        if pos_match:
            counts["Negative" if is_negated else "Positive"] += 1
            is_negated = False

        elif neg_match:
            counts["Positive" if is_negated else "Negative"] += 1
            is_negated = False

        elif numb_match:
            counts["Overloaded"] += 1
            is_negated = False

    # Decision Logic
    max_score = max(counts.values())

    if max_score == 0:
        return "Neutral"

    winners = [mood for mood, score in counts.items() if score == max_score]

    if len(winners) > 1:
        return "Mixed"

    return winners[0]


# -------------------------------
# Text Preprocessing Wrapper
# -------------------------------
def process_text_input(user_input):
    """
    Cleans and tokenizes user input,
    then returns detected mood.
    """

    user_input = user_input.lower()
    clean_text = "".join(ch for ch in user_input if ch not in string.punctuation)
    tokens = [word for word in clean_text.split() if word not in STOPWORDS]

    return detect_text_mood(tokens)


# -------------------------------
# Help System
# -------------------------------
def give_help(mood):

    data = mood_database.get(mood, mood_database.get("Neutral"))

    if mood == "Overloaded":
        print("\n⚠️  CRITICAL DATA DETECTED ⚠️")
        st = input("Enter your screen time (hours/day): ")

        try:
            st_val = float(st)
            if st_val > 0:
                days_per_year = (st_val * 365) / 24
                print(f"\n📊 You lose approx {days_per_year:.1f} full days/year to screens.")
                if st_val > 3:
                    print("⚠️ Cognitive fatigue risk increasing.")
        except ValueError:
            print("Invalid number entered. Skipping screen analysis.")

    print("\n" + "═"*50)
    print(f"✨ {mood.upper()} MOOD ANALYSIS ✨")
    print("═"*50)
    print(f"STATUS  : {mood}")
    print(f"ANALYSIS: {data.get('analysis', 'Insufficient data.')}")
    print(f"SCIENCE : {data.get('science_tip', data.get('why_it_matters', 'N/A'))}")
    print(f"ADVICE  : {data.get('deep_advice', 'Take a mindful pause.')}")
    print(f"TASK    : {random.choice(data.get('tasks', ['Take a short walk.']))}")
    print("═"*50)