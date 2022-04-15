"""
Slightly updated game.py module
"""

from game import Item, Character, Enemy, Friend, Room, main_character

main_character.lives = 1
main_character.friends = []


class Weapon(Item):
    def __init__(self, label: str) -> None:
        super().__init__(label)


class Medicine(Item):
    def __init__(self, label: str) -> None:
        super().__init__(label)

    def heal(self):
        main_character.lives += 1


class Transport(Item):
    def __init__(self, label: str) -> None:
        super().__init__(label)

    def needs_operator(self, other):
        self.operator = other

    def operate(self, other):
        if self.operator == other:
            print(f'Thanks to {other.label}, you can use {self.label}')
            return True
        print(
            f'You can\'t use the {self.label}!\nYou need to find {self.operator} first!')
        return False


class Enemy(Character):
    def __init__(self, label: str, description: str) -> None:
        super().__init__(label, description)
        self.lives = 1
        phrases = {}

    def set_action(self, action):
        self.action = action

    def set_death(self, phrases: dict):
        self.phrases = phrases

    def set_lives(self, num: int):
        self.lives = num

    def fight(self, fight_with: str) -> bool:
        """
        Checks if an enemy can be defeated by certain item
        """
        if fight_with in self.weakness:
            defeated_enem = self.get_defeated()
            print(f'You fend {self.label} off with the {fight_with}')
            if fight_with in self.phrases.keys():
                print(f"[{self.label}]: {self.phrases[fight_with]}")
            self.lives -= 1
            if self.lives <= 0:
                self.set_defeated(defeated_enem+1)
                return True
            else:
                return self.lives
        print(
            f'{self.label} just {self.action}!\nYou have {main_character.lives-1} lives left')
        main_character.lives -= 1
        return False
