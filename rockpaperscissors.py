import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images = [rock,paper,scissors]



user =  int(input("whats your choice: 0 for rock, 1 for paper, 2 for scissors - "))
if user >= 3:
 print("You entered invalid number!")
else:
    print("You choose:")
    print(images[user])
 
    computer = random.randint(0,2)
    print("computer choose:")
    print(images[computer])
    
    if user == 0 and computer == 2:
            print("YOU WIN!")
    elif computer == 0 and user == 2:
            print("YOU LOSE!")
    elif user > computer:
                print("YOU WIN!")
    elif computer > user:
                print("YOU LOSE!")

    
