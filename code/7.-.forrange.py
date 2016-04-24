answer = int(input("How many times do you want to play? "))

for i in range(0,answer):
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
