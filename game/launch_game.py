from game.classes import Monsters
from game.utils import show, option
from game.classes.NPC import NPC
from game.classes.room import Room
from game.classes import Hero


def show_room_options(room: Room):
    return room.next_rooms.keys()


def npc_in_room():
    message = "what do you want?"
    choices = ["talk", "go out"]
    choice = option(message, choices)
    return choice


def handle_choice(hero: Hero, rooms: Room, choice: str) -> Room:
    if choice == "info":
        show(hero)
        return rooms

    room = rooms.change_room(choice)

    if isinstance(room.creature, Monsters):
        hero.fight(room.creature)
        room.creature = None
    elif isinstance(room.creature, NPC):
        choice = npc_in_room()
        if choice == "talk":
            room.creature.talk_npc(hero)
    else:
        show("The rooms is empty.")

    return room


def navigate_rooms(hero, rooms):

    while True:
        choice = show_room_options(rooms)
        rooms = handle_choice(hero, rooms, choice)
