#!/usr/bin/env python

# import brain_games.games_flow
from brain_games import games_flow
from random import choice


def main():
    user_name = games_flow.start_game()
    games_flow.print_task(
        'Answer "yes" if the number is even, otherwise answer "no".')

    count_of_correct_answers = 0
    listOfSign = ['+', '-', '*']

    while count_of_correct_answers < games_flow.req_correct_answers:
        first_number = games_flow.generate_int()
        second_number = games_flow.generate_int()
        sign = choice(listOfSign)
        expression = '{} {} {}'.format(first_number, sign, second_number)
        games_flow.print_question(expression)

        if sign == '+':
            correct_answer = first_number + second_number
        elif sign == '*':
            correct_answer = first_number * second_number
        elif sign == '-':
            correct_answer = first_number - second_number

        answer = games_flow.get_answer()
        if answer != str(correct_answer):
            games_flow.print_bad_result(answer, correct_answer, user_name)
            count_of_correct_answers = 0
        else:
            games_flow.print_good_result()
            count_of_correct_answers += 1

    games_flow.finish_game(user_name)
