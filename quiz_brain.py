class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False)? ")
        self.check_answer(user_answer, current_question) 
        self.question_number += 1
    
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            print(f"You correctly answered {self.score} out of {len(self.question_list)} questions.")
            return False
        
    def check_answer(self, user_answer, current_question):
        if user_answer.lower() == current_question.answer.lower():
            print("Your answer is correct")
            self.score += 1
        else:
            print("Sorry, your answer is wrong")
            print(f"The correct answer is {current_question.answer}")
        print(f"Current score is: {self.score}\n")