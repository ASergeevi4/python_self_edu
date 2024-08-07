class Character:            # Creating main class
    base_health_points: int
    base_attack_power: int
    base_defence: int
    character_name: str

    def __init__(self, *, level: int = 1) -> None:
        self.level = level
        self._init_attributes()

    def _init_attributes(self) -> None:
        self.health_points = self.base_health_points * self.level 
        self.attack_power = self.base_attack_power * self.level

    def __str__(self) -> str:
        return f"{self.character_name} (level: {self.level}, hp: {self.health_points}, power: {self.attack_power})"

    def attack(self, *, target: "Character") -> None:
        target.got_damage(damage=self.attack_power)

    def got_damage(self, *, damage: int) -> None:
        effective_damage = damage * (100 - self.defence) / 100
        effective_damage = round(effective_damage)
        self.health_points -= effective_damage
        return effective_damage

    def is_alive(self) -> bool:
        return self.health_points > 0

    @property
    def defence(self) -> int:
        return self.base_defence * self.level
    
    @property
    def max_health_points(self) -> int:
        return self.level * self.base_health_points
    
    def health_points_percent(self) -> float:
        return 100 * self.health_points / self.max_health_points

class Ork(Character):
    base_health_points = 100
    base_attack_power = 10
    character_name = "Ork"
    base_defence = 15

    @property
    def defence(self) -> int:
        defence = super().defence
        if self.health_points < 50:
            defence *= 3
        return defence

class Elf(Character):
    base_health_points = 50
    base_attack_power = 15
    character_name = "Elf"
    base_defence = 10

    def attack(self, *, target: Character) -> None:
        attack_power = self.attack_power
        if target.health_points_percent() < 30:
            attack_power *= 3
        target.got_damage(damage=attack_power)

def fight(*, character_1: Character, character_2: Character) -> None:
    round_counter = 1
    while character_1.is_alive() and character_2.is_alive():
        print(f"Round {round_counter}:")
        print(f"{character_1.character_name} attacks {character_2.character_name} with {character_1.attack_power} power.")
        character_1.attack(target=character_2)
        print(f"{character_2.character_name}'s HP is now {character_2.health_points}.")
        
        if character_2.is_alive():
            print(f"{character_2.character_name} attacks {character_1.character_name} with {character_2.attack_power} power.")
            character_2.attack(target=character_1)
            print(f"{character_1.character_name}'s HP is now {character_1.health_points}.")
        
        round_counter += 1
        print()

    print(f"Final result:")
    print(f"{character_1} is_alive: {character_1.is_alive()}")
    print(f"{character_2} is_alive: {character_2.is_alive()}")

ork = Ork(level=1)
elf = Elf(level=1)

fight(character_1=ork, character_2=elf)
