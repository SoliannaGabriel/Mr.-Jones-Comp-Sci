# My game is called "I need to get to track practice!"
# It mainly takes place in my house but also the park nearby
# you just got home from school at 4:00 pm and need to complete all of your homework to make it to track practice by 5:00 pm. In order to do this though, you must not get distracted. Do your homework!!

import time

rooms = {
    "room1": "You are in your living room. You can see your backpack on the floor and your calendar on the wall. It's 4:00 pm and you have 1 hour to finish you homework before track pratice at 5:00 pm. You can go 'upstairs' to your bedroom or 'outside' to the park.",
    "room2": "You are in your bedroom. Your bed is unmade and your desk is clutterd with books. You can start 'studying' or go 'back downstairs' to the living room.",
    "room3": "You are at the park. You can take a 'walk' or go 'back inside' to your living room.",
    "room4": "You are in the middle of studying. You can 'continue' studying or 'stop' and go to the bedroom.",
    "room5": "Time is up, you didn't finish your homework and you're late for practice. Game over."
}

current_room = "room1"

while True:
    
    print(rooms[current_room])
    action = input("What would you like to do?")
    if action == "upstairs" and current_room == "room1":
        current_room = "room2"
    elif action == "outside" and current_room == "room1":
        current_room == "room3"
    elif action == "back downstais" and current_room == "room2":
        current_room = "room1"
    elif action == "studying" and current_room == "room2":
        current_room == "room1"
    elif action == "back inside" and current_room == "room3":
        current_room == "room1"
    elif action == "continue" and current_room == "room4":
        time.sleep(30)
        print("30 minutes have passed.")
        current_room = "room4"
    elif action == "stop" and current_room == "room4":
        current_room == "room2"
    elif (time.localtime()) [3]*60+time.localtime() [4]>=60 and current_room != "room5":
        current_room = "room5"
    else:
        print("Invalid action.")
        
