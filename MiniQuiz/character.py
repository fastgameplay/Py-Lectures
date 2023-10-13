import random

class Character:
    def __init__(self, name, health, attack_power):
        self._name = name
        self.health = health
        self._attack_power = attack_power

    @property
    def name(self):
        return self._name


    @property
    def attack_power(self):
        return self._attack_power
    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value >= 0:
            self._health = value
        else:
            self._health = 0

    def attack(self, opponent):
        damage = random.randint(1, self.attack_power)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")

    def __str__(self):
        return f"{self.name} (Health: {self.health}, Attack Power: {self.attack_power})"
    
