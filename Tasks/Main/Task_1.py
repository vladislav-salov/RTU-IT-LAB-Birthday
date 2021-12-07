# Задание 1: "Ассистент".


def input_procedure(day_memory_limit, week_memory_limit):
    memory = {}
    week_memory_questions = []
    week_memory_answers = []
    day_memory_questions = []
    day_memory_answers = []
    current_day_memory = 0
    current_week_memory = 0
    day_of_week = 0
    output = []
    while True:
        input_text = input()
        if input_text == "~":
            break
        if input_text != "day":
            command, text = map(str, input_text.split())
            if command == "learn":
                question, answer = map(str, text.split(":"))
                day_memory_questions.append(question)
                day_memory_answers.append(answer)
                current_day_memory += 1
                if current_day_memory > day_memory_limit:
                    day_memory_questions.pop(0)
                    day_memory_answers.pop(0)
            elif command == "student":
                value = memory.get(text)
                if value is not None:
                    output.append(memory[text])
                    continue
                if text in week_memory_questions:
                    memory_questions_reversed = week_memory_questions[::-1]
                    output.append(week_memory_answers[len(week_memory_questions) -
                                                      memory_questions_reversed.index(text) - 1])
                    continue
                if text in day_memory_questions:
                    memory_questions_reversed = day_memory_questions[::-1]
                    output.append(day_memory_answers[len(day_memory_questions) -
                                                     memory_questions_reversed.index(text) - 1])
                else:
                    output.append("")
        else:
            if len(day_memory_questions) != 0:
                for element in day_memory_questions:
                    week_memory_questions.append(element)
                for element in day_memory_answers:
                    week_memory_answers.append(element)
                current_week_memory += len(day_memory_questions)
                if current_week_memory > week_memory_limit:
                    for i in range(current_week_memory - week_memory_limit):
                        week_memory_questions.pop(0)
                        week_memory_answers.pop(0)
            if day_of_week == 7:
                day_of_week = 0
                current_week_memory = 0
                for i in range(len(week_memory_questions)):
                    memory[week_memory_questions[i]] = week_memory_answers[i]
                week_memory_questions = []
                week_memory_answers = []
            day_of_week += 1
            day_memory_questions = []
            day_memory_answers = []
            current_day_memory = 0
    return output


def output_procedure(output_array):
    for element in output_array:
        print(element)


def main():
    n, m = map(int, input().split())
    output_procedure(input_procedure(n, m))


if __name__ == "__main__":
    main()
