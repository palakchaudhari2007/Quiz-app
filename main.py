from quiz import run_quiz
import json

def save_score(score, total):
    result = {
        "score": score,
        "total": total
    }

    with open("score.json", "w") as f:
        json.dump(result, f, indent=4)

def main():
    print("🧠 Welcome to the Quiz App!")

    score, total = run_quiz()

    print(f"\n🏆 Final Score: {score}/{total}")

    save_score(score, total)
    print("📦 Score saved to score.json")

if __name__ == "__main__":
    main()