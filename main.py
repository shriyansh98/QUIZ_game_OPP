from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# for i in range(0,len(question_data):
#     question_bank = Question(question_data[i]["text"],question_data[i]["answer"])
#                )

for question in question_data:
    ques_text = question['text']
    ques_ans = question['answer']
    new_question = Question(ques_text,ques_ans)
    question_bank.append(new_question)

 
qb = QuizBrain(question_bank)
while qb.still_has_questions():
    qb.next_question()

print(f"YOU Have Finished The QUIZ\nYOUR SCORE : {qb.score}/{len(qb.list)}")