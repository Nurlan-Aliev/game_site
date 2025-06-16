from game.src.classes.heroes import Hero


class Weapon:
    def __init__(self, name: str, damage: int, weapon_type: str, hero_class: Hero):
        self.name = name
        self.damage = damage
        self.weapon_type = weapon_type
        self.hero_class = hero_class

    def __str__(self):
        return f"{self.name} ({self.weapon_type}, Урон: {self.damage})"
