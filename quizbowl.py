def run_quiz(questions):
   """Runs a quiz and calculates the user's score."""
   # Create a variable to store the score
   correct_answers = 0


   # Use a for loop to ask questions
   for question, correct_answ in questions.items():
       print(question)


       # Ask the user to enter their answer
       user_answ = input("Your answer: ")


       # Verify if the answer the user entered was correct or not, using the .lower() method
       correct = user_answ.lower() == correct_answ.lower()


       # Display for the user if their answer was correct or not
       if correct:
           print("Correct!")


           # Add one to the correct answer score variable
           correct_answers += 1
       else:
           print(f"Incorrect. The correct answer is {correct_answ}.")


   # Display the results
   print("Quiz ended.")
   print(f"You scored {correct_answers}/{len(questions)}.")


def main():
   """Main function to define questions and run the quiz."""
   # Define a dictionary with five questions and answers
   quiz_dictionary = {
       'What is the third planet from the Sun? ': "Earth",
       'In what year did the American Revolution begin? ': "1775",
       'In what country is the Taj Mahal located in? ': "India",
       'Who is the most famous Greek Poet? ': "Homer",
       'The central powers during World War I consisted of Germany, Austria-Hungary, the Ottoman Empire, and which other country? ': "Bulgaria"
   }


   # Run the quiz using the defined questions
   run_quiz(quiz_dictionary)


if __name__ == "__main__":
   # Execute the main function if the script is run directly
   main()