from game.classes.base import Character


class Room:
    def __init__(
        self,
        name: str,
        creature: Character | None,
        description: str | None = None,
        blocked: bool = False,
    ):
        self.name = name
        self.description = description
        self.creature = creature
        self.next_rooms: dict[str, Room] = {}
        self.blocked = blocked

    def add_rooms(self, *args: "Room"):
        self.next_rooms.update(
            {room.name: room for room in args if isinstance(room, Room)}
        )

    def change_room(self, choice: str) -> tuple:

        if choice not in self.next_rooms.keys():
            return (self,)

        if self.next_rooms[choice].blocked:
            return self, "blocked"

        return (self.next_rooms[choice],)

    def unblocked(self):
        self.blocked = False

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
