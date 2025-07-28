films = {
    "How To Train Your Dragon": [15, 1],
    "Big Hero 6": [12, 4],
    "Your Name": [15, 2],
    "Silent Voice": [18, 2],
    "Broly Movie": [18, 1],
    "Jujutsu Kaisen": [18, 5],
    "Weathering With You": [16, 2],
}

while True:
    choice = input("What movie you would like to Watch?: ").strip().title()

    if choice in films:
        age = int(input("what is your age?: ").strip())

        # check user age
        if age >= films[choice][0]:

            # check enough seats/tickets
            tickets = films[choice][1]
            if tickets > 0:  # tickets OR films[choice][1]
                print("Enjoy your Movie ")
                films[choice][1] = films[choice][1] - 1
            else:
                print("We have no seats available")

        else:
            print("U are young boi")

    else:
        print('we dont have that movie u r looking for "boi"!')
