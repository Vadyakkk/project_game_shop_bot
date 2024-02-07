from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def genre_kb():
    kb = ReplyKeyboardMarkup(row_width=True)
    kb.add(KeyboardButton('Action'))
    kb.add(KeyboardButton('MMO'))
    kb.add(KeyboardButton('RPG'))
    return kb

