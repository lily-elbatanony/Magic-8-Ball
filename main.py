def get_user_guess():
    while True:
        try:
            guess=int(input("Enter your guess(1-100)"))
            if 1<=guess<=100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input! Please enter a number.")
            