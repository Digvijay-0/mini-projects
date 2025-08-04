movies = {
    "Tarzen": [8, 1],
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

    if choice in movies:
        try:
            age = int(input("what is your age?: ").strip())
       
            if age < 1 or age > 100:
                print("enter valid age")

            elif age >= movies[choice][0]:
                question = (
                    input(f"would you like to buy a ticker for movie {choice} ? y/n: ")
                    .strip()
                    .capitalize()
                )

                if question == "Y" and movies[choice][1] > 0:
                    movies[choice][1] = movies[choice][1] - 1
                    print("enjoy movie")

                elif movies[choice][1] == 0:
                    print("no tickets left")
                elif question == "N":
                    pass

            else:
                print("U are young boi")

        except:
            print('? invalid age! Boi')  
    
    else:
        print('we dont have that movie u r looking for "boi"!')

"""        # check user age
        if age >= films[choice][0]:

            # check enough seats/tickets
            tickets = films[choice][1]
            if tickets > 0:  # tickets OR films[choice][1]
                print("Enjoy your Movie ")
                films[choice][1] = films[choice][1] - 1
            else:
                print("We have no seats available")"""
