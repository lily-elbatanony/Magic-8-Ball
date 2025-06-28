import random
responses=["Yes, definitely!",
           "No, not now,",
           "Ask again later.",
           "Its certain.",
           "Very doubtful",
           "Outlook is good.",
           "Better not tell you now.",
           "Concentrate and ask again."]
def get_random_response():
    return random.choice(responses)
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
            
def display_response(response):
    print("\nThe Magic 8-Ball says: ", response, "\n")

def play_again():
    while True:
        choice=input("Do you want to ask another quetion-yes, no? ").strip().lower()
        if choice=="yes":
            return True
        elif choice=="no":
            print("Thanks for playing! Goodbye!")
            return False
        else:
            print("Pleasw type 'yes', or 'no'.")
