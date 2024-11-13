from character import Character


class Potion(Character):
    def __init__(self, i_type):
        super().__init__()
        self.type = i_type
        self.hp = 100