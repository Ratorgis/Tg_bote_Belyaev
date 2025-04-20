from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

main_kb = ReplyKeyboardMarkup(
    keyboard = [ 
        [
            KeyboardButton(text='Биография'),
            KeyboardButton(text='Карьера')
        ],
        [
            KeyboardButton(text='Труды и Награды'),
            KeyboardButton(text='Достижения и Направления')
        ],
        [
            KeyboardButton(text='Пройти Тест')
        ]
    ],
    resize_keyboard=True
)

questions = [
    {
        "question": "В каком году С.Т. Беляев окончил МФТИ ?",
        "answers": ["1946", "1952", "1962", "1978"],
        "correct": 1
    },
    {
        "question": "Какую должность Беляев занимал в Новосибирском государственном университете (НГУ)?",
        "answers": ["Декан", "Профессор", "Ректор"],
        "correct": 2
    },
    {
        "question": "Каокй медалью наградили Беляева в 2010 году совместно с Герардом 'т Хоофтом? ",
        "answers": ["Финберга", "Курчатова", "Ломоносова"],
        "correct": 2
    },
    {
        "question": "В каком году Беляев переехал в Новосибирский Академгородок? ",
        "answers": ["1952", "1962", "1978", "1986"],
        "correct": 1
    },
    {
        'question': 'Какой ученый оказал наибольшее влияние на Беляева во время его обучения ?',
        'answers': ['Н.Бор', 'Л.Д.Ландау', 'Г.И.Будкер'],
        'correct': 1
    },
    {
        'question': 'Какой из перечисленных орденов НЕ относится к Беляеву ?',
        'answers': ['Ленина', 'Славы', 'Красной Звезды'],
        'correct': 1
    },
    {
        'question': 'В каком учебном заведении Беляев был ректором с 1965 по 1978 год?',
        'answers': ['НГУ', 'МФТИ', 'МГУ'],
        'correct': 0
    },
    {
        'question': 'В каком году Беляев получил Золотую медаль имени Л.Д. Ландау?',
        'answers': ['1998', '2004', '2010', '2012'],
        'correct': 0
    },
]

def generate_keyboard(question_data):
    keyboard_builder = InlineKeyboardBuilder()
    for idx, answer in enumerate(question_data["answers"]):
        keyboard_builder.button(
            text=answer,
            callback_data=f"answer_{idx}"
        )
    return keyboard_builder.as_markup()
