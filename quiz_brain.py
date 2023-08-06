

class QuizBrain():

    def __init__(self,q_list):
        self.number = 0
        self.list = q_list
        self.score  = 0
    
    def input_handler(self,ans):
        if ans == 't':
           return 'True'
        elif ans == 'f':
            return 'False'
        else:
            user_ans = input("please input a correct letter ANS? :")
            self.input_handler(user_ans)


    def next_question(self):
        current_question = self.list[self.number] 
        self.number += 1
        user_ans = input(f"Q.{self.number}: {current_question.text} (T/F): t").lower()
        self.input_handler(user_ans)
        # print(current_question.answer)
        self.check_ans(user_ans, current_question.answer)
    
    def still_has_questions(self):
        return self.number < len(self.list)
    
    def check_ans(self,u_ans,correct_ans):
        
        if u_ans == correct_ans:
            print("you got it right")
            self.score += 1

        else:
            print("that was wrong")
        
        print(f"the correct ans was: {correct_ans} SCORE:{self.score}/{self.number}")
        
    

           