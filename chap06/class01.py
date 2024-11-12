# 空のクラス

class StudentCard:
    school_name = 'Python 大学'
    
    @classmethod
    def print_name(cls):
        print('学校名:', cls.school_name)
        
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    def print_info(self):
        print('学籍番号:', self.id)
        print('氏名:', self.name)
        print('学校名:', self.school_name)


# このファイルがpythonコマンドで
# 呼び出された場合
if __name__ == '__main__':
    StudentCard.print_name()        

    a1 = StudentCard(1234, '浦島太郎')
    a1.print_info()

    # StudentCard.school_name = 'Java大学'

    a2 = StudentCard(1235, '乙姫')
    a2.print_info()

