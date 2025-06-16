import random

from game.src.classes.base import Character
from game.src.classes.heroes import Hero
from game.src.classes.room import Room
from game.src import utils
from enum import Enum


class QuestStatus(Enum):
    NOT_ACCEPTED = "Не принят"
    IN_PROGRESS = "В работе"
    COMPLETED = "Завершён"
    DECLINED = "Отказался"


class NPC(Character):
    def __init__(
        self,
        name: str,
        quest: str,
        monster: Character,
        xp: int,
        health: int,
        power: int,
        room: Room | None = None,
    ):
        super().__init__(name, health, power)
        self._quest = quest
        self.monster = monster
        self.xp = xp
        self.room = room
        self._status = QuestStatus.NOT_ACCEPTED

    @property
    def quest(self):
        return self._quest

    @property
    def status(self):
        if not self.monster.alife and self._status == QuestStatus.IN_PROGRESS:
            self._status = QuestStatus.COMPLETED
            self.room.unblocked() if self.room else None
        return self._status

    def get_quest(self, hero: Hero):
        utils.show(self.quest)

        message = "Will you did it?"
        choices = [
            "i did it" if self._status == QuestStatus.IN_PROGRESS else "i will did it",
            "No",
        ]
        choice = utils.option(message, choices)
        if choice == "i will did it":
            utils.show("I'll wait for you here")
            self._status = QuestStatus.IN_PROGRESS

        elif choice == "i did it":
            if self.status == QuestStatus.COMPLETED:
                hero.xp += self.xp
                utils.show("thank you")
            else:
                utils.show("Liar")
        else:
            utils.show("oh noo")

    def talk_npc(self, hero: Hero):
        status = self.status
        if status == QuestStatus.NOT_ACCEPTED:
            self.get_quest(hero)
        if status == QuestStatus.IN_PROGRESS:
            utils.show(
                f"{self.name}:"
                + random.choice(
                    [
                        "still wait you here",
                        "are you done?",
                        "i must be here",
                    ]
                )
            )
        if status == QuestStatus.COMPLETED:
            utils.show(random.choice(["thank you", "I can be calm"]))
