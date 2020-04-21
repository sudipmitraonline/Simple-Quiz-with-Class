class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

#@Author : Sudip Mitra
#E-mail : sudipmitraonline@gmail.com

question_prompts = [
    "What is the fastest programming language among these ? \n a) Java \n b) Python \n c) C++\n\nYour Answer :",
    "\nTensorflow is a module of ? \n a) Java \n b) Python \n c) C++\n\nYour Answer :",
    "\nSuitable language for android deevelopment ? \n a) Java \n b) Python \n c) C++\n\nYour Answer :",
]

questions = [
    Question(question_prompts[0],"c"),
    Question(question_prompts[1],"b"),
    Question(question_prompts[2],"a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer :
            score += 1
    print("\nYou got " + str(score) + " out of " + str(len(questions)) + " correct.")
run_test(questions)
