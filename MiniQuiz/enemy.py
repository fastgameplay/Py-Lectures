from character import Character

class Enemy(Character):
    def __init__(self, name, health, attack_power, gold_reward):
        super().__init__(name, health, attack_power)
        self._gold_reward = gold_reward

    @property
    def gold_reward(self):
        return self._gold_reward

    def defeated(self):
        print(f"{self.name} is defeated!")
        return self.gold_reward

    def __str__(self):
        return f"Enemy: {super().__str__()}, Gold Reward: {self.gold_reward}"