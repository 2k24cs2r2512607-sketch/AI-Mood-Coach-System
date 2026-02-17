# -------------------------------
# MAIN CONTROLLER
# -------------------------------
from colorama import Fore, Style, init
init(autoreset=True)
from text_module import process_text_input, give_help
from questionnaire_module import questionnaire_mood


# -------------------------------
# Final Combination Logic
# -------------------------------
def combine_moods(text_mood, questionnaire_mood):
    """
    Final decision logic:
    - If both agree → return that mood
    - If different → return Neutral
    """

    if text_mood == questionnaire_mood:
        return text_mood
    return "Neutral"


# -------------------------------
# Execution Flow
# -------------------------------
def run_mood_coach():

    print("\n🌈 MOOD COACH AI 🌈")
    print("=" * 50)

    # STEP 1 → TEXT INPUT
    user_input = input("\nHow are you feeling right now? ")

    text_mood = process_text_input(user_input)
    print(f"\n🤖 Text Analysis Result: {text_mood}")

    # STEP 2 → QUESTIONNAIRE
    print("\nNow let's verify with a short questionnaire.")
    questionnaire_result = questionnaire_mood()
    print(f"\n🧠 Questionnaire Result: {questionnaire_result}")

    # STEP 3 → FINAL COMBINATION
    final_mood = combine_moods(text_mood, questionnaire_result)

    print("\n" + "=" * 50)
    print(f"🎯 FINAL VERIFIED MOOD: {final_mood.upper()}")
    print("=" * 50)

    # STEP 4 → HELP SYSTEM
    give_help(final_mood)


# Run system
if __name__ == "__main__":
    run_mood_coach()