"""
Main module of lab4 task 6
"""

import game2

# ==============================================================
# Creating transport and objects
tank = game2.Transport("Tank")
tank.set_description(
    "Effective against tanks bud needs a TRO fighter to operate. \
It can be reused as a weapon.")
javelin = game2.Weapon("Javelin")
javelin.set_description(
    "FGM-148 is effective against tanks. It destroys it completely.")
bandera_smuzi = game2.Weapon("Bandera-smuzi")
bandera_smuzi.set_description("Effective against everything")
bandera_portrait = game2.Weapon("Bandera Portrait")
bandera_portrait.set_description("Everyone, except bosses is afraid of him")
gun = game2.Weapon("GUN")
gun.set_description("(Glory to UkraiNe) - Super powerful ukrainian weapon")
medicine = game2.Medicine("Medicine")
medicine.set_description("Just a normal medicine. Can save your life")
# ==============================================================
# Creating Enemies
general_message = {
    "GUN": "Oh no! You've got a GUN!",
    "Javelin": "Aaaaa! I don't have any gun don!",
    "Bandera Portrait": "Oh no! Bandera is here!!! *Dies of heart attack*",
    "Tank": "F#$k don! That's my tank don!",
    "Bandera-smuzi": "*Swears a lot in russian* \
also transforms into a live version of the Burning Man festival ending)"
}

putik = game2.Enemy(
    "Putin", "An old dwarf with marasmus.")
putik.set_conversation(
    "Kill Ukrainians! Destroy Ukraine!\nEveryone must die!\nRussia go! USSR forever!")
putik.set_weakness(["Javelin", 'GUN', 'Tank', 'Bandera-smuzi'])
putik.set_action('bited you in a leg')
putik.set_lives(3)
putik.set_death({
    "GUN": "Oh no! You've got a GUN! Someone, pomogite!",
    "Javelin": "Aaaaa! Don't do thi....!",
    "Bandera Portrait": "I'm not that silly!",
    "Tank": "That's my last tank! You can't do this!",
    "Bandera-smuzi": "Aaaa! I'm on fire! Pomogite!"
})
kadon = game2.Enemy(
    "Kadyrov", "A TikTok and Telegram warrior (basically just a coward).")
kadon.set_conversation("Who are you don? Are you a new actor don?")
kadon.set_weakness(["Javelin", 'GUN', 'Tank', 'Bandera-smuzi'])
kadon.set_action('shot you! Also made a tiktok video')
kadon.set_lives(2)
kadon.set_death({
    "GUN": "Oh no don! You've got a GUN don!",
    "Javelin": "Aaaaa don! TikTok friends don, help me don! I don't have any gun don!",
    "Tank": "F#$k don! That's my tank don!",
    "Bandera-smuzi": "Aaaa don! I'm on fire don!"
})
katsap_soldier = game2.Enemy(
    "Katsap soldier",
    "Just a nobrainer fighter. Obsessed with vodka and putin.")
katsap_soldier.set_conversation(
    "Kill Ukrainians! Glory to putin! Matuska raseia lutshya!")
katsap_soldier.set_weakness(['GUN', 'Bandera Portrait', 'Bandera-smuzi'])
katsap_soldier.set_action('Stabbed you with shattered glass from vodka bottle')
katsap_soldier.set_lives(1)
katsap_soldier.set_death(general_message)

katsap = game2.Enemy(
    "Katsap", "Another 'Vatnuk'. Obsessed with vodka and putin.")
katsap.set_conversation(
    "Slava putinu! Za raseiu!")
katsap.set_weakness(["Javelin", 'GUN', 'Bandera Portrait',
                     'Pigeon', 'Tank', 'Bandera-smuzi'])
katsap.set_action('bited you in a leg')
katsap.set_lives(1)
katsap.set_death(general_message)

katsap_propaganda = game2.Enemy(
    "Katsap", "Another 'Vatnuk'. Obsessed with vodka and putin.")
katsap_propaganda.set_conversation(
    "SVoih ne brosayem! putin molodets!")
katsap_propaganda.set_weakness(["Javelin", 'GUN', 'Bandera Portrait',
                                'Tank', 'Bandera-smuzi'])
katsap_propaganda.set_action('turned on russia anthem')
katsap_propaganda.set_lives(1)
katsap_propaganda.set_death(general_message)
kadyk = game2.Enemy(
    "Kadyrovets", "Blodthirsty a$$h0le. Obsessed with kadyrov and money.")
kadyk.set_conversation(
    "Are you a new security guy don?")
kadyk.set_weakness(["Javelin", 'Bandera Portrait',
                   'Tank', 'Bandera-smuzi'])
kadyk.set_action('shot a TikTok video and "accidentally" shot you')
kadyk.set_lives(1)
kadyk.set_death(general_message)
# ==============================================================
# Creating Friend
tro = game2.Friend(
    "TRO fighter",
    "Cool guy. Knows how to shoot well as well as driving a tank and tracktor")
tro.set_conversation(
    "Slava Ukraini! Thank you for help!")
# ==============================================================
# Adding operator to the transport
tank.needs_operator(tro)
# ==============================================================
# Creating rooms
c0 = game2.Room("Central hall")
c0.set_description("A large Hall with lots of russian symbolics and four doors")

n0 = game2.Room("Soviet union shrine")
n0.set_description(
    "Real lenin is here. Also it's a place where putin \
likes to spend his time with russian priests trying to recussicate \
ussr's leaders and ussr itself")
n0.set_character(putik)
n1 = game2.Room("Kadyrov's hideout")
n1.set_description(
    "Giant room with lots of gold and even bigger greenscreen \
where kadyrov himself can shoot his videos")
n1.set_character(kadon)
n2 = game2.Room("Security room")
n2.set_description(
    "A room filled with monitors and servers, kadyrovets sits here and defences his bosses")
n2.set_character(kadyk)
n3 = game2.Room("Security room")
n3.set_description("A room where chmonias brother protects putin")
n3.set_character(katsap_soldier)
s0 = game2.Room("Putin's vault")
s0.set_description(
    "A room with the largest table anyone has ever seen, little katsapian \
church and golden toilet\nThere are some potatoes, so Lukashenko must have been here...")
s0.set_character(katsap_propaganda)
s1 = game2.Room("Armory - Tanks storage")
s1.set_description(
    "Huge hanger where tanks are stored. Currently only one is there. \
Other were destroyed by our army")
s1.set_item(tank)
s2 = game2.Room("Stolen ukrainian vehicles")
s2.set_description(
    "Enormous, dirty garage-like room. All vehicles were sold by \
corrupted russian authorities")
s2.set_character(katsap_soldier)
s3 = game2.Room("Security room")
s3.set_description("A room filled with vodka bottles and anasha")
s3.set_character(katsap)
e0 = game2.Room("Jail")
e0.set_description("A very cold room where our people are kept")
e0.set_character(tro)
e1 = game2.Room("Funreal room")
e1.set_description(
    "A room with coffin and dosen of candles. Dead Jyrinovskii lays here")
e2 = game2.Room("Maroder's room")
e2.set_description("A room packed with washing machines and other stolen items")
e2.set_character(kadyk)
e2.set_item(medicine)
e2.set_item(javelin)
e3 = game2.Room("Security room")
e3.set_description("One of many security rooms made for protecting putin")
e3.set_character(katsap)
e3.set_item(gun)

w0 = game2.Room("Storage of anti-dictator items")
w0.set_description(
    "A room with numerous flags of Ukraine and many other 'illegal' things")
w0.set_item(bandera_portrait)
# previously Chornobyl-dislocated katcap here, glows, harmless
w1 = game2.Room("Security room")
w1.set_description(
    "A small room with something that glows sitting in the corner")
w1.set_character(katsap_soldier)
w1.set_item(medicine)
w2 = game2.Room("Dyversant office")
w2.set_description("A vast room with many screens and dyversy plans")
w2.set_character(kadyk)
w2.set_item(bandera_smuzi)
w3 = game2.Room("Propaganda office")
w3.set_description(
    "A giant room with dosens of computers where propagandists are doing their dirty things")
w3.set_character(katsap_propaganda)
# ==============================================================
# Linking rooms
n0.link_room(n1, "west")
n1.link_room(n0, "east")
n1.link_room(n2, "west")
n2.link_room(n1, "east")
n2.link_room(n3, "south")
n3.link_room(n2, "north")
n3.link_room(c0, "south")

c0.link_room(n3, "north")
c0.link_room(w3, "west")
c0.link_room(e3, "east")
c0.link_room(s3, "south")

w3.link_room(c0, 'east')
w3.link_room(w2, 'west')
w2.link_room(w3, 'east')
w2.link_room(w1, 'north')
w1.link_room(w2, 'south')
w1.link_room(w0, 'north')
w0.link_room(w1, 'south')

s3.link_room(c0, 'north')
s3.link_room(s2, 'south')
s2.link_room(s3, 'north')
s2.link_room(s1, 'west')
s1.link_room(s2, 'east')
s1.link_room(s0, 'west')
s0.link_room(s1, 'east')

e3.link_room(c0, 'west')
e3.link_room(e2, 'east')
e2.link_room(e3, 'west')
e2.link_room(e1, 'south')
e1.link_room(e2, 'north')
e1.link_room(e0, 'south')
e0.link_room(e1, 'north')


current_room = c0
backpack = {}

dead = False


def fight_result_fun(fight_result):
    dead = False
    if fight_result == True:
        print(
            f"Hooray, you destroyed {inhabitant.label}!")
        if inhabitant.label == 'Putin':
            print("You've killed enemy leader! You are now a legend and a hero!")
        if inhabitant.get_defeated() == 13:
            print("Congratulations, you have vanquished the katsap horde!")
            dead = True
        current_room.character = None
    elif fight_result == False:
        if game2.main_character.lives != 0:
            print("Oh dear, you were attacked.")
            print("Be careful next time and use medicine")
    else:
        print(
            f'{inhabitant.label} has {fight_result} lives left')
    return dead


while dead == False:
    if game2.main_character.lives != 0:
        print("\n")
        current_room.get_details()

        inhabitant = current_room.get_character()
        if inhabitant is not None:
            inhabitant.describe()
        if isinstance(inhabitant, game2.Friend):
            game2.main_character.friends.append(inhabitant.label)
        item = current_room.get_item()
        if item is not None:
            item.describe()

        command = input("> ")

        if command in ["north", "south", "east", "west"]:
            current_room = current_room.move(command)
        elif command == "talk":
            if inhabitant is not None:
                inhabitant.talk()
        elif command == "fight":
            if inhabitant is not None:
                if isinstance(
                        inhabitant, game2.Enemy):
                    print("What will you fight with?")
                    fight_with = input()
                    if inhabitant.label == 'Putin' and (
                            fight_with.upper() == 'SLAVA UKRAINI' or fight_with.
                            upper() == 'GLORY TO UKRAINE'):
                        fight_result_fun(True)
                        print(
                            "Congratulations, you have killed Putin!")
                    elif fight_with in backpack.keys():
                        if tro.label in game2.main_character.friends and fight_with == 'Tank':
                            fight_result = backpack[fight_with].operate(tro)
                            print('Tanks are awesome!')
                            dead = fight_result_fun(fight_result)
                        elif isinstance(backpack[fight_with], game2.Weapon):
                            fight_result = inhabitant.fight(fight_with)
                            dead = fight_result_fun(fight_result)
                        else:
                            print(f"You can't use {fight_with} as a weapon")
                    else:
                        print(f"You don't have a {fight_with}")
                else:
                    print(
                        f"You can't fight with {inhabitant.label}, he is friend")
            else:
                print("There is no one here to fight with")
        elif command == "take":
            if item is not None:
                print("You put the " + item.get_name() + " in your backpack")
                backpack[item.get_name()] = item
                current_room.set_item(None)
            else:
                print("There's nothing here to take!")
        elif command == "heal":
            print("What will you heal yourself with?")
            med_item = input()
            if med_item in backpack.keys() and isinstance(
                    backpack[med_item],
                    game2.Medicine):
                backpack[med_item].heal()
                backpack.pop(med_item)
                print(f'You just healed yourself with the {med_item}')
            else:
                print(f'You can\'t heal yorself with the {med_item}')
        elif command == "backpack":
            if len(backpack) != 0:
                print(', '.join(backpack))
            else:
                print('You don\'t have any items')
        elif command == "friends":
            if len(game2.main_character.friends) != 0:
                print(', '.join(game2.main_character.friends))
            else:
                print('You don\'t have any friends yet!')
        elif command == "help":
            print('You can use:\n\
                "north", "south", "east", "west" to navigate\n\n\
                "talk"\t    - talk with somebody in room\n\
                "fight"\t    - fight with somebody in room\n\
                "take"\t    - take item that is in room\n\
                "heal"\t    - you can heal yourself with some object\n\
                "backpack"  - view your items\n\
                "help"\t    - view this menu')
        else:
            print("I don't know how to " + command)
    else:
        print('You died!')
        dead = True
