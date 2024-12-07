from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

async def inline_kb():
    inline_kb = InlineKeyboardBuilder()
    inline_kb.add(InlineKeyboardButton(text="камень", callback_data='stone'),
                  InlineKeyboardButton(text="ножница", callback_data='scissor'),
                  InlineKeyboardButton(text="бумага", callback_data='paper'))
    return inline_kb.adjust(1).as_markup()