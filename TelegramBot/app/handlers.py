from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
"from database import get_ids"

from datetime import datetime, timedelta

import app.keyboards as kb
from database import add_user, plus_streak, get_streak, get_last_date, upd_date, break_streak, get_table

import emoji

router = Router()

current_date = datetime.now()

"id_list = get_ids()"
"print(get_ids())"

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        'Приветствую ,ученик, я твой водный сенсей. Введи команду /help для старта твоего пути водного шиноби!')


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(f"Я бот который поможет тебе выпивать необходимое количество воды! \n "
                         f"Для того чтобы начать - выполни /register,а затем сообщай мне о выпитых тобою стаканах воды, "
                         f"выполняй дневную норму и копи {emoji.emojize(':fire:')}STREAK{emoji.emojize(':fire:')}.")


@router.message(Command('register'))
async def registration(message: Message):
    add_user(message)
    await message.answer('Регистрация прошла успешно, твой путь начался!' + emoji.emojize(':flexed_biceps:'),
                         reply_markup=kb.main)


@router.message(lambda message: message.text == 'Я выпил воды')
async def process_drink(message: Message):
    chat_id = message.chat.id
    curr_streak = get_streak(chat_id)
    last_click = datetime.strptime(get_last_date(chat_id), '%Y-%m-%d')
    print(last_click)
    print(current_date - last_click)
    print()
    if (current_date - last_click) < timedelta(days=1):
        await message.reply(f'Сегодня ты выпил уже достаточно!{emoji.emojize(':sweat_droplets:')}')
        return

    if last_click == 'date':
        plus_streak(message, curr_streak)
        upd_date(message)
        await message.reply(
            f"Ты попил воды! Твой STREAK : {curr_streak + 1} {emoji.emojize(':fire:')}.")
        return

    elif (current_date - last_click) > timedelta(days=2) and curr_streak != 0:
        curr_streak = 0
        await message.answer('Твой STREAK СБРОШЕН')

    plus_streak(message, curr_streak)
    upd_date(message)
    await message.reply(
        f"Ты попил воды! Твой STREAK : {curr_streak + 1} {emoji.emojize(':fire:')}.")


@router.message(lambda message: message.text == 'Профиль')
async def show_profile(message: Message):
    chat_id = message.chat.id
    curr_streak = get_streak(chat_id)
    await message.answer(
        f"{emoji.emojize(':bust_in_silhouette:')} \n Имя: {message.chat.first_name} \n {emoji.emojize(':fire:')} STREAK x{curr_streak} {emoji.emojize(':fire:')}")


@router.message(lambda message: message.text == 'Таблица Лидеров')
async def show_leaderboard(message: Message):
    table = get_table(message)
    await message.reply(table, parse_mode='HTML')

"""@router.message_handler()
async def choose_your_dinner():
    for user in :
        await bot.send_message(chat_id = user, text = "Хей🖖 не забудь
        выбрать свой ужин сегодня", reply_markup = menu_garnish)"""


