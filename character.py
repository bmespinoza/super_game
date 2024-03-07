import random

from powerstat import PowerStat


class Character:
    def __init__(
        self, id: str, name: str, alignment: str, powerstats: dict[str, str]
    ) -> None:
        self.id = id
        self.name = name
        self.alignment = alignment
        self.powerstats: dict[str, PowerStat] = {
            str(powerstat_name): PowerStat(powerstat_name, powerstat_base_value)
            for powerstat_name, powerstat_base_value in powerstats.items()
        }
        self.actual_stamina = self.calculate_actual_stamina()
        self._hp = 0.0
        self.fb = 0.0

    @property
    def hp(self) -> float:
        if self._hp > 0:
            return self._hp
        return 0.0

    @hp.setter
    def hp(self, hp: float):
        self._hp = hp

    @staticmethod
    def calculate_actual_stamina() -> int:
        return random.randint(0, 10)

    def get_initial_hp(self) -> float:
        stats_formula = (
            self.powerstats["strength"].stat_value * 0.8
            + self.powerstats["durability"].stat_value * 0.7
            + self.powerstats["power"].stat_value
        ) / 2
        actual_stamina_formula = 1 + self.actual_stamina / 10
        return stats_formula * actual_stamina_formula + 100

    def update_filiation_coefficient(self, team_aligntment: str) -> None:
        base_formula = 1 + random.randint(0, 9)
        if team_aligntment == self.alignment:
            self.fb = base_formula
        else:
            self.fb = 1 / base_formula

    def update_powerstats(self) -> None:
        for stat in self.powerstats.values():
            stat.update_stat_value(self.fb)

    def mental_attack(self) -> float:
        return (
            self.powerstats["intelligence"].stat_value * 0.7
            + self.powerstats["speed"].stat_value * 0.2
            + self.powerstats["combat"].stat_value * 0.1
        ) * self.fb

    def strong_attack(self) -> float:
        return (
            self.powerstats["strength"].stat_value * 0.6
            + self.powerstats["power"].stat_value * 0.2
            + self.powerstats["combat"].stat_value * 0.2
        ) * self.fb

    def fast_attack(self) -> float:
        return (
            self.powerstats["speed"].stat_value * 0.55
            + self.powerstats["durability"].stat_value * 0.25
            + self.powerstats["strength"].stat_value * 0.2
        ) * self.fb

    def select_attack(self) -> float:
        return random.choice(
            [self.mental_attack, self.strong_attack, self.fast_attack]
        )()
