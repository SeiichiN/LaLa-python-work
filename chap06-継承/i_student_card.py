# i_student_card

from student_card import StudentCard

class IStudentCard(StudentCard):
    def __init__(self, id, name, nationality):
        self.nationality = nationality
        super().__init__(id, name)
    def print_info(self):
        super().print_info()  # 親クラスのメソッド呼出
        print('国籍:', self.nationality)
