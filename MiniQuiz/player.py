from character import Character;

class Player(Character):
    def __init__(self, name, health, attack_power, gold):
        super().__init__(name, health, attack_power)
        self._gold = gold

    @property
    def gold(self):
        return self._gold

    def collect_gold(self, amount):
        self._gold += amount
        print(f"{self.name} has collected {amount} gold!")

    def __str__(self):
        return f"{super().__str__()}, Gold: {self.gold}"