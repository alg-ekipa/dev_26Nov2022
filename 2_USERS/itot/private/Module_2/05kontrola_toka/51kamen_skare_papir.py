### log odigranih partija
### rezultat krajnji
### END game


import random
play = 'Y'
cpt_points = 0
your_points = 0
cnt_game=0

option_rule = {
  1 : "Rock",
  2 : "Scissors",
  3 : "Paper"
}
option_branch = option_rule.keys()


# print rezultata
def print_score(your_points,cpt_points): 
    print(f'''
    YOU    :   CPU
    {your_points}\t\t{cpt_points}''')


while play.upper() == "Y": # dok je Y igra se dalje
    option = str(input('''Please enter the number for option: 
        1. Rock
        2. Scissors 
        3. Paper
        '''))

        ### defirniranje unosa da mora biti 1- 3
    while  option.isdigit() == False or int(option) not in option_rule.keys():
        option = input('The input is not good, please re-enter option 1 - 3: \n')

    rnd_choice =  random.choice(list(option_rule.keys()))
    print(rnd_choice)
    print(option_rule.keys(rnd_choice))



    if int(option) == 1:
        cnt_game += 1
        print(f'Computer shown {rnd_choice}, and you {option}')
        if rnd_choice == 1:
            print(f'TIE')
            print_score(your_points,cpt_points)
        if rnd_choice == 2 :
            print('You won!')
            your_points += 1
            print_score(your_points,cpt_points)
        if rnd_choice == 3:
            print('Computer won!')
            cpt_points += 1
            print_score(your_points,cpt_points)

    if int(option) == 2:
        cnt_game += 1
        print(f'Computer shown {rnd_choice}, and you {option}')
        if rnd_choice == 1:
            print('Computer won!')
            cpt_points += 1
            print_score(your_points,cpt_points)
        if rnd_choice == 2 :
            print(f'TIE')
            print_score(your_points,cpt_points)
        if rnd_choice == 3:
            print('You won!')
            your_points += 1
            print_score(your_points,cpt_points)

    if int(option) == 3:
        cnt_game += 1
        print(f'Computer shown {rnd_choice}, and you {option}')
        if rnd_choice == 1:
            print('You won!')
            your_points += 1
            print_score(your_points,cpt_points)
        if rnd_choice == 2:
            print('Computer won!')
            cpt_points += 1
            print_score(your_points,cpt_points)
        if rnd_choice == 3:
            print(f'TIE')
            print_score(your_points,cpt_points)

            


            


