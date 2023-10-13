from enemy import Enemy;
from player import Player;
from game import Game;

player = Player(name="Goblin Slayer", health=30, attack_power=20, gold=0)
enemy_1 = Enemy(name="Goblin", health=30, attack_power=10, gold_reward=10)
enemy_2 = Enemy(name="Hob Goblin", health=30, attack_power=15, gold_reward=10)
momonga = Enemy(name="Ainz Ooal Gown", health=200, attack_power=150, gold_reward=1000)

game = Game(player)

game.add_enemy(enemy_1)
game.add_enemy(enemy_2)
game.add_enemy(momonga)

game.play()