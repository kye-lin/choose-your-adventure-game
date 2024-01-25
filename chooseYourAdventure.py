import matplotlib.pyplot as plt
import numpy as np
import time, os, sys
from sys import exit

'''
Todo: Write b. Build a boat scenario
'''

def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.035) # change to slower for users

def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.035)
    value = input()
    return value

name = typingInput("\nHello! What is your name?\n    ")
world = typingInput("\nWelcome, " + name + ". This is a text-based choose-your-adventure game. \n\nWARNING: This game involves gore and violence. Player discretion is advised.\n\nEach world has ONE way to win. All other paths cause death.\n\nPlease type 1 or 2 to choose a world. Then, press [ENTER].\n    ")

    
if world != '1' and world != '2':
	world = typingInput("Invalid input. Please type 1 or 2 for the world you shall start in.")

if world == '1':
    scene1_0 = typingInput("\nYou and one other passenger are the sole survivors of a plane crash. The two of you landed on the sandy shore of an unknown island with no other land in sight. It is a hot and sweaty day. What do you do?\n    a. Introduce yourself and get to know each other.\n    b. Go explore the island on your own.\n    c. Curl up in a ball and cry.\n\nType 'a', 'b', or 'c' and press [ENTER].\n    ")
    
    if scene1_0 != 'a' and scene1_0 != 'b' and scene1_0 != 'c':
        scene1_0 = typingInput("Invalid input. Type 'a', 'b', or 'c' and press [ENTER].\n    ")

    if scene1_0 == 'a':
        scene1_1 = typingInput("\nYOU CHOSE: a. Introduce yourself and get to know each other.\n\nYou introduce yourself as " + name + ". The other passenger replies that their name is _̵̜̜̞̂͝-̵̨̲͓͋́̓\̴̟̀͝͝'̶̰͍̪̝́̇;̶̢̐͜͝>̵̻̬̄̂. Next thing you know, the two of you hit it off talking about everything from hometowns and occupations to Burger King foot lettuce. Before you know it, the sun has set, the air starts to get chilly, and eerie noises start reverberating through a nearby forest. _̵̜̜̞̂͝-̵̨̲͓͋́̓\̴̟̀͝͝'̶̰͍̪̝́̇;̶̢̐͜͝>̵̻̬̄̂ asks you \"What should we do?\" What do you answer?\n    a. \"Let's start a fire!\"\n    b. \"Let's build a boat and find civilization!\"\n\nType 'a' or 'b' and press [ENTER].\n    ")
        if scene1_1 != 'a' and scene1_1 != 'b':
            scene1_1 = typingInput("Invalid input. Type 'a' or 'b' and press [ENTER].\n    ")

        if scene1_1 == 'a':
            scene1_2 = typingInput("\nYOU CHOSE: a. \"Let's start a fire!\"\n\nIt is afternoon. You both agree to meet back at the beach at sunset. You split off into a nearby forest to find firewood. After a good 30 minutes, you have an armfull of twigs, sticks, and small logs. You head back to the beach a little early. On your way back, though, you hear distant screaming. You think it's a human scream. It must be _̵̜̜̞̂͝-̵̨̲͓͋́̓\̴̟̀͝͝'̶̰͍̪̝́̇;̶̢̐͜͝>̵̻̬̄̂. You drop all your wood and run toward the screaming.\n\nGood or bad, the screaming stopped. You assume _̵̜̜̞̂͝-̵̨̲͓͋́̓\̴̟̀͝͝'̶̰͍̪̝́̇;̶̢̐͜͝>̵̻̬̄̂ is dead.\n\nSuddenly, a large ferocious animal appears, snarling and growling at you. It wants to eat you. This must be the animal that attacked _̵̜̜̞̂͝-̵̨̲͓͋́̓\̴̟̀͝͝'̶̰͍̪̝́̇;̶̢̐͜͝>̵̻̬̄̂, you think.\n\nWeaponless, you do the only thing you can do: run. Then you realize how dumb of an idea that was because the animal runs much faster than you. It chomps at you and a sharp pain shoots through your calf. You try to keep running, but it hurts so bad that you slow down. Then the animal pounces on your back and the two of you topple over.\n\nThis is it, you think. I'm gonna die. But somehow, you manage to elbow the animal hard enough so that it backs off for a split second. Then you grab a nearby rock and throw it at the animal. It hits and dislocates the animal's leg. You half-run half-limp away.\n\nYou eventually get to the beach. Exhausted and light-headed from losing blood, you close your eyes and fall asleep listening to the hushed pulling and tugging of the ocean waves.\n\nTHE END.\n\nThanks for playing! Press any key and then [ENTER] to restart the program.\n    ")
            if isinstance(scene1_2, str):
                os.execl(sys.executable, sys.executable, *sys.argv)
        elif scene1_1 == 'b':
            scene1_2 = typingInput("\nYOU CHOSE: b. \"Let's build a boat and find civilization!\"\n\nThe two of you decide to find materials for building a boat. The best bet seems to be finding enough wood to build a raft.\n\nFast forward three weeks. After constant trial and error and hunting-for-food breaks, you finally finish building a raft, as well as four paddles.\n\nExcitedly, you two aboard the raft with a store of food and water and a plan to keep paddling until you reach land. However, after a few hours of paddling, the raft starts leaking, and the two of you end up struggling against freezing cold water. The waves keep crashing into your face and pulling you under, until you drown. As your last breath escapes your lungs, you wonder if _̵̜̜̞̂͝-̵̨̲͓͋́̓\̴̟̀͝͝'̶̰͍̪̝́̇;̶̢̐͜͝>̵̻̬̄̂ is okay or not.\n\nTHE END.\n\nThanks for playing! Press any key and then [ENTER] to restart the program.\n    ")
    
    elif scene1_0 == 'b':
        scene1_1 = typingInput("\nYOU CHOSE: b. Go explore the island on your own.\n\nEmbracing your lone wolf energy, you leave the other passenger and trek toward the center of the island.\n\nAfter walking about a mile, you come across a strange looking tree. It bears a type of spiky red fruit you have never seen before. Your stomach has been rumbling for the past hour, and there has been no other sign of food so far. What do you do?\n    a. Pick the fruit and eat it.\n    b. Keep walking. Eating the fruit could be dangerous.\n\nType 'a' or 'b' and press [ENTER].\n    ")

        if scene1_1 != 'a' and scene1_1 != 'b':
            scene1_1 = typingInput("Invalid input. Type 'a' or 'b' and press [ENTER].\n .   ")

        if scene1_1 == 'a':
            scene1_2 = typingInput("\nYOU CHOSE: a. Pick the fruit and eat it.\n\nYou find a fruit low enough for you to reach. After some struggling, you eventually pick it and hungrily take a bite. It tastes surprisingly good. You eat the entire fruit before climbing the tree to pick more fruits. Happily, you think about how you'll collect an armload of fruits to sustain you until help arrives.\n\nThen you start feeling the symptoms. Your throat swells up and your skin starts to burn. Your eyes well up with tears. What starts as an allergic reaction becomes immense pain all over your body. You cough up blood and start foaming at the mouth. The sun shining down on you looks oddly like a person with arms reaching down at you. Then you pass out and die.\n\nTHE END.\n\nThanks for playing! Press any key and then [ENTER] to restart the program.")
            if isinstance(scene1_2, str):
                os.execl(sys.executable, sys.executable, *sys.argv)
    
    elif scene1_0 == 'c': 
        scene1_1 = typingInput("\nYOU CHOSE: c. Curl up in a ball and cry.\n\nOk crybaby. Without moving from your spot, you shrink into a fetal position, hugging your knees. You tears start flowing down your face, each drop plopping on the sand and sinking down into the abyss. Then you fall asleep.\n\nWhen you wake up the next morning, the other passenger is gone. You are all alone. You decide that you need to find food and water before it's too late.\n\nAfter walking about a mile, you come across a strange looking tree. It bears a type of spiky red fruit you have never seen before. Your stomach has been rumbling for the past hour, and there has been no other sign of food so far. What do you do?\n    a. Pick the fruit and eat it.\n    b. Keep walking. Eating the fruit could be dangerous.\n\nType 'a' or 'b' and press [ENTER].\n    ")
        
        if scene1_1 != 'a' and scene1_1 != 'b':
            scene1_1 = typingInput("Invalid input. Type 'a' or 'b' and press [ENTER].\n")
        if scene1_1 == 'a':
            scene1_2 = typingInput("\nYOU CHOSE: a. Pick the fruit and eat it.\n\nYou find a fruit low enough for you to reach. After some struggling, you eventually pick it and hungrily take a bite. It tastes surprisingly good. You eat the entire fruit before climbing the tree to pick more fruits. Happily, you think about how you'll collect an armload of fruits to sustain you until help arrives.\n\nThen you start feeling the symptoms. Your throat swells up and your skin starts to burn. Your eyes well up with tears. Then your skin starts to stretch and you grow 10 feet in size. Your muscles plump up. Suddenly, you are super buff!!! Any animals that look at you cower in fear.\n\nWith your newfound strength, you are able to hunt easily for food, climb any tree, and build a shack out of wood for shelter. Things are looking good. You end up staying on the island for about a month, sustaining yourself on the local flora and fauna until a random yacht appears in the distance one day. You start a fire so the captain will notice the smoke and come by the island. Then you onboard the ship and start your journey to home sweet home.\n\nTHE END.\n\nThanks for playing! Press any key and then [ENTER] to restart the program.")
            if isinstance(scene1_2, str):
                os.execl(sys.executable, sys.executable, *sys.argv)
        elif scene1_1 == 'b':
            scene1_2 = typingInput("\nYOU CHOSE: b. Keep walking. Eating the fruit could be dangerous.\n\nNice one, smartiepoo. Despite your panging stomach, which is screaming for sustenance, you force your legs to keep moving to find some other kind of food. You keep walking and eventually end up in a forest\n\nWhat the----why is there a snake just lying on one of the branches of the trees? Curious, you take a closer look. It appears to be dead.\n.\n.\n.\n.\n.\n.\n.\nSIIIIIKE. Its eyes pop open and center on you. Before you can run away, it lunges at you, bites your face, and then recoils into the leaves of the tree until it is out of sight. Stinging with pain, you fall to the ground. The world starts to go in and out of focus, and your hearing wavers.\n\nThen you die.\n\nTHE END.\n\nThanks for playing! Press any key and then [ENTER] to restart the program.") 
            if isinstance(scene1_2, str):
                os.execl(sys.executable, sys.executable, *sys.argv)

elif world == '2':
    scene2_0 = typingInput("\nYou wake up in a mysterious forest. Surrounding you are trees so tall and luscious that they obstruct your view of the sky. You hear faint rustling in a nearby bush. What do you do?\n    a. Climb a tree to scout the area.\n    b. Sneak over to the bush and see what creature is inside.\n    c. Run away. What if it's a man-eating tiger!?!?\n\nType 'a', 'b', or 'c' and press [ENTER].\n    ")

    if scene2_0 != 'a' and scene2_0 != 'b' and scene2_0 != 'c':
        scene2_0 = typingInput("Invalid input. Type 'a', 'b', or 'c' and press [ENTER].\n    ")

    if scene2_0 == 'a':
        scene2_1 = typingInput("\nYOU CHOSE: a. Climb a tree to scout the area.\n\n As the smartie-poo you are, you scale up the closest tree that you are able to climb. You get about 8 feet high before stopping. You see a small hut among the dense trees. \n    You decide to climb down and approach the small hut. After 30 minutes, you get to the front door. It's a moldy wooden cabin with only one room and one window. You knock on the door. It creaks open and reveals a haggard old woman. Her frizzy gray hair sticks up in all directions. She takes one look at you, snarls like a cat, and slams the door. What do you do?\n    a. Try knocking again.\n    b. Leave.\n\nType 'a' or 'b' and press [ENTER].\n    ")
        if scene2_1 == 'a':
            scene2_2 = typingInput("\nYOU CHOSE: a. Try knocking again.\n\nYou knock on the old woman's door again. No response. You wait 1..2..3......10 long seconds before giving up.\n\nYou turn around to leave, when you hear a strange wooshing sound and then feel a dull pain in your back.\n.\n.\n.\n.\n.\n.\n.\n.\nThe woman just threw an axe into your back.\n\nYou fall to your knees, face smushing into the muddy grass. Your blood stains the dirt around you red. Your vision starts to blur. \n\nYour life flashes before your eyes---memories as a child, memories with your family, memories with friends, good times, bad times---until a bright light takes over your consciousness and you black out for good.\n\nTHE END.\n\nThanks for playing! Press any key and then [ENTER] to restart the program.")
            if isinstance(scene2_2, str):
                os.execl(sys.executable, sys.executable, *sys.argv)
            
        elif scene2_1 == 'b':
            scene2_2 = typingInput("\nYOU CHOSE: b. Leave.\n\nYou turn around and walk away. You keep walking for hours and hours until you notice a hiking trail. You follow the 5-mile-long hiking trail until you get to a parking lot. A group of hikers who are socializing notice you. You look terrible. Your eyes are sunken and your lips are parched because you are dehydrated. You almost pass out when the group of hikers shouts in alarm and runs over to catch you. They give you water and ask you a million questions. They figure out where you live, and one of them gives you a ride to the nearest bus station and sends you on your way to home sweet home.\n\nTHE END.\n\nThanks for playing! Press any key and then [ENTER] to restart the program.")
            if isinstance(scene2_2, str):
                os.execl(sys.executable, sys.executable, *sys.argv)
        else:
            scene2_1 = typingInput("Invalid input. Type 'a' or 'b' and press [ENTER].")
    
    elif scene2_0 == 'b':
        scene2_1 = typingInput("\nYOU CHOSE: b. Sneak over to the bush and see what creature is inside.\n\nOut of curiosity, you tiptoe over to the bush and peer inside. Bright yellow eyes look back at you. Next thing you know, you're getting scratched by some feral animal. Its claws are huge and as sharp as knives. It starts eating you alive. The pain is intolerable, and with all the blood you're losing, it's getting hard to focus anymore. Eventually, the animal gets to your heart and rips that apart, and you breathe your last breath.\n\nTHE END.\n\nThanks for playing! Press any key and then press [ENTER] to restart the program.")

        if isinstance(scene2_1, str):
            os.execl(sys.executable, sys.executable, *sys.argv)
    
    elif scene2_0 == 'c': 
        typingPrint("\nYOU CHOSE: c. Run away. What if it's a man-eating tiger!?!?\n\nBetter safe than sorry. You sprint away from the bush of unknown terrors for a good five minutes until you must stop to catch your breath. Your armpits are drenched in sweat. At least the air is cool and misty. When you finally calm down a bit, you notice the sound of running water, and realize how thirsty you are.\n\nYour phone is almost out of battery, but you are smart enough to check the weather for the next 10 days. The weather app shows a graph of temperatures plotted against time.\n\n")
        # matplotlib graph
        fig = plt.figure(figsize=(6.4, 6.4))
        ax = plt.axes()

        times = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        temp = np.array([78, 82, 85, 81, 87, 90, 92, 96, 102, 93])

        ax.plot(times, temp)

        ax.set_title('10-Day Daily Average Temperatures at Your Location')
        ax.set_xlabel('Days')
        ax.set_ylabel('Temperature (F)')
        ax.grid()

        fig.text(0.5, 0.01, 'Close this window to continue the game.', horizontalalignment='center')

        plt.show()

        scene2_1 = typingInput("You decide that since it's going to be hot, you should stay near the river to prevent dehydration. You drink some of the water. It tastes like shit. Then you try to find food around the area but fail. Later, when night falls, you wonder if the water was clean. It probably wasn't, you realize. Then you fall asleep.\n\nThe next day, you wake up with a raging fever and diarhhea. The water must have been dirty, as expected. You try to wait out the fever, but it gets so unbearable. The hot, humid climate does not help. You try to walk around and find food, but it is difficult because you get dizzy after every 10 steps or so.\n\nThe day after, your illness gets worse. You can barely move or breathe. You cannot get up. Then you die.\n\nTHE END.\n\nThanks for playing! Press any key and then press [ENTER] to restart the program.")
        
        if isinstance(scene2_1, str):
            os.execl(sys.executable, sys.executable, *sys.argv)




"""
elif world == '3':
    scene3_0 = typingInput("\nYou are the new governor of California, and an aspiring senator. Your dream is to beat the world record for the longest filibuster: 24 hours and 18 minutes (last updated: 2023). The primary elections are coming up in about 3 months. What do you do?\n    A. Contact your campaign team and schedule a meeting.\n    B. Fabricate a scandal about your opponent and report it to a notable news organization. \n    C. Take a nap. The elections will take care of themselves.\n\nType 'A', 'B', or 'C' and press [ENTER].")
    if scene3_0 == 'A':
        scene3_1 = typingInput("\nYOU CHOSE: A. \n\n")
    elif scene3_0 == 'B':i
        scene3_1 = typingInput("\nYOU CHOSE: B. \n\n")
    elif scene3_0 == 'C': 
        scene3_1 = typingInput("\nYOU CHOSE: C. \n\n")
    else:
        scene3_1 = typingInput("Invalid input. Type 'A', 'B', or 'C' and press [ENTER].")
"""

