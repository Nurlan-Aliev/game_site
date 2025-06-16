from abc import ABC


class Character(ABC):
    def __init__(self, name: str, health: int, power: int):
        self.name = name.title()
        self._health = health
        self._full_health = health
        self.power = power
        self._alife = True

    @property
    def health_percent(self):
        return int(self._health / self._full_health * 100)

    def attack(self, target: "Character"):
        target.health -= self.power

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = min(value, self._full_health)
        if self.health <= 0:
            self._alife = False

    @property
    def alife(self):
        return self._alife

    def health_bar(self):
        filled_percentage = int((self._health / self._full_health) * 100)
        empty_percentage = 100 - filled_percentage
        return f"{self.name.center(14, ' ')}: [{(filled_percentage * '=') + (empty_percentage * ' ')}]"
