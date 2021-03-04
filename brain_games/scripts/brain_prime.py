#!/usr/bin/env python

from brain_games import games_flow


def is_prime(num):
    counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1
    return 'yes' if counter == 2 else 'no'


def main():
    user_name = games_flow.start_game()
    games_flow.print_task(
        'Answer "yes" if given number is prime. Otherwise answer "no".'
    )
    count_of_correct_answers = 0

    while count_of_correct_answers < games_flow.req_correct_answers:
        rand_number = games_flow.generate_int()
        correct_answer = is_prime(rand_number)

        games_flow.print_question(str(rand_number))
        answer = games_flow.get_answer()

        if answer != str(correct_answer):
            games_flow.print_bad_result(answer, correct_answer, user_name)
            count_of_correct_answers = 0

        else:
            games_flow.print_good_result()
            count_of_correct_answers += 1

    games_flow.finish_game(user_name)
