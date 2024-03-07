import random
from typing import Optional
from character import Character
from constants import AlignmentType


class Team:
    def __init__(self, name: str, team_size: int) -> None:
        self.members: list[Character] = []
        self.alignment: Optional[str] = None
        self.name: str = name
        self.alive_members: int = team_size

    def add_member(self, member: Character) -> None:
        self.members.append(member)

    def get_team_alignment(self) -> None:
        heroes = sum(
            1 for member in self.members if member.alignment == AlignmentType.GOOD
        )
        villains = sum(
            1 for member in self.members if member.alignment == AlignmentType.BAD
        )
        if heroes > villains:
            self.alignment = AlignmentType.GOOD
        elif villains > heroes:
            self.alignment = AlignmentType.BAD
        else:
            self.alignment = random.choice([AlignmentType.GOOD, AlignmentType.BAD])
        self.update_members_by_alignment()

    def update_members_by_alignment(self) -> None:
        for member in self.members:
            member.update_filiation_coefficient(self.alignment)
            member.update_powerstats()
            member.hp = member.get_initial_hp()

    def get_alive_members(self) -> list[Character]:
        return [member for member in self.members if member.hp > 0]

    def reduce_alive_members(self):
        self.alive_members -= 1

    def show_team(self) -> str:
        text = "Team members:"
        for member in self.members:
            text += f"<li>{member.name}</li>"
        text += "\n"
        return text
