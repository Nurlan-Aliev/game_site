import random
from game.classes.base import Character


class Monsters(Character):
    def __init__(
        self,
        name: str,
        health: int,
        power: int,
        exp_reward: int,
    ):
        super().__init__(name, health, power)
        self.exp_reward = exp_reward

    def __str__(self):
        return self.name


class BossMonster(Monsters):

    def __init__(
        self,
        name: str,
        health: int,
        power: int,
        exp_reward: int,
        ultimate_phrase: str,
        ultimate_power: int,
    ):
        super().__init__(name, health, power, exp_reward)
        self.ultimate_phrase = ultimate_phrase
        self.ultimate_power = ultimate_power

    def ultimate_attack(self, target: Character):
        target.health -= self.ultimate_power
        return self.ultimate_phrase.upper()

    def attack(self, target: Character):
        if random.randint(1, 4) == 4:
            return self.ultimate_attack(target)
        target.health -= self.power
