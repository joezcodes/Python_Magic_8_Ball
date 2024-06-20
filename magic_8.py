import random

answers = [
            'It is certain', 'Reply hazy, try again', 'Do not count on it',
            'It is decidedly so',	'Ask again later',	'My reply is no',
            'Without a doubt',	'Better not tell you now',	'My sources say no',
            'Yes definitely',	'Cannot predict now',	'Outlook not so good',
            'Yes! You should thank Joe for your good fortune by checking his Ko-fi out.'
]

ans1 = random.choice(answers)
question = input(f'Ask your question and hit any key:')
print(question)
print(ans1)