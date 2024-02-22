import random


def generate_powerball_numbers():
   """Generates and prints PowerBall numbers."""
   # Generate random numbers for the main balls (1 to 69)
   main_balls = [random.randint(1, 69) for _ in range(5)]
  
   # Generate a random number for the PowerBall (1 to 26)
   powerball = random.randint(1, 26)
  
   # Print the generated numbers
   print("Your PowerBall numbers are:", *main_balls, "PowerBall:", powerball)


def main():
   """Main function to welcome the user and generate PowerBall numbers."""
   print("Welcome to the PowerBall number generator.")
  
   # Ask the user if they want PowerBall numbers
   answer = input("Would you like some PowerBall numbers? (yes/no): ").lower()
  
   # Check the user's response
   if answer == "yes":
       generate_powerball_numbers()
   else:
       print("You have ended the program.")
  
   # Thank the user for stopping by
   print("Thank you for stopping by.")


if __name__ == "__main__":
   # Execute the main function if the script is run directly
   main()