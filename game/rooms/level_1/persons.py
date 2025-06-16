from game.classes.NPC import NPC
from game.rooms.level_1.modnster_list import monsters_dict

sister_elvari = NPC(
    name="Sister Elvari",
    quest="Defeat the Ancient Guardian to break the seal and open the path ahead.",
    monster=monsters_dict["boss_1"],
    xp=60,
    health=50,
    power=5,
)


skrivn = NPC(
    name="Skrivn",
    quest="Kill all the giant rats. They whisper at night, I can't sleep!",
    monster=monsters_dict["boss_2"],
    xp=15,
    health=40,
    power=3,
)

npcs_dict = {
    "sister_elvari": sister_elvari,
    "skrivn": skrivn,
}
