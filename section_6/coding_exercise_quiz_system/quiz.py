def parse_questions(question):
    question_list = question.split('=')
    parsed_question = question_list[0]
    parsed_answer = question_list[1]
    return {'question': parsed_question + "=", 'answer': parsed_answer}


question_file = open('questions.txt', 'r')
questions_and_answers = [parse_questions(question.strip()) for question in question_file.readlines()]
question_file.close()

total_questions = len(questions_and_answers)
score = 0
for equation in questions_and_answers:
    question = equation["question"]
    answer = input(f"What is the answer to {question}")
    score += 1 if answer == equation["answer"] else False

answer_file = open('result.txt', 'w')
answer_file.write(f"Your final score is {score}/{total_questions}.")
answer_file.close()
