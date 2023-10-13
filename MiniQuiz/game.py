import random

class Game:
    def __init__(self, player):
        self._player = player
        self._enemies = []

    def add_enemy(self, enemy):
        self._enemies.append(enemy)

    def play(self):
        print(f"Welcome, {self._player.name}! \n")
        while self._enemies:
            enemy = random.choice(self._enemies)
            print(f"A wild {enemy.name} appears! \n")

            while self._player.health > 0 and enemy.health > 0:
                self._player.attack(enemy)
                if enemy.health <= 0:
                    gold_reward = enemy.defeated()
                    self._player.collect_gold(gold_reward)
                else:
                    enemy.attack(self._player)
                print(f"\n{self._player}")
                print(f"{enemy}\n")

            if self._player.health <= 0:
                print(f"{self._player.name} has been defeated!")
                print("Game over.")
                break

            self._enemies.remove(enemy)

        if not self._enemies:
            print(f"Congratulations, {self._player.name}! You have defeated all enemies and won the game with {self._player.gold} gold.")