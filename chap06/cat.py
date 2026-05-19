# cat.py

class Cat:
    def __init__(self, name):
        self.name = name

    def say(self):
        print(f'{self.name}: にゃあ')

        
if __name__ == '__main__':
    cat1 = Cat('たま')
    cat2 = Cat('れお')
    cat1.say()
    cat2.say()
