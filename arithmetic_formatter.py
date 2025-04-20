#arithmetic_formatter

def arithmetic_arranger(problems, show_answers=False):
    operators = ['+', '-']

    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_line = []
    second_line = []
    dashes_line = []
    answers_line = []  

    for problem in problems:
        parts = problem.split()
        num_1 = parts[0]
        operator = parts[1]
        num_2 = parts[2]

        if operator not in operators:
            return "Error: Operator must be '+' or '-'."

        if not num_1.isdigit() or not num_2.isdigit():
            return 'Error: Numbers must only contain digits.'

        if len(num_1) > 4 or len(num_2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        if show_answers:
            if operator == '+':
                answer = str(int(num_1) + int(num_2))
            elif operator == '-':
                answer = str(int(num_1) - int(num_2))

        width = max(len(num_1), len(num_2)) + 2
        first_line.append(num_1.rjust(width))
        second_line.append(operator + num_2.rjust(width - 1))
        dashes_line.append('-' * width)

        if show_answers:
            answers_line.append(answer.rjust(width))

    arranged = (
        '    '.join(first_line) + '\n' +
        '    '.join(second_line) + '\n' +
        '    '.join(dashes_line)
    )

    if show_answers:
        arranged += '\n' + '    '.join(answers_line)

    return arranged

print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')