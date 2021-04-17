from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    answer = question["answer"]
    new_question = Question(question_text, answer)
    question_bank.append(new_question)

print(question_bank[0].text)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("\nYou've completed the Quiz")
print("Your final score was: {}/{}".format(
      quiz.score, quiz.question_number))
