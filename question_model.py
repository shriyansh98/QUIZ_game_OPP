from data import question_data



class Question:
    

    def __init__(self,q_text,q_answer):
        self.text = q_text
        self.answer =q_answer

# new_q = Question(question_data[0]["text"],"false")
# print(new_q.text)