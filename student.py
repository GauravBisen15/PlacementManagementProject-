class Student():
    def __init__(self,name,roll,cgpa,branch,placed=False):
        self.name=name
        self.roll=roll
        self.cgpa=cgpa
        self.branch=branch
        self.placed=placed


    def __str__(self):

        status="Placed"if self.placed else "Not Placed"
        return f"{self.roll} | {self.name} | {self.branch} | {self.cgpa} | {status}"    
