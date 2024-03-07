import random


class PowerStat:
    def __init__(self, name: str, base: str) -> None:
        self.name: str = name
        self.base: int = int(base) if base != "null" else 0
        self.actual_stamina: int = self.calculate_actual_stamina()
        self.stat_value: float = 0

    @staticmethod
    def calculate_actual_stamina() -> int:
        return random.randint(0, 10)

    def update_stat_value(self, fb: float) -> None:
        self.stat_value = ((2 * self.base + self.actual_stamina) / 1.1) * fb
