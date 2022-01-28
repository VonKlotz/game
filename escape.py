import sys
import time
import random


name = input("whats your name =>")
if name == "":
    name = "Player"
# set the player name

points = 0
# create a points variable

def slowprint(s):
    for c in s + "\n" :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

def add_points():
    global points
    points += random.randint(20, 50)
    # add random number of points known as coins in the story

### quest under this line


def story_intro():
    print(" ▄████▄   ▄▄▄       ███▄    █    ▓██   ██▓ ▒█████   █    ██")
    print("▒██▀ ▀█  ▒████▄     ██ ▀█   █     ▒██  ██▒▒██▒  ██▒ ██  ▓██▒")
    print("▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒     ▒██ ██░▒██░  ██▒▓██  ▒██░")
    print("▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒     ░ ▐██▓░▒██   ██░▓▓█  ░██░")
    print("▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░     ░ ██▒▓░░ ████▓▒░▒▒█████▓ ")
    print("░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒       ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒")
    print("  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░    ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░")
    print("░          ░   ▒      ░   ░ ░     ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░")
    print("░ ░            ░  ░         ░     ░ ░         ░ ░     ░       ")
    print("░                                 ░ ░                          ")
    print("   ▓█████   ██████  ▄████▄   ▄▄▄       ██▓███  ▓█████")
    print("   ▓█   ▀ ▒██    ▒ ▒██▀ ▀█  ▒████▄    ▓██░  ██▒▓█   ▀")
    print("   ▒███   ░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██░ ██▓▒▒███ ")
    print("   ▒▓█  ▄   ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██▄█▓▒ ▒▒▓█  ▄  ")
    print("   ░▒████▒▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██▒ ░  ░░▒████▒")
    print("   ░░ ▒░ ░▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░▒▓▒░ ░  ░░░ ▒░ ░")
    print("    ░ ░  ░░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░▒ ░      ░ ░  ░")
    print("      ░   ░  ░  ░  ░          ░   ▒   ░░          ░   ")
    print("      ░  ░      ░  ░ ░            ░  ░            ░  ░")

    slowprint(f"welcome {name} to our game")
    slowprint("You wake up in a strange building, you dont really remember much. Other than being struck over the head with something. You shout hello?? But no one replies. all you can hear is an eerie echo of your own voice. You decide to try to find your way out of this strange building you have found yourself in. As you walk through the long narrow corridor you are faced with three directions. ")
    
    # story here
    intro()


def intro():
    global points
    points = 0

    slowprint("To go left press 1 To go straight press 2 To go right press 3")
    answer1 = input("whats your choice => ")
    
    if answer1 == "1":
        add_points()
        left_path()
        
    elif answer1 =="2":
        add_points()
        straight_path()
        
    elif answer1 == "3":
        add_points()
        right_path()
        
    else:
        wrong_choice_message()
        intro()

#left path


def left_path():
    slowprint("You have chosen to go left.As you turn left looking around, scared cold and hungry. The light above you is flickering, on and off. In the distance your not sure if you can see figures in the dark shaddows, or i your eyes are playing tricks on you. After what feels like a lifetime of walking down the damp and cold corridor you find a small box and open it.Inside are some small coins, you fumble around to try and get them into your pocket.")
    slowprint(f"You have {points} coins.")
    slowprint("You finally come to an opening seperating in to two directions which will you choose?")
    slowprint("To go left press 1 To go right press 3")
    answer1 = input("whats your choice => ")

    if answer1 == "1":
        add_points()
        left_path_choice_a()
    elif answer1 == "3":
        add_points()
        left_path_choice_b()
    else: 
        wrong_choice_message()
        left_path()

def left_path_choice_a():
    slowprint("You have chosen to go left. You slowly step trying to watch where your putting your feet, being careful not to trip over anything. Lights flickering , a cold breeze on the back of your neck , making your small hairs stand on end. You feel as though someone is watching you.. As you progress you see a small chest of drawers and decide to open it. Inside the small drawers you see some strange coins. You put them in your pocket and keep slowly moving forward. ")
    slowprint(f"You have {points} coins.")
    slowprint("You see two possible directions infront of you. Where will you choose to go next?")
    slowprint("To go left press 1 To go right press 3")
    answer1 = input("whats your choice => ")
    if answer1 == "1":
        left_path_choice_a_1()
    elif answer1 == "3":
        add_points()
        left_path_choice_a_2()
    else:
        wrong_choice_message()
        left_path_choice_a()

def left_path_choice_a_1():
    slowprint("You have chosen to go left. Your wondering, 'how did i get here?'. Theres a door, you decide to go inside and take a look. Inside the small cramped room , amongst the the old dust furnature you find a small chest, inside the small chest are some coins. You take the coins and continue cautiously on your way.")
    slowprint(f" you have {points} coins.")
    slowprint("Upon exiting the room you are faced with a door either side of you, one to your left and one to your right. which will you choose?")
    slowprint("To go left press 1 To go right press 3")
    answer1 = input("whats your choice => ")
    if answer1 == "1":
        slowprint("you have chosen to go left, everything goes dark, other than a small glint of moonlight shining in through the cracks between the bricks.. Theres a loud crash and a bang. You are faced with a tall dark shaddow. You cant make out who , or for that matter what it is. You try to fight off what ever or who ever it is. but theyre too strong. ")
        game_over()

    elif answer1 == "3":
        slowprint("Yes is this it, you continue right. As your walking you see the moonlight becoming brighter and brighter, the fresh night breeze getting stronger and stronger. Until you step foot outside. ")
        victory()

    else:
        wrong_choice_message()
        left_path_choice_a_1()
        
def left_path_choice_a_2():
    slowprint("You have chosen to go right. You feel asthough you have been lost forever. You tummys rumbling, goosbumps have taken hold of your entire body. As you stumble through the building, you see skeletons of what can only be descried as past people. trapped and forgotten forever. You begin to worry that you will never see daylight again.You look down and find a small piece of paper. Its hard to make out what is writtin on the paper. 'This is of no use!' You think to yourself tossing it to the ground hopelessly.")
    slowprint("Again you are faced with only two directions.. left or right? You think to yourself 'is this place a maze or something, all the corridors look the same.' with what little amount of light you have you hopelessly carry on.")
    slowprint("To go left press 1 To go right press 3")
    answer1 = input("whats your choice => ")

    if answer1 == "1":
        slowprint("As you turn left the creaky wooden flooring dosent feel too stable, you stumble and hear a cracking sound as the floor collapses and you fall you your death.")
        game_over()
        
    elif answer1 =="3":
        slowprint("Oh my can it be ? you have found your way out and escaped.")
        victory()

    else:
        wrong_choice_message()
        left_path_choice_a_2()

def left_path_choice_b():
    slowprint("You have chosen to go right. Dragging your feet slowly one foot after another, theres an open door. You cautiosly enter the room. 'Is anybody here' you call. But no reply. In the flickers of the old light you see the room is an old nursery. In the corner thie light is shining through a small crack onto an old cupboard with one door slightly ajar. You step over to the cupoard kneel down to take a look. Inside are some coins.")
    slowprint(f"You have {points} coins.")
    slowprint("You collect the coins and continue through the room over the creaky wooden floorboards. As you exit the room there are two sets of stairs. One to the left of you and one to the right. which will you choose?")
    slowprint("To go left press 1 To go right press 3")
    answer1 = input("whats your choice => ")

    if answer1 == "1":
        left_path_choice_b_1()
        
    elif answer1 =="3":
        left_path_choice_b_2()
    else:
        wrong_choice_message()
        left_path_choice_b()

def left_path_choice_b_1():
    slowprint("You have chosen to go left. You hear an owl from outside. Wondering to yourself. 'am i close? will this lead me out of this terrble place?' Crossing your fingers you move on.")
    slowprint("After sometime , you come to two doors, one on the left and one on the right. They both look so differnt. One is old and discoloured , with small holes in, and the other the paint has peeled off revealing deep scratches, and has an old broken padlock hanging from a rusty loop on the door. Which door will you choose?")
    slowprint("To choose left press 1 To choose right press 3")
    answer1 = input("whats your choice => ")
    if answer1 == "1":
        slowprint(f"{name} You hesitantly enter to room. 'BANG' the door slams shut behind you. You quickly turn around frantically trying to prize open the door. 'RAWR' you feel something tickle your neck , what feels like a short brittle hair. You slowly turn around to see what your faced with. As you turn , the moonlight shining through a small window reavels a huge lion. It seems someone dosent want me in here. You crawl around looking for anything to help you. before you can grasp anything, the lion raises a huge paw revealing razer sharp claws. You try to protect yourself but ultimatley fail. Resulting in your death. ")
        game_over()
        
    elif answer1 =="3":
        slowprint("As you reach for the handle you hear the sounds of birds tweeting in the night, You grasp the handle and pull , hoping youve made the right choice. As you open the door theres a strong gust of wind that takes the handle from your grip. As it opens you see the clear night sky. 'This is it im free' you scream.")
        victory() 

    else:
        wrong_choice_message()
        left_path_choice_b_1()

def left_path_choice_b_2():
    slowprint("You have chosen to go right. At this point youd be happy to eat anything! Starving and cold, you can hardly feel your feet anymore. The stones making up the floor are loose and making it exeptionly hard to walk. You keep going hoping to find some aswers soon.")
    slowprint(f"{name} after stumbling over your own feel on the loose stones, you fall yo the ground with a huge thud. After a brief cry , you decide to carry on. Ahead are two openings. One to your let and one to your right. What will you decide?")
    slowprint("To go left press 1 To go right press 3")
    answer1 = input("whats your choice => ")
    if answer1 == "1":
        slowprint("You have chosen the left opening, As you step though, your foot hits a loose brick, you hear a clicking soung coming from inside the walls. Befor you know it the walls start to get smaller and smaller. Looking around you see a screwdriver, ' No this wont help' still looking you find a large pole. You try to use it to wedge the walls, in the hope it will stop them closing in. You get it wedged, everything seems okay.... until 'SNAP' the pole breaks. Despite your best efforts the walls close in and you're crushed. ")
        game_over()
              
    elif answer1 =="3":
        slowprint("You have chosen the right opening. Stepping through You see a room at the end of a small corridor, 'This room seems brighter than the rest.' You think to yourself. As you approach the room you notice the door is slightly open. You reach for the handle, pulling the door towards you. You step inside , hearing the wind in the trees. as you go inside you notice the window is broken. ' is this large enough for me to climb through?' You put one foot on a small dresser and pull youself up to the window, and you manage to pull yourself out.")
        victory() 
    else:
        wrong_choice_message()
        left_path_choice_b_2()

# straight path


def straight_path():
    slowprint("You have chosen to go straight.'This path looked alot brighter than the others, hopefully that's a good thing' you think to yourself. Walking down the hall , you spot a pink door. Theres marks on the door. 'Is that blood?' you question yourself. Deciding to go inside the room, the lights flickering.In the dim flickering light You see an old wardrobe and decide to explore. inside the wardrobe you find some coins.")
    slowprint(f"you have {points} coins.")
    slowprint("You collect your coins , and exit the room onto a strange hallway. Before you are two directions. Which will you choose?")
    slowprint("To go left press 1 To go right press 3")
    answer1 = input("whats your choice => ")

    if answer1 == "1":
        straight_path_choice_a()    
        
    elif answer1 =="3":
        straight_path_choice_b()

    else:
        wrong_choice_message()
        straight_path()

def straight_path_choice_a():
    slowprint("You have chosen to go left. While wandering for what feels line an eterity You see a loose brick and decide to pull it out. Behind the brick is a small note. Its unreadable. you think to yourself ' this is useless!' and angrily toss it away. You find nothing useful here.")
    slowprint("Continuing down the path , you spot two staircases one to your left and one to your right. Where will you go ?")
    slowprint("To go left press 1 To go right press 3")
    answer1 = input("whats your choice => ")

    if answer1 == "1":
        add_points()
        straight_path_choice_a_1()
        
    elif answer1 == "3":
        add_points()
        straight_path_choice_a_2()

    else:
        wrong_choice_message()
        straight_path_choice_a()

def straight_path_choice_a_1():
    slowprint("You have chosen to go left. You see a figure in the distance, it sounds as though its chuckling, you begin too run but before you can get near it it disappears. Leaving nothing but a small black pouch behind. You pick it up and look inside. Nothing inside except a few strange gold coins.")
    slowprint(f"Your hearts pumping in your chest. Adrenaline kicks in, your now more determined than ever to escape. You have {points} coins.")
    slowprint("After exploring the pouch you continue walking when your faced with two doors. Both differ in size and appearence. One is smaller and newer looking, as though someone has been here recently. the other is larger and is made from steel. which will you choose?")
    slowprint("To choose the left door press 1 To choose the right door press 3")
    answer1 = input("whats your choice => ")

    if answer1 == "1":
        slowprint("You have chosen the left door, this is the door made from steel. As you reach to open it the cold metal handle in your hand, you step inside. Your once again greeted by the shaddowy figure. Before you get close enough to see who or what it is , your struck with a blunt object. You fall to the ground. Your vision starts to fade until you drift into unconsiousness.")
        game_over()  

    elif answer1 == "3":
        slowprint("You have chosen the right door. Filled with hope you reach for the handle of the smaller door, in side the room is a large painting sitting in a strange position against the wall. As you struggle to move this large painting, you see an opening behind. 'Maybe someone has been here before' you stumble to your knees and crawl through the small opening. After going through the small crawl space you feel mud on your hands and a breeze in your hair. 'IM FREE' you cry to yourself.")
        victory()
        
    else:
        wrong_choice_message()
        straight_path_choice_a_1()
    
def straight_path_choice_a_2():
    slowprint(f" {name} you have chosen to go right. You hear voices in the distance, your heart starts pumping out of your chest. You try to shout for help. but the voices seem to fade away to nothing Frantically running down the long corridor, you see a small dusty box. Upon picking it up some coins fall out on to the ground. You pick them up and continue on. ")
    slowprint(f"you now have have {points} coins.")
    slowprint("After what feels like forever your out of breath and take a minuete to catch your breath. while sitting on the cold hard floor you spot 2 more corridors ahead. one to your left and one to your right. Where will you go ?")
    slowprint("To go left press 1 To go right press 3")
    answer1 = input("whats your choice => ")

    if answer1 == "1":
        game_over()  
    elif answer1 == "3":
        victory() 
    else:
        wrong_choice_message()
        straight_path_choice_a_2()

def straight_path_choice_b():
    slowprint(f"{name} you have chosen to go right. As you're walking along the long narrow corridor, you see somthing shining in the corner of your eye. You go to investigate. Upon approaching the item you see that it is a key. You pick up the key and carefully put it in your pocket.")
    slowprint(f"{name} will this key be useful in helping you escape ? or is it just a key to no where?")
    slowprint("After collecting the key, you see an open door and go inside the room , inside the room splits in to two different directions. One to the left and one to the right. 'where to go ?' you wonder. ")
    slowprint("To go left press 1 To go right press 3")
    answer1 = input("whats your choice => ")

    if answer1 == "1":
        straight_path_choice_b_1()
        
    elif answer1 == "3":
        add_points()
        straight_path_choice_b_2() 

    else:
        wrong_choice_message()
        straight_path_choice_b()

def straight_path_choice_b_1():
    slowprint("You have chosen to go left. 'Is this a good idea ?' you worriedly think to yourself. Have you made the right choice? putting one foot infront of the other you go ahead , your feet are aching , your legs are tired. but you have to carry on and keep pushing through. Stepping on the cold hard floor, watching the bricks to the side of you pass by as your walking for what feels like hours. you finally come to the end of the corridor , it splits off into two directions. To your let and your right. where will you choose to go?")
    slowprint("To go left press 1 To go right press 3")
    answer1 = input("whats your choice => ")
    if answer1 == "1":
        slowprint(f"{name} you choose to go left, tiredly stepping down this eerie corridor, your not paying enough attention. As you step you hear a click, and the floor beneath you has dissapeared. You'd stepped on a trap door and have fallen to your death.")
        game_over()
        
    elif answer1 == "3":
        slowprint(f"{name} You have chosen the right path, 'is this the way to freedom?' you wonder as you tiredly put one foot infront of the other.The further along you get the brighter the corridor seem's , more and more light beaming from the end of the path. Rubbing your eyes and walking toward the brighness you see, you see a wall that has tumbled down and the moonlight shining ever so bright. you, clamber over the tumbled wall and out to the fresh night air. 'IM FREE' you weep to yourself.")
        victory()
    else:
        wrong_choice_message()
        straight_path_choice_b_1()

def straight_path_choice_b_2():
    slowprint(f"You have chosen to go right. {name} You're faced with nothing but a dead end and an old rusth set of ladders. Who knows where this leads? You grasb the ladders and start to climb, at the top you reach a small landing with two openings facing you . which will you choose? The left one or the right one?")
    slowprint(f"you feel someone watching you , you need to escape , can you make the right decision {name} you have {points} coins collected so far.")
    slowprint("To go left press 1 To go right press 3")
    answer1 = input("whats your choice => ")

    if answer1 == "1":
        slowprint("You have chosen the left opening, as you step through you realise there's nothing there, but a but a very small ledge but before you can rethink your decision you loose your footing and fall from the side of the building. ")
        game_over()
        
    elif answer1 == "3":
        slowprint("You have chosen the right, you step through the opening. You feel the fresh air on your face. Infront of you is a staircase leading to the gound outside. 'i made it' you cried to yourself.")
        victory()
    else:
        wrong_choice_message()
        straight_path_choice_b_2()



# Right path


def right_path():
    slowprint("You have chosen to go right. As you're walking through the long narrow corridor you see somthing on the floor. You decide to pick it up. Its a small trinket box with coins inside. After collecting your coins you continue to try and break free of this horrible place.  ")
    slowprint(f"You now have {points} coins.")
    slowprint("While walking you see 2 small crawl spaces one to your left and one to your right where will you go ?")
    slowprint("To go left press 1 To go right press 3")
    answer1 = input("What's your choice: ")

    if answer1 == "1":
        add_points()
        right_path_choice_a()
        
    elif answer1 == "3":
        add_points()
        right_path_choice_b()
    
    else:
        wrong_choice_message()
        right_path()


def right_path_choice_a():
    slowprint(f"{name} you have chosen to go left. You see chains on the wall, attatched to those is the unfortunate skeleton of past prisoners. You start to panic and pick up the pace. you start to wonder if you will ever escape? the lights are dull the halls are quiet, but you see a phone just lying on the ground, you try pressing all the buttons but nothing works. It dosent work. Beside the phone are some small coins scattered on the ground. You pick them up and bundle them into your pocket.")
    slowprint(f"you progress with {points} coins gained.")
    slowprint("You are at the end of the hall, two options ahead of you , where will you go?")
    slowprint("To go left press 1 To go right press 3")
    answer1 = input("What's your choice: ")

    if answer1 == "1":
        right_path_choice_a_1()
    
    elif answer1 == "3":
        right_path_choice_a_2()
    
    else:
        wrong_choice_message()
        right_path_choice_a()

    
def right_path_choice_a_1():
    slowprint("You have chosen to go left.")
    slowprint(f"You hear a voice laughing what sounds mile's away as you continue to drag your feet toward the strange nouise, it gets louder and louder, until......... it just dissapears. Upon getting to where you heard the noise , your standing and a gloomy empty room with nothing but two doors inside. Descision time. Where will you go?")
    slowprint("To choose the left door press 1 To choose the right right door press 3")
    answer1 = input("What's your choice: ")

    if answer1 == "1":
        slowprint("The right door lead's straight to a shark pool , you fall into the water and to your death.")
        game_over()
    
    elif answer1 == "3":
        slowprint("the right door , although is very heavy and stiff to open , finally cracks open and you fall straight through the opening on to the grass outside. You're free!")
        victory()

    else:
        wrong_choice_message()
        straight_path_choice_a_1()

def right_path_choice_a_2():
    slowprint("You have chosen to go right. Is this a good idea? This way feels cold, and scary. Your eyelids are starting to get heavy. Will you ever be free? whilst daydreaming about being home in your nice warm bed you reach the end of this route. infront ar you are two options , where will you go?")
    slowprint("To go left press 1 To go right press 3")
    answer1 = input("What's your choice: ")
    if answer1 == "1":
        slowprint("You walk left, you trip over a raised brick and land in a giant meat grinder ")
        game_over()
    
    elif answer1 == "3":
        slowprint("You have chosen right. This long hall continues until you reach a tall iron gate. You look and try to open it, you pull at the lock until it finally breaks. You open the gate and run as fast as your legs will take you.")
        victory()
    else:
        wrong_choice_message()
        straight_path_choice_a_2()   

def right_path_choice_b():
    slowprint(f"{name} you have chosen to go right. Your getting scared your never going to escape now. Hearts pounding, all you can hear is the small draft of wind whistling down the corridor. As you drag your tired feet you see ?")
    slowprint(f"You have {points} coins.")
    slowprint("To go left press 1 To go right press 3")
    answer1 = input("What's your choice: ")

    if answer1 == "1":
        add_points()
        right_path_choice_b_1()

    elif answer1 == "3":
        add_points()
        right_path_choice_b_2()  

    else:
        wrong_choice_message()
        right_path_choice_b()

def right_path_choice_b_1():
    slowprint("You have chosen to go left. Do you feel confident with that decision? it looks dark down here.You can hardly see a thing. Just a dusty table , on the table neatly stacked are some coins.")
    slowprint(f"you have {points} coins.")
    slowprint("You take the coins and run until you reach the two doors. only 2 ways to go. where will you decide?")
    slowprint("To go left press 1 To go right press 3")
    answer1 = input("What's your choice: ")

    if answer1 == "1":
        slowprint("You made the descision to go left. Hopeful you open the door and step inside, as you enter and look around...'BANG' the door slams shut behind you ' this cant be!' rubbing your eyes you start to cry. Your back where you started and you lost all your coins on the way")
        intro()
    
    elif answer1 == "3":
        slowprint("Upon opeing the right door you are faced with and unfamilar figure guarding the xit. you manage to fight him off anf run free in to the dark misty night.")
        victory()
    else:
        wrong_choice_message()
        right_path_choice_b_1()

def right_path_choice_b_2():
    slowprint(f"{name} you have chosen to go right. You walk for a while before coming to two doors , one to your left and one to your right. where will you go ?")
    slowprint(f"You have {points} coins.")
    slowprint("To go left press 1 To go right press 3")
    answer1 = input("What's your choice: ")

    if answer1 == "1":
        slowprint("You have chosen the left door. Before you can move an arrow hits you right between the eyes.")
        game_over()
    
    elif answer1 == "3":
        slowprint("You have chosen the right door. the only door in this whole building to open easily. As you open it you realise your free! ")
        victory()
    else:
        wrong_choice_message()
        right_path_choice_b_2()
        

### messages under this line

def wrong_choice_message():
    slowprint("Wrong choice")
    time.sleep(2)



def game_over():
    print("  ▄████  ▄▄▄       ███▄ ▄███▓▓█████")
    print(" ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀")
    print("▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███")
    print("░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄ ")
    print("░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒")
    print(" ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░")
    print("  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░")
    print("░ ░   ░   ░   ▒   ░      ░      ░   ")
    print("      ░       ░  ░       ░      ░  ░")
    print("                                      ")
    print(" ▒█████   ██▒   █▓▓█████  ██▀███   ▐██▌")
    print("▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒ ▐██▌")
    print("▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒ ▐██▌")
    print("▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄   ▓██▒")
    print("░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒ ▒▄▄ ")
    print("░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░ ░▀▀▒")
    print("  ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░ ░  ░")
    print("░ ░ ░ ▒       ░░     ░     ░░   ░     ░ ")
    print("    ░ ░        ░     ░  ░   ░      ░    ")
    print("              ░                         ")
    slowprint(f"Sorry {name} you have not escaped.")
    # known as gameover

def victory():
    print(" ██▒   █▓ ██▓ ▄████▄  ▄▄▄█████▓ ▒█████   ██▀███  ▓██   ██▓")
    print("▓██░   █▒▓██▒▒██▀ ▀█  ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒ ▒██  ██▒")
    print(" ▓██  █▒░▒██▒▒▓█    ▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒  ▒██ ██░")
    print("  ▒██ █░░░██░▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄    ░ ▐██▓░")
    print("   ▒▀█░  ░██░▒ ▓███▀ ░  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒  ░ ██▒▓░")
    print("   ░ ▐░  ░▓  ░ ░▒ ▒  ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░   ██▒▒▒ ")
    print("   ░ ░░   ▒ ░  ░  ▒       ░      ░ ▒ ▒░   ░▒ ░ ▒░ ▓██ ░▒░ ")
    print("     ░░   ▒ ░░          ░      ░ ░ ░ ▒    ░░   ░  ▒ ▒ ░░  ")
    print("      ░   ░  ░ ░                   ░ ░     ░      ░ ░     ")
    print("     ░       ░                                    ░ ░     ")
    slowprint(f"Victory!!! You have escaped this strange and scary building, never to see it again. with {points} coins. get yourself a snack you earned it *coins are not exchangable for real money")



story_intro()
