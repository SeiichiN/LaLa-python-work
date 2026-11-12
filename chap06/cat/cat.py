# 6.1.3 クラスの書き方

class Cat:
    def __init__(self, name):
        self.name = name

    def say(self):
        print(f'{self.name}: にゃあ')

        
if __name__ == '__main__':
    cat1 = Cat('たま')
    cat2 = Cat('レオ')
    cat1.say()
    cat2.say()
