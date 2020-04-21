{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "What is the fastest programming language among these ? \n",
      " a) Java \n",
      " b) Python \n",
      " c) C++\n",
      "\n",
      "Your Answer : a\n",
      "\n",
      "Tensorflow is a module of ? \n",
      " a) Java \n",
      " b) Python \n",
      " c) C++\n",
      "\n",
      "Your Answer : x\n",
      "\n",
      "Suitable language for android deevelopment ? \n",
      " a) Java \n",
      " b) Python \n",
      " c) C++\n",
      "\n",
      "Your Answer : c\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "You got 0 out of 3 correct.\n"
     ]
    }
   ],
   "source": [
    "class Question:\n",
    "    def __init__(self, prompt, answer):\n",
    "        self.prompt = prompt\n",
    "        self.answer = answer\n",
    "\n",
    "#@Author : Sudip Mitra\n",
    "#E-mail : sudipmitraonline@gmail.com\n",
    "\n",
    "question_prompts = [\n",
    "    \"What is the fastest programming language among these ? \\n a) Java \\n b) Python \\n c) C++\\n\\nYour Answer :\",\n",
    "    \"\\nTensorflow is a module of ? \\n a) Java \\n b) Python \\n c) C++\\n\\nYour Answer :\",\n",
    "    \"\\nSuitable language for android deevelopment ? \\n a) Java \\n b) Python \\n c) C++\\n\\nYour Answer :\",\n",
    "]\n",
    "\n",
    "questions = [\n",
    "    Question(question_prompts[0],\"c\"),\n",
    "    Question(question_prompts[1],\"b\"),\n",
    "    Question(question_prompts[2],\"a\"),\n",
    "]\n",
    "\n",
    "def run_test(questions):\n",
    "    score = 0\n",
    "    for question in questions:\n",
    "        answer = input(question.prompt)\n",
    "        if answer == question.answer :\n",
    "            score += 1\n",
    "    print(\"\\nYou got \" + str(score) + \" out of \" + str(len(questions)) + \" correct.\")\n",
    "run_test(questions)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
