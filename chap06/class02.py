from student_card import StudentCard

class IStudentCard(StudentCard):
    def __init__(self, id, name, nationality):
        self.nationality = nationality
        super().__init__(id, name)
    def print_info(self):
        print(f'国籍: {self.nationality}')
        super().print_info()
        

sc1 = IStudentCard(1234, '山下一郎', 'Japan')
sc2 = IStudentCard(1235, '木下花子', 'U.S.')
sc1.print_info()
sc2.print_info()
