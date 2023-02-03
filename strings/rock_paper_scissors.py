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

#Write your code below this line 👇
choice= int(input('What do you choose? Type 0 for Rock, 1 for Paper, 2 for scissors '))
if int(choice) >=3 and int(choice)< 0:
  print("you typed an invalid number")
computer= random.randint(0,2)
print(computer)
if choice == 0 and computer == 1:
  print (f"{rock} \n {paper}\n You lost")
elif choice == 0 and computer == 2:
  print (f"{rock} \n {scissors}\n You won")
elif choice == 1 and computer == 0:
  print(f"{paper} \n {rock} \n You won")
elif choice == 1 and computer == 2:
  print(f"{paper} \n {scissors} \n You lost")
elif choice == 2 and computer == 0:
  print(f"{scissors} \n {rock} \n You lost")
elif choice ==2 and computer ==1:
  print(f"{scissors} \n {paper} \n You won")
else:
  print('try again')