### Game conter ne broji partiju, ako je krivi unos bio
### log odigranih partija  game_log
### probati pokanuti cijelu while PLAY petlju za TAB kako bi se mogao mjenjati Y/N prije konacnog kraja
### rezultat krajnji
### END game


'''TODO'''

import random
play = 'Y'
cpt_points = 0
your_points = 0
cnt_game=0
limit = 3 # za TEST
game=''
end_game = False

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

game_log = {}

option_rule = {
  1 : "Rock",
  2 : "Scissors",
  3 : "Paper"
}
option_branch = option_rule.keys()


# print rezultata i broja partija
def print_score(your_points,cpt_points): 
    print(f'''
    Game played: {cnt_game}
    YOU    :   CPU
    {your_points}\t\t{cpt_points}''')

def test_game(game):  # provjera zelis li novu igru
    while game.upper() not in ["N","Y"]:
        game = input('Enter error. Do you wont new game? N - ne; Y - da:\n ')
    if game.upper() in ["N","Y"]:
        return True

print('prije wile play')

while play.upper() == "Y":  # dok je Y igra se dalje
    while end_game == False: # False dok ne zavrsi igra
        option = str(input('''Please enter the number for option: 
                1. Rock
                2. Scissors 
                3. Paper
    You choose: '''))

            ### defirniranje unosa da mora biti 1- 3
        while  option.isdigit() == False or int(option) not in option_rule.keys():
            option = input('The input is not good, please re-enter option 1 - 3: \n')

        rnd_choice =  random.choice(list(option_rule.keys()))

        if int(option) == 1:
            cnt_game += 1
            print(f'''Computer shown {option_rule[rnd_choice]}, and you {option_rule[int(option)]}''')
            if rnd_choice == 1:
                print(bcolors.WARNING + '\tTIE' + bcolors.ENDC)
                print_score(your_points,cpt_points)
            if rnd_choice == 2 :
                print(bcolors.OKGREEN + '\tYou won!'+ bcolors.ENDC)
                your_points += 1
                print_score(your_points,cpt_points)
            if rnd_choice == 3:
                print(bcolors.FAIL +'\tComputer won!' + bcolors.ENDC)
                cpt_points += 1
                print_score(your_points,cpt_points)
            game_log[cnt_game]= [rnd_choice, int(option), your_points,cpt_points]
            if your_points == limit or cpt_points == limit:
                end_game = True
                
        if int(option) == 2:
            cnt_game += 1
            print(f'Computer shown {rnd_choice}, and you {option}')
            if rnd_choice == 1:
                print(bcolors.FAIL +'\tComputer won!' + bcolors.ENDC)
                cpt_points += 1
                print_score(your_points,cpt_points)
            if rnd_choice == 2 :
                print(bcolors.WARNING + '\tTIE' + bcolors.ENDC)
                print_score(your_points,cpt_points)
            if rnd_choice == 3:
                print(bcolors.OKGREEN + '\tYou won!'+ bcolors.ENDC)
                your_points += 1
                print_score(your_points,cpt_points)
            game_log[cnt_game]= [rnd_choice, int(option), your_points,cpt_points]
            if your_points == limit or cpt_points == limit:
                end_game = True
                
        if int(option) == 3:
            cnt_game += 1
            print(f'Computer shown {rnd_choice}, and you {option}')
            if rnd_choice == 1:
                print('You won!')
                your_points += 1
                print_score(your_points,cpt_points)
            if rnd_choice == 2:
                print(bcolors.FAIL +'\tComputer won!' + bcolors.ENDC)
                cpt_points += 1
                print_score(your_points,cpt_points)
            if rnd_choice == 3:
                print(bcolors.WARNING + '\tTIE' + bcolors.ENDC)
                print_score(your_points,cpt_points)
            game_log[cnt_game]= [rnd_choice, int(option), your_points,cpt_points]
            if your_points == limit or cpt_points == limit:
                end_game = True
                
        if end_game == True:
            print('    Game log:')
            print(' #  C  M  MP CP')
            for g_l_key,g_l_Value  in game_log.items():
                print(f' {g_l_key} {g_l_Value}')
        
        ###### Pitanje nove igre? #######
    if end_game == True:  
        game = input('Do you wont new game? N - no; Y- yes: \n') 
        while game.upper() not in ["N","Y"]:
            game = input('Enter error. Do you wont new game? N - ne; Y - da:\n ')
            if game.upper() in ["N","Y"]:
                play=game
       

        end_game = False  ### resetiranje logova na 0
        game_log = {}
        nt_game = 0
        your_points = 0
        cpt_points = 0
           
print('END GAME')