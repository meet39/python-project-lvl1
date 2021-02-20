#!/usr/bin/env python

from brain_games.games_flow import *

from random import randint


def is_even(num):
    return 'yes' if ((num % 2) == 0) else 'no'


def generate_int():
    return randint(1, 100)


def main():
    user_name = start_game()
    print_task('Answer "yes" if the number is even, otherwise answer "no".')
    count_of_correct_answers = 0

    while count_of_correct_answers < req_correct_answers:
        random_number = generate_int()
        print_question(random_number)

        answer = get_answer()
        correct_answer = is_even(random_number)

        if answer != correct_answer:
            print_bad_result(answer, correct_answer, user_name)
            count_of_correct_answers = 0
        else:
            print_good_result()
            count_of_correct_answers += 1

    finish_game(user_name)
