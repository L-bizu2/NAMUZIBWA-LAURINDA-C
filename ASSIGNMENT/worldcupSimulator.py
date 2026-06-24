#Initialization

morale = 80
strength = 75
tournament_active = True
current_stage = "Preparation"

print("---WELCOME TO MY 2026 WORLD CUP SIMULATOR!---")

while tournament_active:
    print(f"\nCurrent Stage:{current_stage}")
    print(f"Stats -> Morale: {morale}%, Strength: {strength}%")

#User Choices
    print("\nChoose action for this phase:")
    print("1. Intense Traning Session(Boosts Stats")
    print("2. Play Scheduled Match / Advance Stage")
    print("3. Match Delayed(Bad Weather/ Postponement)")
    print("4. Rest Team(Feature under Development)")
    print("5. Quit Simulation")

    choice = input("Enter choice(1-5):")

#Handling user choices using loops
    if choice == "1":
        print("\n--Training HARD--")
        strength += 10
        morale += 5
#loop will continue naturally to next stage        

    elif choice == "2":
        print(f"\n --Advance from {current_stage}..--")
        if current_stage == "Preparation":
            print("Preparation COMPLETE. Move to Group Stage!")
            current_stage = "Group Stage"

        elif current_stage == "Group Stage":
            #decide if they qualify based on stats
            if strength > 60:
                print("You have WON 3 matches. Move to Knockout stage!")
                current_stage = "Knockout Stage"
            else:
                print("Eliminated in the Group stage! GAME OVER.")
                break

        elif current_stage == "Knockout Stage":
            if strength >= 85 and morale >= 80:
                print("Congratulations! Your team has WON The 2026 World Cup!")
            else:
                print("Knocked out in the Semi-Final. So close!")
                break 
        if choice == "3":
            print("\nMatch has been delayed due to Bad Weather. Resetting phase..")
            continue

        #temporary placeholder using pass
        if choice == "4":
            print("\n[System Note: Team Rest logic will be fully implemented in a future update.]")
            pass
        if choice == "5":
            print("\nExiting Simulator. Adios!")
            break
        else:
            print("\nInvalid Choice. Please try again!")
            print("\ln---SIMULATOR TERMINATING---")