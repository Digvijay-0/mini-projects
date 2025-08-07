name = input("Enter your name : ").strip().title()
print("Welcome", name, "to this adventure")


def swim_across():
    q1 = (
        input(
            "You cross a river, Your cloths are wet. \nSoon its gooing to be dusk \n Would you like to move forward or stay till dawn (stay/walk) : "
        )
        .lower()
        .strip()
    )
    print("____________________________________________________________")
    if q1 == "stay":
        print("You were poison by snake, \nYou are ☠️")

    elif q1 == "walk":
        q2 = (
            input("You see a stranger, \nWould you like to talk with him? (yes/no) : ")
            .lower()
            .strip()
        )
        print(" ")
        if q2 == "yes":
            q3 = (
                input(
                    "Hello whats your name😑 ? \nwill you tell him your real name or not as he seems suspicious \n Enter name you ganna tell him : "
                )
                .title()
                .strip()
            )
            if q3 == name:
                print("Stanger man gives you a Gold coin \n🏆 You Won the Game 🏆")

            else:
                print("Stranger stabs you 🔪🩸")

        elif q2 == "no":
            print(
                "Stranger follows you, You run try to escape but due to continue travelling You are tired..He catches you... \n and stabs you 🔪🩸"
            )
        else:
            print("Not valid option, \nYou Loose☠️")
    else:
        print("Not valid option, \nYou Loose☠️")


ans = (
    input(
        "you are on dirt road, it has come to an end You can only go left or right. \nWhich way would you choose? : "
    )
    .lower()
    .strip()
)
print(" ")
if ans == "right":
    ans = (
        input(
            'You came to a river you can walk around it or swim across it, \nEnter swim to "swim" across or "walk" to walk around : '
        )
        .lower()
        .strip()
    )
    print(" ")
    if ans == "walk":
        ans = (
            input(
                "You are walking for a quite while would you still like to continue or swim across \n (walk/swim) : "
            )
            .lower()
            .strip()
        )
        if ans == "walk":
            print("Your ran out of water, you cant move further ☠️")
        elif ans == "swim":
            swim_across()
        else:
            print("Not valid option, \nYou Loose☠️")

    elif ans == "swim":
        swim_across()

    else:
        print("Not valid option, \nYou Loose☠️")

elif ans == "left":
    ans1 = (
        input(
            """There is a old wooden bridge, would you like to move forward or just go back to main road, \nEnter "walk" to move forward or "back" to return to main road: """
        )
        .strip()
        .lower()
    )
    print(" ")
    if ans1 == "walk":
        ans1 = (
            input(
                "The bridge start to swing as intensity of wind is increase and one of wooden steps breaks, \nYou dont know whether the you will be able to make it \nwould you like to continue or jump in flowing water below (walk/jump): "
            )
            .strip()
            .lower()
        )
        if ans1 == "jump":
            swim_across()
        elif ans1 == "walk":
            print(
                "You foot stuck in one of the plank of bridge, as you try to remove it the bridge ropes breaks \n Your foot is stuck and you smash to a cliff ☠️"
            )
        else:
            print("Not valid option, \nYou Loose☠️")
    elif ans1 == "back":
        print("You see a small girl crying and you loose ☠️")

    else:
        print("Not valid option, \nYou Loose☠️")

else:
    print("Not valid option, \nYou Loose☠️")
