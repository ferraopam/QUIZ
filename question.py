class Question:

    def __init__(self, qdata, opt1, opt2, opt3, opt4, cananswer):
        self.qdata = qdata
        self.opt1 = opt1
        self.opt2 = opt2
        self.opt3 = opt3
        self.opt4 = opt4
        self.cananswer = cananswer


    
    def __str__(self):
        return f"{self.qdata} \n A.{self.opt1} \n B.{self.opt2} \n C.{self.opt3} \n D.{self.opt4}"



