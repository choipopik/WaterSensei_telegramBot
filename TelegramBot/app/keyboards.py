from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Я выпил воды',)],
    [KeyboardButton(text='Профиль')],
    [KeyboardButton(text='Таблица Лидеров')]
], resize_keyboard=True, input_field_placeholder='Меню')


