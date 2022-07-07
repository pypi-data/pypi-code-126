# hey-ailab/ailab/main.py
from ailab.answer import AnswerBot
from ailab.command import CommandParser


def main():
    args = CommandParser().get_args()
    answerbot = AnswerBot()

    if args.name:
        answerbot.print_my_name()
    elif args.age:
        answerbot.print_my_old()
