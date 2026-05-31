"""
Pilots Quiz for Commercial Aviation
"""

def main():
    questions = [
        {
            "question": "What is the minimum safe altitude over a congested area?",
            "options": [
                "A. 500 feet above the highest obstacle",
                "B. 1,000 feet above the highest obstacle within a horizontal radius of 2,000 feet",
                "C. 2,000 feet above ground level",
                "D. 500 feet above ground level"
            ],
            "answer": "B"
        },
        {
            "question": "What does a flashing red light from the control tower mean to an aircraft on the ground?",
            "options": [
                "A. Cleared to taxi",
                "B. Stop",
                "C. Taxi clear of runway in use",
                "D. Return to starting point on airport"
            ],
            "answer": "C"
        },
        {
            "question": "What is the primary purpose of the rudder on an aircraft?",
            "options": [
                "A. To control pitch",
                "B. To control yaw",
                "C. To control roll",
                "D. To increase lift"
            ],
            "answer": "B"
        },
        {
            "question": "Which instrument indicates whether the aircraft is climbing, descending, or in level flight?",
            "options": [
                "A. Altimeter",
                "B. Airspeed Indicator",
                "C. Vertical Speed Indicator",
                "D. Heading Indicator"
            ],
            "answer": "C"
        },
        {
            "question": "What is the standard direction of turns in a holding pattern?",
            "options": [
                "A. Left",
                "B. Right",
                "C. Either direction",
                "D. Depends on ATC instructions"
            ],
            "answer": "B"
        }
    ]

    score = 0
    print("\n--- Pilots Quiz: Commercial Aviation ---\n")
    for idx, q in enumerate(questions, 1):
        print(f"Q{idx}: {q['question']}")
        for opt in q["options"]:
            print(opt)
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {q['answer']}.\n")
    print(f"Quiz complete! Your score: {score}/{len(questions)}")

if __name__ == "__main__":
    main()
