"""
Lab 4 task 5
game.py
"""


class MainCharacter():
    """
    Main character class
    """

    def __init__(self) -> None:
        self.defeated = 0


main_character = MainCharacter()


class Room:
    """
    Room class
    """

    def __init__(self, label: str) -> None:
        """
        Init
        """
        self.label = label
        self.character = None
        self.item = None
        self.north = None
        self.south = None
        self.east = None
        self.west = None

    def set_description(self, description) -> None:
        """
        Sets description
        """
        self.description = description

    def link_room(self, other: object, direction: str) -> None:
        """
        Connects different rooms
        """
        # Unfortunately, here is no switch/case in Python
        dirs = ["north", "south", "east", "west"]
        if direction == dirs[0]:
            self.north = other
        elif direction == dirs[1]:
            self.south = other
        elif direction == dirs[2]:
            self.east = other
        else:
            self.west = other

    def set_character(self, other: object) -> None:
        """
        Adds a character to a room
        """
        self.character = other

    def get_details(self) -> None:
        """
        Prints details about room
        """
        print(self.label)
        print('--------------------')
        print(self.description)
        rooms = [self.west, self.east, self.south, self.north]
        dirs = ['west', 'east', 'south', 'north']
        for room in zip(rooms, dirs):
            if room[0] != None:
                print(f'The {room[0].label} is {room[1]}')

    def get_character(self) -> object:
        """
        Returns character that is in current room
        """
        return self.character

    def get_item(self) -> object:
        """
        Returns an item that is in the room
        """
        return self.item

    def move(self, direction: str) -> object:
        """
        Changes the room
        Basically returns linked room
        """
        dirs = ["north", "south", "east", "west"]
        if direction == dirs[0] and self.north != None:
            return self.north
        elif direction == dirs[1] and self.south != None:
            return self.south
        elif direction == dirs[2] and self.east != None:
            return self.east
        elif direction == dirs[3] and self.west != None:
            return self.west
        else:
            print('You can\'t go through the walls ;)\nAt least yet')
        return self

    def set_item(self, item: object) -> None:
        """
        Adds an item to a room
        """
        self.item = item


class Character:
    """
    Parental class for Friends and Enemies
    """

    def __init__(self, label: str, description: str) -> None:
        """
        Init
        """
        self.label = label
        self.description = description

    def set_conversation(self, words: str) -> None:
        """
        Adds some words for the character to say
        """
        self.words = words

    def set_weakness(self, weakness: str) -> None:
        """
        Adds some weakness
        """
        self.weakness = weakness

    def describe(self) -> None:
        """
        Prints character's description
        """
        print(f'{self.label} is here!\n{self.description}')

    def talk(self) -> None:
        """
        Prints character's words
        """
        print(f'[{self.label} says]: {self.words}')

    def set_defeated(self, num: int = 1) -> None:
        """
        Sets the number of defeated enemies
        """
        main_character.defeated = num

    def get_defeated(self) -> None:
        """
        Gets the number of defeated enemies
        """
        return main_character.defeated


class Enemy(Character):
    """
    Enemy class
    """

    def __init__(self, label: str, description: str) -> None:
        """
        Init
        """
        super().__init__(label, description)
        # self.defeated = 0

    def set_conversation(self, words: str) -> None:
        """
        Described in parental class
        """
        super().set_conversation(words)

    def set_weakness(self, weakness: str) -> None:
        """
        Described in parental class
        """
        super().set_weakness(weakness)

    def describe(self) -> None:
        """
        Described in parental class
        """
        super().describe()

    def talk(self) -> None:
        """
        Described in parental class
        """
        super().talk()

    def set_defeated(self, num: int) -> None:
        """
        Described in parental class
        """
        super().set_defeated(num)

    def get_defeated(self) -> int:
        """
        Described in parental class
        """
        return super().get_defeated()

    def fight(self, fight_with: str) -> bool:
        """
        Checks if an enemy can be defeated by certain item
        """
        if self.weakness == fight_with:
            defeated_enem = self.get_defeated()
            self.set_defeated(defeated_enem+1)
            print(f'You fend {self.label} off with the {fight_with}')
            return True
        print(f'{self.label} crushes you, puny adventurer!')
        return False


class Friend(Character):  # Not used
    """
    Friend class
    """

    def __init__(self, label: str, description: str) -> None:
        """
        Init
        """
        super().__init__(label, description)

    def set_conversation(self, words: str) -> None:
        """
        Described in parental class
        """
        super().set_conversation(words)

    def describe(self) -> None:
        """
        Described in parental class
        """
        super().describe()

    def talk(self) -> None:
        """
        Described in parental class
        """
        super().talk()


class Item:
    """
    Item class
    """

    def __init__(self, label: str) -> None:
        """
        Init
        """
        self.label = label

    def set_description(self, description: str) -> None:
        """
        Sets description
        """
        self.description = description

    def describe(self) -> None:
        """
        Prints item's description
        """
        print(f'The [{self.label}] is here - {self.description}')

    def get_name(self) -> str:
        """
        Returns item's label
        """
        return self.label
