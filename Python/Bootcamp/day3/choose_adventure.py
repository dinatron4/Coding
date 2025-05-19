print(r'''
 _______________________________      __________________________
/                               \    /                          |
| I Love you Pudding!           /    | I will kill this brat!   |
\_________________________     /     |   _______________________/
                          \   /_______\ /
               __....----''\./         | `````----....__
          _-```             o          o                ```-_
        .'                 \S/        /P\                    `.
        |`-_              _/ \_       / \                  _-'|
        |   ```--....____                     ____....--```   |
        |                `````-----------````                |
        |-__                                               __-|
        |   ~~~--________                     ________--~~~   |
        |                ~~~~~-----------~~~~~                |
        |-__                                               __-|
        |   ~~~--________                     ________--~~~   |
        |                ~~~~~-----------~~~~~                |
         `-_                                               _-'
            ```--....____                     ____....--```
                         `````-----------''''')
print("Welcome to Whole Cake Island.\nYour mission is to escape the island.")
print("You are at the top of the wedding cake.")
action = input("           Do you want to jump or stay?(Jump or Stay)\n           ").lower()

if action == "jump":
    print("While you were flying mid-air, Luffy grabbed you with one hand.")
    print("However, before you got to Luffy, Katakuri intercepted you and you hit the floor.")
    action = input("           Do you want to run or hide?(Run or Hide)\n           ").lower()
    if action == "run":
        print("You ran in direction to the gate. In your journey, you accidentaly inhaled a poison gas from Reiju.")
        print("You started to see things, and now you see three different gates. A red, a blue and a white gate.")
        action = input("           Which one do you want to open?(Red, Blue or White)\n           ").lower()
        if action == "red":
            print("The red gate was actually Oven's back. He grabbed you and fried you alive. You are dead!")
        elif action == "blue":
            print("The blue gate was actually Daifuku's genie. He cut you in half. You are dead!")
        elif action == "white":
            print("You managed to find the correct gate and rolled down the hill.")
            print("You have now the final choice. Get to the shark-submerge or run to Sunny.")
            action = input("           Where do you want to go?(Shark or Sunny)\n           ").lower()
            if action == "shark":
                print("You have entered the shark-submerge and escaped the island. Congrats!!!")
            else:
                print("You got to the Sunny. However, Zeus and Prometheus are on top of you.\nBOOOOOOOM\nYou are dead!")
    else:
        print("Licked, Licked... You got trapped by candy and suffocated. You are dead!")
else:
    print("Mama came and smashed you into pieces. You are dead!")

