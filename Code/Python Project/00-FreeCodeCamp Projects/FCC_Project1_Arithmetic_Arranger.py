def arithmetic_arranger(problems, show_answers=False):
    # 1. check the length of the parameters
    if len(problems) > 5:
        return "Error: Too many problems."

    # 2.check the operand
    operators = []
    for problem in problems:
        lst = problem.split()
        operators.append(lst[1])

    for operator in operators:
        if operator in ["*", "/"]:
            return "Error: Operator must be '+' or '-'."

    # 3. check for non-digits
    numbers = []
    for problem in problems:
        lst = problem.split()
        numbers.append(lst[0])
        numbers.append(lst[2])

    for number in numbers:
        if not number.isdigit():
            return "Error: Numbers must only contain digits."
        # 4. Check operand length
        elif len(number) > 4:
            return "Error: Numbers cannot be more than four digits."

    # 5. Evaluation
    answers = []
    top_row = ""
    bottom_row = ""
    dashes = ""
    answer_row = ""

    for i in range(0, len(numbers), 2):
        num1 = int(numbers[i])
        num2 = int(numbers[i + 1])
        operator = operators[i // 2]

        if operator == "+":
            result = num1 + num2
        else:
            result = num1 - num2
        answers.append(result)

        # 6. formatting problem rows
        space_width = max(len(numbers[i]), len(numbers[i + 1])) + 2
        top_row += numbers[i].rjust(space_width)
        bottom_row += operator + numbers[i + 1].rjust(space_width - 1)
        dashes += "-" * space_width
        # 7. Spacing between problems
        if i != len(numbers) - 2:
            top_row += " " * 4
            bottom_row += " " * 4
            dashes += " " * 4

    # 8. Formating answer row
    for i in range(len(answers)):
        space_width = max(len(numbers[2 * i]), len(numbers[2 * i + 1])) + 2
        answer_row += str(answers[i]).rjust(space_width)

        # 9. Spacing between answers
        if i != len(answers) - 1:
            answer_row += " " * 4

    # 10. final arrangement and return
    if show_answers:
        arranged_problems = "\n".join((top_row, bottom_row, dashes, answer_row))
    else:
        arranged_problems = "\n".join((top_row, bottom_row, dashes))

    return arranged_problems


print()
print(f'{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}')
