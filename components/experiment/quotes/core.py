# -*- coding: utf-8 -*-
import random


def generate_tom_lehrer_quote():
    quotes = [
        "Life is like a sewer. What you get out of it depends on what you put into it.",
        "I know that there are people who do not love their fellow man, and I hate people like that!",
        "Be prepared to revise any system, scrap any method, abandon any theory, if the success of the job requires it.",
        "I feel that if a person has problems communicating the very least he can do is to shut up.",
        "It is a sobering thought that when Mozart was my age he had been dead for two years.",
    ]
    return random.choice(quotes)


def generate_douglas_adams_quote():
    quotes = [
        "I love deadlines. I like the whooshing sound they make as they fly by.",
        "I may not have gone where I intended to go, but I think I have ended up where I needed to be.",
        "I refuse to answer that question on the grounds that I don't know the answer.",
        "The answer to the ultimate question of life, the universe, and everything is 42.",
        "Time is an illusion. Lunchtime doubly so.",
    ]
    return random.choice(quotes)
