import random
user_choice = input("What do you choose ? Type 0 for Rock , 1 for Paper , 2 for Scissor\n")
computer_choice = random.randint(0,2)
print("Computer_choose")
if user_choice == 0 and computer_choice==1:
    print("Hey Cheers You win")
elif user_choice == 2 and computer_choice==1:
    print("Hey Cheers You win")
elif user_choice == 2 and computer_choice==0:
    print("Hey Cheers You win")
elif user_choice == 1 and computer_choice==2:
    print("Eat your Shit")
elif user_choice == 0 and computer_choice==2:
    print("Eat your Shit")
elif user_choice == 1 and computer_choice==0:
    print("Eat your Shit")
else:
    print("Jerk off")