import random


ROUNDS_COUNT = 3
MIN_NUMBER = 1
MAX_NUMBER = 100
GCD_INSTRUCTION = "Find the greatest common divisor of given numbers."


def gcd(number1, number2):
    while number2:
        number1, number2 = number2, number1 % number2
    return number1


def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(GCD_INSTRUCTION)

    for _ in range(ROUNDS_COUNT):
        number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
        number2 = random.randint(MIN_NUMBER, MAX_NUMBER)
        correct_answer = str(gcd(number1, number2))

        print(f"Question: {number1} {number2}")
        user_answer = input("Your answer: ")

        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
