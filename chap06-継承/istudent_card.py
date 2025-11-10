# p243 継承

from student_card import StudentCard

class IStudentCard(StudentCard):
    def __init__(self, id, name, nationality):
        self.nationality = nationality
        super().__init__(id, name)
        
    def print_info(self):
        print(f'国籍: {self.nationality}')
        super().print_info()


if __name__ == '__main__':
    istCard = IStudentCard(1240, '浦島太郎', '日本')
    istCard.print_info()  # id,name
    
    
        
