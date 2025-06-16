from game.src.classes.monster import Monsters, BossMonster


monster_1 = Monsters("giant_rat", health=30, power=5, exp_reward=25)
monster_2 = Monsters("crypt_bat", health=20, power=7, exp_reward=22)
monster_3 = Monsters("decaying_skeleton", health=35, power=9, exp_reward=30)
monster_4 = Monsters("mad_spirit", health=28, power=10, exp_reward=32)
monster_5 = Monsters("cave_spider", health=32, power=8, exp_reward=28)
monster_6 = Monsters("oozing_slime", health=40, power=6, exp_reward=26)

boss_1 = BossMonster(
    name="ancient_guardian",
    health=90,
    power=15,
    exp_reward=60,
    ultimate_phrase="You shall not pass the seal!",
    ultimate_power=30,
)

boss_2 = BossMonster(
    name="rat_king",
    health=85,
    power=14,
    exp_reward=55,
    ultimate_phrase="My children will feast on your bones!",
    ultimate_power=28,
)


monsters_dict = {
    "monster_1": monster_1,
    "monster_2": monster_2,
    "monster_3": monster_3,
    "monster_4": monster_4,
    "monster_5": monster_5,
    "monster_6": monster_6,
    "boss_1": boss_1,
    "boss_2": boss_2,
}
