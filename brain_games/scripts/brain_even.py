import random


ROUNDS_COUNT = 3
MIN_NUMBER = 1
MAX_NUMBER = 100
EVEN_INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(EVEN_INSTRUCTION)

    for _ in range(ROUNDS_COUNT):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        correct_answer = "yes" if is_even(number) else "no"

        print(f"Question: {number}")
        user_answer = input("Your answer: ")

        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
