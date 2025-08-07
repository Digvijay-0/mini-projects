name = input("Enter your name : ")
print("Welcome", name, "to this adventure")


def swim_across():
    q1 = input("")


ans = (
    input(
        "you are on dirt road, it has come to an end You can only go left or right. \nWhich way would you choose? "
    )
    .lower()
    .strip()
)

if ans == "right":
    ans = (
        input(
            'You came to a river you can walk around it or swim across it, \nEnter swim to "swim" across or "walk" to walk around : '
        )
        .lower()
        .strip()
    )
    if ans == "walk":
        ans = (
            input(
                'You are walking for a quite while would you still like to continue or swim across \n "walk"/"swim" : '
            )
            .lower()
            .strip()
        )
        if ans == "walk":
            print("Your ran out of water, you cant move further")
        elif ans == "swim":
            swim_across()
        else:
            print("Not valid option, \nYou Loose☠️")

    elif ans == "swim":
        swim_across()

    else:
        print("Not valid option, \nYou Loose☠️")

elif ans == "left":
    print("")

else:
    print("Not valid option, \nYou Loose☠️")
