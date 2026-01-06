from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from game_art import logo

print(logo)

question_bank = []

for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()
