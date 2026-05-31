# hello_world_game.py
# Simple Hello World Game Demo

def main():
    print("Welcome to the Interactive Age Game!")
    name = input("What is your name? ")
    print(f"Hello, {name}! Let's play a quick game.")
    age_input = input("Please enter your age: ")
    try:
        age = int(age_input)
        if age < 0:
            print("Age cannot be negative.")
        elif age <= 2:
            print("You are a baby.")
        elif age <= 12:
            print("You are a child.")
        elif age <= 19:
            print("You are a teen.")
        elif age <= 59:
            print("You are an adult.")
        else:
            print("You are a senior citizen.")
    except ValueError:
        print("Invalid input. Please enter a valid number for age.")

if __name__ == "__main__":
    main()
