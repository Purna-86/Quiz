import random

def display_welcome():
    print("Welcome to the Quiz Game!")
    print("Answer the following questions and test your knowledge.")
    print("--------------------------------------------------------")

def load_questions():
    # Add your questions and answers here
    questions = [
        {"question": "What is the capital of France?", "choices": ["Berlin", "Paris", "Rome", "Madrid"], "correct_answer": "Paris"},
        {"question": "Which planet is known as the Red Planet?", "choices": ["Venus", "Mars", "Jupiter","Saturn"], "correct_answer": "Mars"},
        {"question": "Who is the Founder of YSRCP Political Party in A.P?",
           "choices": ["Nara Chandrababu Naidu","YS JaganMohanReddy","Pawan Kalyan","K.A Paul"],
           "correct_answer":"YS JaganMohanReddy"
           },
       {
       "question": "How do you stay updated on industry trends and advancements?",
            "choices": ["Attend workshops and conferences regularly", " Read industry publications and blogs", " Engage in online courses and webinars", "None of the above"],
            "correct_answer": " Attend workshops and conferences regularly"
            },
       {
        "question": "How do you approach making important decisions?",
            "choices": ["Rely on gut instincts", " Gather relevant information and analyze the options", " Seek consensus from the team", "Avoid making decisions whenever possible"],
            "correct_answer": "Gather relevant information and analyze the options"
            },
       {
       "question": "When faced with a complex problem, your approach is to:",
            "choices": ["Jump into solving it immediately", "Analyze the problem, break it down, and then develop a solution", "Seek help from colleagues or superiors", "Ignore it and hope it goes away"],
            "correct_answer": "Analyze the problem, break it down, and then develop a solution"
            },
      {
       "question": "In a team project, how do you contribute most effectively?",
            "choices": ["Take charge and provide direction", " Collaborate with team members, valuing everyone's input", "Prefer working independently", "Contribute only when necessary"],
            "correct_answer": " Collaborate with team members, valuing everyone's input"
            },
       {
        "question": "When leading a team, what leadership style do you typically adopt?",
            "choices": ["Authoritarian – providing clear instructions and expectations", "Democratic – involving team members in decision-making", " Laissez-faire – giving team members full autonomy", " I prefer not to lead"],
            "correct_answer": "Democratic – involving team members in decision-making"
            },
    ]
    return questions

def present_question(question):
    print(question["question"])
    for choice in question["choices"]:
        print(choice)
    user_answer = input("Your answer: ").upper()
    return user_answer

def evaluate_answer(user_answer, correct_answer):
    return user_answer == correct_answer

def display_feedback(is_correct, correct_answer):
    if is_correct:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")

def play_quiz():
    questions = load_questions()
    score = 0

    for question in questions:
        user_answer = present_question(question)
        is_correct = evaluate_answer(user_answer, question["correct_answer"])
        display_feedback(is_correct, question["correct_answer"])

        if is_correct:
            score += 1

    return score

def display_results(score, total_questions):
    print("--------------------------------------------------------")
    print(f"Your final score is: {score}/{total_questions}")
    print("Thanks for playing!")

def play_again():
    return input("Do you want to play again? (yes/no): ").lower() == "yes"

def main():
    display_welcome()
    
    while True:
        score = play_quiz()
        display_results(score, len(load_questions()))

        if not play_again():
            break

if __name__ == "__main__":
    main()

