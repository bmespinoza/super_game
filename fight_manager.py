from character import Character
import random
from typing import Optional


class FightManager:
    def __init__(self) -> None:
        self.starter_attacker: Optional[Character] = None
        self.current_attacker: Optional[Character] = None
        self.current_target: Optional[Character] = None
        self.fight_summary: str = ""

    def start_characters_fight(
        self, character_one: Character, character_two: Character
    ) -> None:
        self.fight_summary = (
            f"<p>--- round: {character_one.name} vs {character_two.name} ---</p>"
        )
        self.starter_attacker = random.choice([character_one, character_two])
        self.current_attacker = self.starter_attacker
        self.current_target = (
            character_two if self.current_attacker == character_one else character_one
        )

        while character_one.hp > 0 and character_two.hp > 0:
            self.perform_fighter_attack(self.current_attacker, self.current_target)

        winner = self.declare_winner(character_one, character_two)
        self.fight_summary += f"<p>{winner.name} wins</p>"
        self.restore_stats(winner)

    def perform_fighter_attack(self, attacker: Character, target: Character) -> None:
        damage = attacker.select_attack()
        print(f"{attacker.name} attacked doing {damage} damage")
        print(f"{target.name} has {target.hp} hp")
        current_hp = target.hp - damage
        target.hp = current_hp
        print(f"{target.name} now has {target.hp} hp")
        self.current_attacker = target
        self.current_target = attacker

    def declare_winner(
        self, character_one: Character, character_two: Character
    ) -> Character:
        if character_one.hp > 0:
            return character_one
        return character_two

    def restore_stats(self, winner: Character) -> None:
        self.starter_attacker = None
        self.current_attacker = None
        self.current_target = None
        winner.hp = winner.get_initial_hp()
