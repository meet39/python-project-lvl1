#!/usr/bin/env python

from brain_games import games_flow


def find_gcd(first, second):
    if first > second:
        smaller_num = second
    else:
        smaller_num = first

    while smaller_num != 0:
        if (first % smaller_num == 0) and (second % smaller_num == 0):
            return smaller_num
        smaller_num -= 1


def main():
    user_name = games_flow.start_game()
    games_flow.print_task(
        'Find the greatest common divisor of given numbers.'
    )
    count_of_correct_answers = 0

    while count_of_correct_answers < games_flow.req_correct_answers:
        first_number = games_flow.generate_int()
        second_number = games_flow.generate_int()

        games_flow.print_question('{} {}'.format(first_number, second_number))

        answer = games_flow.get_answer()
        correct_answer = find_gcd(first_number, second_number)

        if answer != str(correct_answer):
            games_flow.print_bad_result(answer, correct_answer, user_name)
            count_of_correct_answers = 0
        else:
            games_flow.print_good_result()
            count_of_correct_answers += 1

    games_flow.finish_game(user_name)
