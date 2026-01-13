from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [(Question(element["text"], element["answer"])) for element in question_data]

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You have completed the quiz.")
print(f"Your final score was: {quiz_brain.score}/{quiz_brain.question_number}")