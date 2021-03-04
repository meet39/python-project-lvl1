#!/usr/bin/env python


from brain_games.cli import welcome, welcome_user
from random import randint
import prompt

req_correct_answers = 3


def generate_int(start=1, end=100):
    return randint(start, end)


def start_game():
    welcome()
    return welcome_user()


def print_task(task):
    print(task)


def print_question(expression):
    print('Question: {}'.format(expression))


def get_answer():
    return prompt.string('Your answer:')


def print_bad_result(answer, correct_answer, user_name):
    print("'{}' is wrong answer ;(. Correct answer was '{}'."
          .format(answer, correct_answer))
    print('Let\'s try again, {}!'.format(user_name))


def print_good_result():
    print('Correct!')


def finish_game(user_name):
    print('Congratulations, {}'.format(user_name))
