#!/usr/bin/env python

from brain_games import games_flow


def is_even(num):
    return 'yes' if ((num % 2) == 0) else 'no'


def main():
    user_name = games_flow.start_game()
    games_flow.print_task(
        'Answer "yes" if the number is even, otherwise answer "no".'
    )
    count_of_correct_answers = 0

    while count_of_correct_answers < games_flow.req_correct_answers:
        random_number = games_flow.generate_int()
        games_flow.print_question(random_number)

        answer = games_flow.get_answer()
        correct_answer = is_even(random_number)

        if answer != correct_answer:
            games_flow.print_bad_result(answer, correct_answer, user_name)
            count_of_correct_answers = 0
        else:
            games_flow.print_good_result()
            count_of_correct_answers += 1

    games_flow.finish_game(user_name)
