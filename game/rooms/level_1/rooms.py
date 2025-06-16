from game.rooms.level_1.modnster_list import monsters_dict
from game.classes.room import Room
from game.rooms.level_1.persons import npcs_dict


start_room = Room(
    "start_room",
    None,
    description="Ты просыпаешься в полутёмной каменной комнате. "
    "Перед тобой две арки — налево и направо. "
    "На стенах — следы других путников. Пора выбрать путь.",
)

room1 = Room(
    "room1",
    monsters_dict["monster_1"],
    description="Ты проходишь в прохладное помещение. "
    "Ржавые цепи покачиваются на стенах, воздух напряжён. "
    "Три прохода ведут вперёд, налево и направо. Что-то здесь определённо не так.",
)

room2 = Room(
    "room2",
    monsters_dict["monster_2"],
    description="Комната будто застыла после боя. На полу — разбитое оружие, следы борьбы."
    " Два выхода ведут в неизвестность. Осторожность — твой лучший друг.",
)

room3 = Room(
    "room3",
    monsters_dict["monster_3"],
    description="Посреди комнаты стоит камень с вырезанным вопросом: "
    "'Что ты готов отдать, чтобы выбраться?' Тишина здесь — слишком плотная, чтобы быть нормальной.",
)

room4 = Room(
    "room4",
    monsters_dict["monster_4"],
    description="Ты входишь в зал, усыпанный старыми свитками и книгами. "
    "Запах пыли и воска наполняет воздух. Кто-то здесь что-то искал, но не нашёл.",
)

room5 = Room(
    "room5",
    npcs_dict["skrivn"],
    description="В углу комнаты сидит фигура в капюшоне. Скривн ждёт тебя."
    " Его глаза не мигают, и кажется, он знал, что ты придёшь.",
)

room6 = Room(
    "room6",
    monsters_dict["boss_2"],
    description="Комната напоминает старую мастерскую. "
    "Всё в пыли, но на столе свежие следы."
    " Из темноты вырывается враг, охраняющий этот забытый угол.",
)

room7 = Room(
    "room7",
    monsters_dict["monster_5"],
    description="Комната жаркая, стены будто дышат жаром. "
    "Тени здесь двигаются сами по себе. "
    "Впереди — ещё один проход, но каждый шаг отзывается страхом.",
)

room8 = Room(
    "room8",
    monsters_dict["monster_6"],
    description="Туман застилает взгляд. Ты ничего не видишь дальше вытянутой руки. "
    "Звуки глушатся, как будто ты под водой. Комната закрыта… пока что.",
    blocked=True,
)

room9 = Room(
    "room9",
    npcs_dict["sister_elvari"],
    description="Лёд покрывает стены и пол. Сестра Эльвари стоит посреди зала, будто живая статуя. "
    "Её взгляд пронизывает, словно знает твои страхи.",
)

roomA = Room(
    "roomA",
    monsters_dict["boss_1"],
    description="Ты попадаешь в зал, который пульсирует светом и страхом. "
    "Пространство здесь неустойчиво. Главный противник уже ждёт тебя — и у него нет намерений пощадить.",
)

roomB = Room(
    "roomB",
    None,
    description="Символы на полу вспыхивают при каждом шаге. Это место как будто вне времени."
    " Все дороги вели сюда. Дверь за тобой захлопнулась.",
    blocked=True,
)


start_room.add_rooms(room1, room2)
room1.add_rooms(start_room, room6, room7)
room2.add_rooms(start_room, room3, room4)
room3.add_rooms(room2, room9)
room4.add_rooms(room2, room5)
room5.add_rooms(room4)
room6.add_rooms(room1)
room7.add_rooms(room1, room8, roomA)
room8.add_rooms(room7)
room9.add_rooms(room3)
roomA.add_rooms(room7, roomB)
roomB.add_rooms(roomA)
npcs_dict["sister_elvari"].room = roomB
npcs_dict["skrivn"].room = room8

rooms_lvl_1 = {
    "start_room": start_room,
    "room1": room1,
    "room2": room2,
    "room3": room3,
    "room4": room4,
    "room5": room5,
    "room6": room6,
    "room7": room7,
    "room8": room8,
    "room9": room9,
    "roomA": roomA,
    "roomB": roomB,
}
