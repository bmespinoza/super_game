import random
from service import get_characters_info
from team import Team
from typing import Optional
from character import Character
from fight_manager import FightManager


class Game:
    def __init__(self, team_size: int = 5) -> None:
        self.team_size = team_size
        self.first_team: Optional[Team] = None
        self.second_team: Optional[Team] = None
        self.fight_manager = FightManager()
        self.summary = ""

    def prepare_game(self, first_team_name: str, second_team_name: str) -> None:
        print("preparing game...")
        self.create_teams(first_team_name, second_team_name)
        characters_info = get_characters_info(2 * self.team_size)
        for character_info in characters_info:
            character = self.create_character(character_info)
            self.add_character_to_team(character)
        self.first_team.get_team_alignment()
        self.second_team.get_team_alignment()
        self.summary += self.first_team.show_team()
        self.summary += self.second_team.show_team()
        print("ready to start")

    def create_teams(self, first_team_name: str, second_team_name: str) -> None:
        self.first_team = Team(first_team_name, self.team_size)
        self.second_team = Team(second_team_name, self.team_size)

    def create_character(self, character: dict) -> Character:
        return Character(
            character["id"],
            character["name"],
            character["alignment"],
            character["powerstats"],
        )

    def add_character_to_team(self, character: Character) -> None:
        if len(self.first_team.members) < self.team_size:
            self.first_team.add_member(character)
        else:
            self.second_team.add_member(character)

    def start_game(self) -> None:
        print("starting game")
        while self.last_team_standing():
            print("start round")
            first_team_character_fighting = self.get_character_to_fight(self.first_team)
            second_team_character_fighting = self.get_character_to_fight(
                self.second_team
            )
            self.fight_manager.start_characters_fight(
                first_team_character_fighting, second_team_character_fighting
            )
            if first_team_character_fighting in self.first_team.members:
                self.first_team.reduce_alive_members()
            else:
                self.second_team.reduce_alive_members()
            self.summary += self.fight_manager.fight_summary
        self.declare_winner()

    def get_character_to_fight(self, team: Team) -> Character:
        return random.choice(team.get_alive_members())

    def last_team_standing(self) -> bool:
        if self.first_team.alive_members > 0 and self.second_team.alive_members > 0:
            return True
        return False

    def declare_winner(self):
        if len(self.first_team.get_alive_members()) > 0:
            print(f"{self.first_team.name} wins")
            self.summary += f"<b>¡¡¡ {self.first_team.name} wins !!!</b>"
            return self.first_team
        print(f"{self.second_team.name} wins")
        self.summary += f"<b>¡¡¡ {self.second_team.name} wins !!!</b>"
        return self.second_team
