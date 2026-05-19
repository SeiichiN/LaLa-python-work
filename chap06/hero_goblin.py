# hero_goblin.py

from hero import Hero
from goblin import Goblin

hero = Hero('勇者')
goblin = Goblin('ゴブリン')
hero.attack(goblin)
goblin.attack(hero)
hero.run()
goblin.run()
