
while True:
    HP_mob = 50
    choice = int(input("What do you want to do? (1:FIGHT or 2:RUN)\n"))

    if choice == 1:
        turn = int(input("How long do you want to play: "))
        print("You want to play", turn, "turns\n")
        
        for i in range(turn):
            weapon_choice = int(input("1.) Schlong\n2.) Sword\n3.) Stare\nWhat do you want to use to attack: "))
            if weapon_choice == 1:
                print("You choosed Schlong to attack..\n")
                weapon_dmg = 50
            if weapon_choice == 2:
                print("You choosed Sword to attack..\n")
                weapon_dmg = 10
            if weapon_choice == 3:
                print("You choose to stare at it...\n")
                weapon_dmg = 1
            HP_mob = HP_mob - weapon_dmg
            turn = turn - 1
            
            print(HP_mob, "HP left!")
            if turn == 0:
                  if HP_mob == 0:
                    print("YOU WIN!\n") 
                    break
                  elif HP_mob > 0:
                    print("No turns left.....")
                    print("Krajok wa YOU LOSE!\n")
                    break
            elif turn > 0:
                  if HP_mob == 0:
                    print("YOU WIN!\n")
                    break
                  elif HP_mob < 0:
                       HP_mob = HP_mob + 20
                       print("Boss resurrected!!")

            print("You still have", turn, "turns left\n")

    if choice == 2:
        print("L")
        break
