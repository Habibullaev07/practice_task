import random

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from app.keyboards.reply import reply_kb
from app.keyboards.inline import inline_kb

game_1_router = Router()

choices = ['stone', 'scissor', 'paper']

@game_1_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Здравствуйте! Выберите игру, которая вас интересует:", reply_markup=reply_kb)

@game_1_router.message(F.text.lower() == "игра камень ножница бумага")
async def rock_paper_scissor_game(message: Message):
    await message.answer("Выберите один из трех вариантов:", reply_markup=await inline_kb())

@game_1_router.callback_query(F.data.in_({'stone', 'scissor', 'paper'}))
async def play_game(callback: CallbackQuery):
    user_choice = callback.data
    bot_choice = random.choice(choices)
    
    await callback.answer("Вы выбрали")

    if user_choice == bot_choice:
        result = "Ничья! Мы оба выбрали одно и то же."
    elif (user_choice == "stone" and bot_choice == "scissor") or \
         (user_choice == "scissor" and bot_choice == "paper") or \
         (user_choice == "paper" and bot_choice == "stone"):
        result = "Вы выиграли"
    else:
        result = "Вы проиграли!"

    await callback.message.edit_text(result)
