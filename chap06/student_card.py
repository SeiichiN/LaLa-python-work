#p230
# クラスの基本

class StudentCard:
    school_name = 'Python 大学'
    @classmethod
    def show_school_name(cls):
        print(cls.school_name)
        
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def print_info(self):
        print('学籍番号:', self.id)
        print('氏名:', self.name)


print(__name__)
if __name__ == '__main__':
    StudentCard.show_school_name()

    a = StudentCard(1234, '鈴木太郎')
    b = StudentCard(1235, '佐藤花子')

    a.print_info()
    b.print_info()
    a.show_school_name()

