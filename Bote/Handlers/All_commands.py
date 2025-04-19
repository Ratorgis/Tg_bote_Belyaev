from aiogram.types import Message
from aiogram.types.callback_query import CallbackQuery
from aiogram import Router, types
from aiogram.filters import CommandStart
import aiogram.utils.markdown as executor
from Kbds import reply
import random

user_data = dict()

user_router = Router()

File_1 = ''
File_2 = ''
File_3 = ''
File_4 = ''

@user_router.message(CommandStart())
async def get_start(message: Message):
    await message.answer(
        "Привет! Я - бот про биографию Спартака Тимофеевича Беляева",
        reply_markup = reply.main_kb
    )

@user_router.message(lambda message: message.text == 'Биография')
async def first_text(message: Message):
    with open(File_1, 'r', encoding='utf-8') as file:
        file_content = file.read()
    await message.answer(file_content)


@user_router.message(lambda message: message.text == 'Текст Второй')
async def first_text(message: Message):
    with open(File_2, 'r', encoding='utf-8') as file:
        file_content = file.read()
    await message.answer(file_content)

@user_router.message(lambda message: message.text == 'Текст Третий')
async def first_text(message: Message):
    with open(File_3, 'r', encoding='utf-8') as file:
        file_content = file.read()
    await message.answer(file_content)

@user_router.message(lambda message: message.text == 'Текст Четвертый')
async def first_text(message: Message):
    with open(File_4, 'r', encoding='utf-8') as file:
        file_content = file.read()
    await message.answer(file_content)

@user_router.message(lambda message: message.text == 'Пройти Тест')
async def first_text(message: Message):
    user_id = message.from_user.id
    question_data = random.choice(reply.questions)
    user_data[user_id] = question_data
    await message.answer(
        text = question_data['question'],
        reply_markup=reply.generate_question_keyboard(question_data)
    )

@user_router.callback_query(lambda c: c.data.startswith("answer_"))
async def process_answer(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    user_data[user_id] = {
        "remaining_questions": reply.questions.copy(),  
        "correct_answers": 0,
        "wrong_answers": 0
    }
    await send_next_question(user_id, types.message)

async def send_next_question(user_id, message_or_callback):
    user = user_data[user_id]

    if not user["remaining_questions"]:
        correct = user["correct_answers"]
        wrong = user["wrong_answers"]
        total = correct + wrong

        await message_or_callback.answer(
            f"Викторина завершена!\n\n"
            f"Правильных ответов: {correct}\n"
            f"Неправильных ответов: {wrong}\n"
            f"Всего вопросов: {total}"
        )
        return

    question_data = user["remaining_questions"].pop(0)
    user["current_question"] = question_data

    if isinstance(message_or_callback, types.Message):
        await message_or_callback.answer(
            text=question_data["question"],
            reply_markup = reply.generate_question_keyboard(question_data)
        )
    elif isinstance(message_or_callback, CallbackQuery):
        await message_or_callback.message.edit_text(
            text=question_data["question"],
            reply_markup = reply.generate_question_keyboard(question_data)
        )

@user_router.callback_query(lambda c: c.data.startswith("answer_"))
async def process_answer(callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    user = user_data.get(user_id)
    question_data = user.get("current_question")
    if not question_data:
        await callback_query.answer("Что-то пошло не так. Попробуйте снова.")
        return

    selected_idx = int(callback_query.data.split("_")[1])

    if selected_idx == question_data["correct"]:
        user["correct_answers"] += 1
        await callback_query.answer("Правильно!")
    else:
        user["wrong_answers"] += 1
        await callback_query.answer("Неправильно!")

    await send_next_question(user_id, callback_query)