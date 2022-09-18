import os
from add import logos, nums
from time import sleep


# clears the screen
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def start():
    while True:
        val = input('\t> ')
        if val.lower() == 'start' or val.lower() == '1':
            cls()
            for i in ['/', '-', '|', '\\', '/', '-', '|', '\\', '/', '-', '|', '\\']:
                print(f'\tgenerating images... {i}')
                sleep(0.2)
                cls()
            break
        else:
            print('\n\tInvalid input, try again...\n')
            continue
    main()


def main():
    score = 0
    while True:
        for i in range(0, 6):
            print(logos[i]['image'])
            num = 1
            print()
            for j in logos[i]['options']:
                print(f'\t{num}. {j}')
                num += 1
            print('\n\tYour Answer - ')
            while True:
                opt = input('\t> ')
                if opt not in ['1', '2', '3', '4']:
                    print('\n\tInvalid input, try again...\n')
                    continue
                else:
                    opt = int(opt)
                    break

            if logos[i]['options'][opt - 1] == logos[i]['name']:
                print('\n\t✔️ Correct :), +1 point')
                score += 1
                sleep(2)
                cls()
                continue
            else:
                print(f'\n\tWrong :(, it\'s {logos[i]["name"]}')
                sleep(2)
                cls()
                continue
        print(f'''
                ██╗   ██╗ ██████╗ ██╗   ██╗██████╗     ███████╗ ██████╗ ██████╗ ██████╗ ███████╗
                ╚██╗ ██╔╝██╔═══██╗██║   ██║██╔══██╗    ██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝
                 ╚████╔╝ ██║   ██║██║   ██║██████╔╝    ███████╗██║     ██║   ██║██████╔╝█████╗  
                  ╚██╔╝  ██║   ██║██║   ██║██╔══██╗    ╚════██║██║     ██║   ██║██╔══██╗██╔══╝    █████╗    
                   ██║   ╚██████╔╝╚██████╔╝██║  ██║    ███████║╚██████╗╚██████╔╝██║  ██║███████╗  ╚════╝
                   ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝

                                                {nums[score]}
        ''')
        print('\n\twant to play again? (Y/n): ', end="")
        confirm = input()
        confirm = confirm.lower()
        if confirm and confirm == 'y' or confirm == 'yes':
            cls()
            score = 0
            continue
        else:
            print('\n\tBye! Bye\n')
            break


cls()
print('''

                                             
             ██████╗     ██╗   ██╗    ███████╗    ███████╗    ███████╗              ██╗████████╗
            ██╔════╝     ██║   ██║    ██╔════╝    ██╔════╝    ██╔════╝              ██║╚══██╔══╝
            ██║  ███╗    ██║   ██║    █████╗      ███████╗    ███████╗    █████╗    ██║   ██║   
            ██║   ██║    ██║   ██║    ██╔══╝      ╚════██║    ╚════██║    ╚════╝    ██║   ██║   
            ╚██████╔╝    ╚██████╔╝    ███████╗    ███████║    ███████║              ██║   ██║   
             ╚═════╝      ╚═════╝     ╚══════╝    ╚══════╝    ╚══════╝              ╚═╝   ╚═╝
                              
                                                                                score: 0
              Rules - 
           ───────────
           Rules are very simple you need to just guess the image depicted,
           and you get a point. :)
                    Type 'start' to start the game.
                    
''')

if __name__ == '__main__':
    start()
