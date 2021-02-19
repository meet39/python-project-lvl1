#!/usr/bin/env python

from brain_games.cli import welcome, welcome_user
from random import randint
import prompt

def print_task():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def is_even(num):
    return 'yes' if ((num % 2) == 0) else 'no'


def main():
    welcome()
    user_name = welcome_user()
    print_task()
    count_of_correct_answers = 0

    while (count_of_correct_answers < 3):
        random_number = randint(1, 100)

        print('Question: {}'.format(random_number))
        answer = prompt.string('Your answer:')
        correct_answer = is_even(random_number)

        if (answer != correct_answer):
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(answer, correct_answer))
            print('Let\'s try again, {}!'.format(user_name))
            count_of_correct_answers = 0
        else:
            print('Correct!')
            count_of_correct_answers = count_of_correct_answers + 1

    print('Congratulations, {}'.format(user_name))


