from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

from game.classes.heroes import hero_list

from game.classes.monster import Monsters
from game.rooms.level_1.rooms import rooms_lvl_1
from web_app.schemas import AttackSchema
from web_app.utils import get_hero

app = FastAPI()
app.mount("/static", StaticFiles(directory="web_app/static"), name="static")
templates = Jinja2Templates(directory="web_app/templates")

app.add_middleware(SessionMiddleware, secret_key="your-secret-key")


@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/start", response_class=HTMLResponse)
async def start_game(
    request: Request, name: str = Form(...), char_class: str = Form(...)
):
    hero = hero_list[char_class](name)
    request.session["hero"] = hero.to_dict()
    return RedirectResponse(url=f"/first_level", status_code=303)


@app.get("/first_level")
async def first_level(request: Request):
    hero = get_hero(request)
    start_room = rooms_lvl_1["start_room"]
    return templates.TemplateResponse(
        request=request,
        name="level1.html",
        context={
            "hero": hero,
            "rooms": {
                "room_name": start_room.name,
                "description": start_room.description,
                "next_rooms": list(start_room.next_rooms),
            },
        },
    )


@app.get("/change_room")
def change_room(request: Request, this_room: str, next_room: str = ""):
    this_room = rooms_lvl_1[this_room]
    next_room_to_go, *blocked = this_room.change_room(next_room)
    blocked = f"{next_room} is blocked" if blocked else None
    if (
        isinstance(next_room_to_go.creature, Monsters)
        and next_room_to_go.creature.alife
    ):
        return RedirectResponse(url=f"/fight?room={next_room_to_go.name}")

    return templates.TemplateResponse(
        request=request,
        name="move_rooms.html",
        context={
            "rooms": {
                "room_name": next_room_to_go.name,
                "description": next_room_to_go.description,
                "next_rooms": list(next_room_to_go.next_rooms),
                "blocked": blocked,
            }
        },
    )


@app.get("/fight")
def get_fight(request: Request, room: str):
    hero = get_hero(request)
    this_room = rooms_lvl_1[room]
    monster = this_room.creature
    return templates.TemplateResponse(
        request=request,
        name="fight.html",
        context={
            "hero": hero,
            "monster": monster,
            "room": room,
        },
    )


@app.post("/fight")
def fight(request: Request, room: str, attack: AttackSchema):
    hero = get_hero(request)
    this_room = rooms_lvl_1[room]
    monster = this_room.creature
    hero.perform_attack(attack.attack, monster)
    if monster.alife:
        monster.attack(hero)
        request.session["hero"] = hero.to_dict()
    else:
        return RedirectResponse(url=f"/change_room?this_room={room}", status_code=303)

    return templates.TemplateResponse(
        request=request,
        name="fight.html",
        context={
            "hero": hero,
            "monster": monster,
            "room": room,
        },
    )
