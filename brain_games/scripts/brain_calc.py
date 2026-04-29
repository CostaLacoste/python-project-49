import random


ROUNDS_COUNT = 3
MIN_NUMBER = 1
MAX_NUMBER = 20
OPERATORS = ("+", "-", "*")
CALC_INSTRUCTION = "What is the result of the expression?"


def calculate(number1, number2, operator):
    if operator == "+":
        return number1 + number2
    if operator == "-":
        return number1 - number2
    return number1 * number2


def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(CALC_INSTRUCTION)

    for _ in range(ROUNDS_COUNT):
        number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
        number2 = random.randint(MIN_NUMBER, MAX_NUMBER)
        operator = random.choice(OPERATORS)
        correct_answer = str(calculate(number1, number2, operator))

        print(f"Question: {number1} {operator} {number2}")
        user_answer = input("Your answer: ")

        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
