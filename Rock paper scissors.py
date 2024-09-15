import random

def print_rock():
    print("""
    _______
---'   ____)
        (_____)
        (_____)
        (____)
---.__(___)
    """)

def print_paper():
    print("""
        _______
---'    ____)____
              ______)
              _______)
             _______)
---.__________)
    """)

def print_scissors():
    print("""
        _______
---'   ____)____
              ______)
           __________)
          (____)
---.__(___)
    """)

def play_game():
    i_1 = int(input("Enter 0 for rock, 1 for paper, 2 for scissors: "))
    i_2 = random.randint(0, 2)

    if i_1 == 0:
        print_rock()
        if i_2 == 2:
            print_scissors()
            print("You lose.")
        elif i_2 == 1:
            print_paper()
            print("You win.")
        else:
            print_rock()
            print("Try again.")
    elif i_1 == 1:
        print_paper()
        if i_2 == 2:
            print_scissors()
            print("You win.")
        elif i_2 == 0:
            print_rock()
            print("You lose.")
        else:
            print_paper()
            print("Try again.")
    elif i_1 == 2:
        print_scissors()
        if i_2 == 1:
            print_paper()
            print("You lose.")
        elif i_2 == 0:
            print_rock()
            print("You win.")
        else:
            print_scissors()
            print("Try again.")
            play_game()