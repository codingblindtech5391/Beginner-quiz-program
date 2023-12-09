# Main entry to the quiz

from functions.start_quiz import start_quiz


def main():
    welcome_message = """
        Welcome to the quiz!\n
        This game is designed for educational purposes and for learning Python programming.\n
        Please enjoy, and good luck!\n
    """

    print(welcome_message)

    # Start the quiz
    # Returns the final score
    quiz = start_quiz()

    print(f"Quiz completed! Your score is {quiz}")



    return None

if __name__ == '__main__':
    main()