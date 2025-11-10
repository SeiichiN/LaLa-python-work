# クラスの復習

class Robot:
    def __init__(self, name, fuel):
        self.name = name
        self.fuel = fuel
    def run(self):
        if self.fuel >= 10:
            print(f'{self.name}は走った。')
            self.fuel -= 10
            print(f'残り燃料は{self.fuel}')
        else:
            print('燃料不足です。')
    def charge(self, fuel):
        self.fuel = fuel
        print(f'燃料を{fuel}追加した。')
    

# print(__name__)
# このファイルが実行された場合
if __name__ == '__main__':
    robo1 = Robot('太郎', 100)
    robo2 = Robot('花子', 100)
    i = 0
    while(i<12):
        robo1.run()
        i += 1
    robo1.charge(40)
    robo1.run()
    
