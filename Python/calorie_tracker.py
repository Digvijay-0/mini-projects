food_calories = {}


def add_food():
    food_name = input("Enter the name of the food: ")
    calorie_count = int(input("Enter the number of calories in the food: "))
    food_calories[food_name] = calorie_count
    print("Food item added successfully.")


def remove_food():
    food_name = input("Enter the name of the food to be removed: ")
    if food_name in food_calories:
        del food_calories[food_name]
        print("Food item removed successfully.")
    else:
        print("Food item not found.")


def display_food():
    print("Current food items:")
    for food_name, calorie_count in food_calories.items():
        print(food_name, "- Calories:", calorie_count)


def total_calories():
    total_calories = sum(food_calories.values())
    print("Total calories consumed:", total_calories)


def hi():
    while True:
        print("\nCalorie Tracker")
        print("1. Add a food item")
        print("2. Remove a food item")
        print("3. Display current food items")
        print("4. Calculate total calories consumed")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            add_food()
        elif choice == "2":
            remove_food()
        elif choice == "3":
            display_food()
        elif choice == "4":
            total_calories()
        elif choice == "5":
            print("bYe")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    hi()
