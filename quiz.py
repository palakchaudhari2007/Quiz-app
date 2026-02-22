import json

def load_questions():
    with open("questions.json", "r") as f:
        data = json.load(f)
    return data["questions"]

def run_quiz():
    questions = load_questions()
    score = 0

    for q in questions:
        print("\n" + q["question"])

        for i, option in enumerate(q["options"], 1):
            print(f"{i}. {option}")

        try:
            choice = int(input("Your answer (number): "))
            selected = q["options"][choice - 1]

            if selected == q["answer"]:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer: {q['answer']}")

        except:
            print("⚠ Invalid input. Skipping question.")

    return score, len(questions)