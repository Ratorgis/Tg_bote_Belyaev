from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

main_kb = ReplyKeyboardMarkup(
    keyboard = [ 
        [
            KeyboardButton(text='Биография'),
            KeyboardButton(text='Текст Второй')
        ],
        [
            KeyboardButton(text='Текст Третий'),
            KeyboardButton(text='Текст Четвертый')
        ],
        [
            KeyboardButton(text='Пройти Тест')
        ]
    ],
    resize_keyboard=True
)

questions = [
    {
        "question": "Какой цвет у неба?",
        "answers": ["Синий", "Зеленый", "Красный", "Желтый"],
        "correct": 0
    },
    {
        "question": "Сосал ?",
        "answers": ["Нет", "Да"],
        "correct": 1
    }
]

def generate_question_keyboard(question_data):
    keyboard = InlineKeyboardBuilder()
    for idx, answer in enumerate(question_data["answers"]):
        keyboard.button(
            text=answer,
            callback_data=f"answer_{idx}"
        )
    keyboard.adjust(2)  
    return keyboard.as_markup()
