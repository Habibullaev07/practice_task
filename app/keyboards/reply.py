from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reply_kb = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Игра камень ножница бумага")],
        [KeyboardButton(text="Игра рандомайзер")]
        ], resize_keyboard=True, input_field_placeholder="Выберите какая игра вас интересует")
    
    