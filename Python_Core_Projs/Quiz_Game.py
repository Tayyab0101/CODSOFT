import random

questions = [
    {
        "question": "Which planet is known as the 'Red Planet'?",
        "option1": "Venus",
        "option2": "Mars",
        "option3": "Jupiter",
        "option4": "Saturn",
        "correct_answer": "B"
    },
    {
        "question": "Who is the author of the Harry Potter series?",
        "option1": "J.K. Rowling",
        "option2": "Stephen King",
        "option3": "George R.R. Martin",
        "option4": "Suzanne Collins",
        "correct_answer": "A"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "option1": "Ag",
        "option2": "Au",
        "option3": "Fe",
        "option4": "Pb",
        "correct_answer": "B"
    },
    {
        "question": "Which of the following is not a primary color?",
        "option1": "Red",
        "option2": "Green",
        "option3": "Yellow",
        "option4": "Purple",
        "correct_answer": "D"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "option1": "Leonardo da Vinci",
        "option2": "Michelangelo",
        "option3": "Pablo Picasso",
        "option4": "Vincent van Gogh",
        "correct_answer": "A"
    }
]

random.shuffle(questions)  # Shuffle the questions list

correct_answers = 0
print("Welcome to Quiz Game")
for i, question in enumerate(questions):
    print("                                                             ")
    print(f"{i+1}. {question['question']}: ")
    print(f"Option1: {question['option1']}")
    print(f"Option2: {question['option2']}")
    print(f"Option3: {question['option3']}")
    print(f"Option4: {question['option4']}")
    
    user_answer = input("Choose A/B/C/D: ").upper()
    
    if user_answer not in ['A', 'B', 'C', 'D']:
        print("Invalid option. Skipping to next question.")
        continue
    
    if user_answer == question["correct_answer"]:
        print("Correct Answer")
        correct_answers += 1
    else:
        print("Incorrect Answer")
    
    print(f"Current score is {correct_answers}/{i + 1}")
        
print("Quiz completed!")
print(f"You answered {correct_answers} out of {len(questions)} questions correctly.")
