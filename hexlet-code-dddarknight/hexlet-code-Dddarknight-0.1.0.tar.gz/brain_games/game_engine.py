import prompt
from brain_games.cli import welcome_user


def start_game(calculate_result):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    attempt_number = 1
    max_attempts = 3
    while attempt_number <= max_attempts:
        (game_description, question, result) = calculate_result()
        if attempt_number == 1:
            print(game_description)
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer != result:
            print(f'{answer} is wrong answer ;(. Correct answer was {result}'
                  f"Let's try again, {name}!")
            return
        else:
            print('Correct')
        attempt_number += 1
    print(f'Congratulations, {name}!')
