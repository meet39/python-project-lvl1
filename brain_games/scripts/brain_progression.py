#!/usr/bin/env python

from brain_games import games_flow


def generate_expression():
    count_of_numbers = games_flow.generate_int(5, 10)
    missed_position = games_flow.generate_int(0, count_of_numbers)

    start_number = games_flow.generate_int()
    additional = games_flow.generate_int()
    expression = ''

    for i in range(count_of_numbers):
        if i == missed_position:
            expression += ' ..'
            start_number += additional
            answer = start_number

        else:
            start_number += additional
            expression += ' ' + str(start_number)

    return expression, answer


def main():
    user_name = games_flow.start_game()
    games_flow.print_task(
        'What number is missing in the progression?'
    )
    count_of_correct_answers = 0

    while count_of_correct_answers < games_flow.req_correct_answers:
        (expression, correct_answer) = generate_expression()

        games_flow.print_question(expression)
        answer = games_flow.get_answer()

        if answer != str(correct_answer):
            games_flow.print_bad_result(answer, correct_answer, user_name)
            count_of_correct_answers = 0

        else:
            games_flow.print_good_result()
            count_of_correct_answers += 1

    games_flow.finish_game(user_name)
