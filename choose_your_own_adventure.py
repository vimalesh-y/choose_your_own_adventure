name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a mountainous road. It has come to an end and you can either go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer == input("You come to a river. You can walk around it or swim across. Type walk to walk around or swim to swim across: ")

    if answer == "swim":
        print("You swim across and were attacked by alligators.")
    elif answer == "walk":
        print("You walked for many miles and fainted due to running out of water - you lose.")
    else:
        print("Not a valid option - you lose!")
    
elif answer == "right":
    answer == input("You come up to a bridge which looks unstable - do you want to cross it or go back? Select cross/back ")
        
    if answer == "back":
        print("You go back to the main mountain path and lose.")
    elif answer == "cross":
        answer == input("You cross the bridge and meet a hiker. Do you talk to them? Select yes/no. ")

        if answer == "yes":
            print("You talk to the hiker and they hand you £1000 - you win!")
        elif answer == "no":
            print("You miss out on winning the money - you lose!")
        else:
            print("Not a valid option - you lose!")
    else:
        print("Not a valid option - you lose!")

else:
    print("Not a valid option - you lose!")

print("Thank you for playing", name)