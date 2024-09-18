class Student:
    def __init__(self, id, name):
        self.id  = id
        self.name  = name

    def display_information(self):
        print(f"The student name is: {self.name} and stuydent id is: {self.id}")

class Class_Marks(Student):
    def __init__(self, algo, DS, calc, id, name) :
        super().__init__(id,name)
        self.algo_marks = algo
        self.DS_marks = DS
        self.calculus_marks = calc

    def printmarks(self) :
        print(f"Algo marks are {self.algo_marks}\nDS marks are {self.DS_marks}\nCalculus marks are {self.calculus_marks}")

class Class_Result(Class_Marks) :
    def __init__(self, algo, DS, calc, id, name) :
        super().__init__(algo, DS, calc, id, name)
    
    def printresult(self) :
        print(f"Total marks are {self.algo_marks + self.DS_marks + self.calculus_marks}\nAverage is {(self.algo_marks + self.DS_marks  +self.calculus_marks)/3}")
        

result = Class_Result(98, 87, 76, "3457853","Laiba")
result.printresult()
