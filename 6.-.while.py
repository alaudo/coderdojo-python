answer = input("Do you want to play a game? ")

while answer == "yes":
    person1 = input("What is the first name? ")
    person2 = input("What is the second name? ")

    if person1 > person2:
        print(person1)
        print("has won")
    elif person1 == person2:
        print("friendship")
        print("has won")
    else:
        print(person2)
        print("has won")
    answer = input("Do you want to play a game? ")
