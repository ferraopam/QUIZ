from question import Question


class QuestionService:

    questions =  []


    @classmethod
    def loadQuestions(cls):
        with open("Questions.txt") as file:
            data = file.readlines()
            for line in data:
                q = line.split(",")
                cls.questions.append(Question(*q))  #  *q maps with correct options
    
    @classmethod
    def begin_quiz(cls):
        cls.loadQuestions()
        print(f"Total questions found: {len(cls.questions)}")
        
        num_correct = 0
        num_wrong = 0
        for i, question in enumerate(cls.questions):
            print(f"{i+1}. {question} ")
            ch = input("enter your choice [A, B, C, D] only......")

            if ch == question.cananswer.strip():
                num_correct += 1
            else:
                num_wrong +=1

        cls.show_result(num_correct, num_wrong)

    
    
    @classmethod
    def show_result(cls, correct, wrong): #parameteres used here take th value from //
                                          #above num_correct & num_wrong and used for operation
        print("*"*50)
        total_q = len(cls.questions)
        print(f"Total Question: {total_q}")
        print(f"No. of correct qstns: {correct}")
        print(f"No. of wrong qstns: {wrong}")

        percentage = ((correct)/ (total_q)) * 100

        if percentage > 65:
            print("Congratulations!!!!!!!")
        else:
            print("Better luck next time.......")