# 学生証

class StudentCard:
    school_name = 'Python大学'
    @classmethod
    def pr_school_name(cls):
        print(cls.school_name)
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def print_info(self):
        print('学籍番号:', self.id)
        print('氏名:', self.name)
# クラス定義はここまで

# このファイルを実行した場合
if __name__ == '__main__':
    StudentCard.pr_school_name()
    # インスタンスを生成
    a = StudentCard(1234, '鈴木太郎')
    b = StudentCard(1235, '佐藤花子')
    # print(a.school_name)
    a.print_info()
    b.print_info()

