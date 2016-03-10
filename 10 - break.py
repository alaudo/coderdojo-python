while True:
    answer = input("Do you want to play a game? ")
    if (answer != "yes"):
        break
    else:
        person1 = input("What is the first name? ")
        person2 = input("What is the second name? ")

        if person1 > person2:
            print(person1)
        elif person1 == person2:
            print("friendship")
        else:
            print(person2)
        print("has won")
    
