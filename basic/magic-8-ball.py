import random

affirmative_responses = [
    "It is certain",
    "Without a doubt",
    "You may rely on it",
    "Yes – definitely",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes"
]

not_conclusive_responses = [
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again"
]

negative_responses = [
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful"
]

responses = affirmative_responses + not_conclusive_responses + negative_responses

def magic_8_ball():
    question = input("Ask the Magic 8 Ball a question: ")
    print("Thinking...\n")
    print(random.choice(responses))

magic_8_ball()