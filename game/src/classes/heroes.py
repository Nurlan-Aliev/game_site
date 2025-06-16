from game.src.classes.monster import Monsters
from game.src.utils import show, option
from game.src.classes.base import Character
from abc import ABC, abstractmethod


class Hero(Character, ABC):
    def __init__(self, name: str, health: int, power: int):
        super().__init__(name, health, power)
        self._xp = 0
        self.level = 1
        self._change_lvl_exp = 100

    @property
    def xp(self):
        return self._xp

    @xp.setter
    def xp(self, value):
        if value > self._xp:
            self._xp = value
        self.check_level_up()

    def check_level_up(self):
        while self._xp >= self._change_lvl_exp:
            self.lvl_up()
            self._change_lvl_exp += self._change_lvl_exp // 100 * 15

    def lvl_up(self):
        self.level += 1
        self._full_health += self._full_health // 10
        self.health = self._full_health
        show(f"\n{'<'*30} LEVEL UP {'>'*30}\n", style="rgb(215,170,100)")

    @abstractmethod
    def ultimate(self, target):
        pass

    @abstractmethod
    def __str__(self):
        return (
            f"\nHero's name: {self.name}\n"
            f"Health: {self.health}\n"
            f"Damage: {self.power}\n"
            f"level: {self.level}\n"
            f"xp: {self.xp}\n"
        )

    def __iter__(self):
        yield f"\nHero's name: {self.name}\n"
        yield f"Health: {self.health}\n"
        yield f"Damage: {self.power}\n"
        yield f"level: {self.level}\n"
        yield f"xp: {self.xp}\n"

    @abstractmethod
    def perform_attack(self, attack: str, target: Character):
        pass

    def fight(self, enemy: Monsters):
        choices = {"usual attack": self.attack, "ultimate": self.ultimate}

        while self.alife:
            show(self.health_bar(), style="green", second=0.01)
            show(enemy.health_bar(), style="red", second=0.01)

            kick: str = option("how do you want to attack", choices.keys())

            show(choices[kick](enemy), style="green")

            if not enemy.alife:
                self.xp += enemy.exp_reward
                show("u win")
                break
            enemy.attack(self)
        else:
            show("u lose")
            quit()

    def to_dict(self):
        return {
            "__class__": self.__class__.__name__.lower(),
            "name": self.name,
            "_health": self._health,
            "_full_health": self._full_health,
            "power": self.power,
            "alife": self._alife,
            "_xp": self._xp,
            "level": self.level,
            "_change_lvl_exp": self._change_lvl_exp,
        }

    @classmethod
    def from_dict(cls, data):
        hero = cls(name=data.get("name"))
        hero._health = data.get("_health")
        hero.power = data.get("power")
        hero._full_health = data.get("_full_health")
        hero._alife = data.get("_alife")
        hero._xp = data.get("_xp")
        hero.level = data.get("level")
        hero._change_lvl_exp = data.get("_change_lvl_exp")
        return hero


class Warrior(Hero):
    def __init__(self, name):
        super().__init__(name, 100, 15)
        self._stamina = 135
        self._full_stamina = 135

    def ultimate(self, target):
        how_many = 30
        if self._stamina > how_many:
            target.health -= 25
            self._stamina -= how_many
            return "\nFOR HONOR AND COURAGE\n"
        else:
            return "Not enough stamina"

    def perform_attack(self, attack: str, target: Character):
        attacks = {
            "attack": self.attack,
            "ultimate": self.ultimate,
        }
        return attacks[attack](target)

    def lvl_up(self):
        super().lvl_up()
        self._full_stamina += self._full_stamina // 10
        self._stamina = self._full_stamina

    def __str__(self):
        return super().__str__() + f"Stamina: {self._stamina}\n"

    def __iter__(self):
        yield from super().__iter__()
        yield f"Stamina: {self._stamina}\n"

    def to_dict(self):
        hero_dict = super().to_dict()
        hero_dict["_stamina"] = self._stamina
        hero_dict["_full_stamina"] = self._full_stamina
        return hero_dict

    @classmethod
    def from_dict(cls, data):
        hero = super().from_dict(data)
        hero._stamina = data.get("_stamina")
        hero._full_stamina = data.get("_full_stamina")
        return hero


class Samurai(Hero):
    def __init__(self, name):
        super().__init__(name, 100, 17)
        self._stamina = 150
        self._full_stamina = 150

    def ultimate(self, target):
        how_many = 50
        if self._stamina > how_many:
            target.health -= 40
            self._stamina -= how_many
            return "\nこんにちは\n"
        else:
            return "Not enough stamina"

    def perform_attack(self, attack: str, target: Character):
        attacks = {
            "attack": self.attack,
            "ultimate": self.ultimate,
        }
        return attacks[attack](target)

    def to_dict(self):
        hero_dict = super().to_dict()
        hero_dict["_stamina"] = self._stamina
        hero_dict["_full_stamina"] = self._full_stamina
        return hero_dict

    @classmethod
    def from_dict(cls, data):
        hero = super().from_dict(data)
        hero._stamina = data.get("_stamina")
        hero._full_stamina = data.get("_full_stamina")
        return hero

    def __str__(self):
        return super().__str__() + f"Stamina: {self._stamina}\n"

    def __iter__(self):
        yield from super().__iter__()
        yield f"Stamina: {self._stamina}\n"


class Mage(Hero):
    def __init__(self, name):
        super().__init__(name, 100, 10)
        self._mana = 120
        self._full_mana = 120

    def ultimate(self, target):
        how_many = 30
        if self._mana > how_many:
            target.health -= 40
            self._mana -= how_many
            return "\nFIREBALL!!!\n"
        else:
            return "Not enough mana"

    def lvl_up(self):
        super().lvl_up()
        self._full_mana += self._full_mana // 8
        self._mana = self._full_mana

    def perform_attack(self, attack: str, target: Character):
        attacks = {
            "attack": self.attack,
            "ultimate": self.ultimate,
        }
        return attacks[attack](target)

    def __str__(self):
        return super().__str__() + f"Mana: {self._mana}\n"

    def __iter__(self):
        yield from super().__iter__()
        yield f"Mana: {self._mana}\n"

    def to_dict(self):
        hero_dict = super().to_dict()
        hero_dict["_mana"] = self._mana
        hero_dict["_full_mana"] = self._full_mana
        return hero_dict

    @classmethod
    def from_dict(cls, data):
        hero = super().from_dict(data)
        hero._mana = data.get("_mana")
        hero._full_mana = data.get("_full_mana")
        return hero


hero_list = {
    "mage": Mage,
    "samurai": Samurai,
    "warrior": Warrior,
}
