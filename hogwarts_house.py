print("Welcome to the Hogwarts House Quiz!")
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

q1 = input("""
Q1: What trait do you value the most?
A. Bravery
B. Intelligence
C. Loyalty
D. Ambition
""").lower()

if q1 == "a":
    gryffindor += 1
elif q1 == "b":
    ravenclaw += 1
elif q1 == "c":
    hufflepuff += 1
elif q1 == "d":
    slytherin += 1

q2 = input("""
Q2: What is your favorite color?
A. Red
B. Blue
C. Yellow
D. Green
""").lower()

if q2 == "a":
    gryffindor += 1
elif q2 == "b":
    ravenclaw += 1
elif q2 == "c":
    hufflepuff += 1
elif q2 == "d":
    slytherin += 1

q3 = input("""
Q3: Choose a magical creature:
A. Phoenix
B. Owl
C. Badger
D. Snake
""").lower()

if q3 == "a":
    gryffindor += 1
elif q3 == "b":
    ravenclaw += 1
elif q3 == "c":
    hufflepuff += 1
elif q3 == "d":
    slytherin += 1

q4 = input("""
Q4: Pick a subject:
A. Defense Against the Dark Arts
B. Charms
C. Herbology
D. Potions
""").lower()

if q4 == "a":
    gryffindor += 1
elif q4 == "b":
    ravenclaw += 1
elif q4 == "c":
    hufflepuff += 1
elif q4 == "d":
    slytherin += 1

houses = {"Gryffindor": gryffindor, "Ravenclaw": ravenclaw, "Hufflepuff": hufflepuff, "Slytherin": slytherin}
house = max(houses, key=houses.get)
print(f"You belong to {house}!")
