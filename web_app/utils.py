from fastapi import Request
from game.src.classes.heroes import hero_list, Hero


def get_hero(request: Request) -> Hero:
    hero_dict = request.session.get("hero")
    return hero_list[hero_dict.get("__class__")].from_dict(hero_dict)
