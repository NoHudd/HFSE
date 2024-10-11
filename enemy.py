# Description: This file contain the Enemy class and its attributes and methods. This class is used to create the enemy object in the game.

class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        damage = self.attack_power 
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!")

# Define specific enemy types
class GhostlyFigure(Enemy):
    def __init__(self):
        super().__init__("Ghostly Figure", 30, 5)

class HungryGhoul(Enemy):
    def __init__(self):
        super().__init__("Hungry Ghoul", 50, 8)

class Wraith(Enemy):
    def __init__(self):
        super().__init__("Wraith", 70, 10)

class GlitchEntity(Enemy):
    def __init__(self):
        super().__init__("Glitch Entity", 60, 12)

class RestlessSpirit(Enemy):
    def __init__(self):
        super().__init__("Restless Spirit", 40, 10)

class GuardianDaemon(Enemy):
    def __init__(self):
        super().__init__("Guardian Daemon", 100, 20)


