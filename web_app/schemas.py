from pydantic import BaseModel


class AttackSchema(BaseModel):
    attack: str
