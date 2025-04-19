from aiogram.types import Message
from aiogram import Router, types, F
from aiogram.filters import CommandStart
from Kbds import reply

user_data = dict()

user_router = Router()

File_1 = '/root/bio.md2'
File_2 = '/root/car.md2'
File_3 = '/root/rew.md2'
File_4 = '/root/sci.md2'

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


@user_router.message(lambda message: message.text == 'Карьера')
async def first_text(message: Message):
    with open(File_2, 'r', encoding='utf-8') as file:
        file_content = file.read()
    await message.answer(file_content)

@user_router.message(lambda message: message.text == 'Труды и Награды')
async def first_text(message: Message):
    with open(File_3, 'r', encoding='utf-8') as file:
        file_content = file.read()
    await message.answer(file_content)

@user_router.message(lambda message: message.text == 'Достижения и Направления')
async def first_text(message: Message):
    with open(File_4, 'r', encoding='utf-8') as file:
        file_content = file.read()
    await message.answer(file_content)

@user_router.message(lambda message: message.text == 'Пройти Тест')
async def first_text(message: Message):
    user_id = message.from_user.id

    user_data[user_id] = {
        'current_question_index': 0,
        'correct_answers': 0
    }
    question_data = reply.questions[0]
    keyboard = reply.generate_keyboard(question_data)

    await message.answer(
        text=question_data["question"],
        reply_markup=keyboard
    )


@user_router.callback_query(F.data.startswith('answer_'))
async def handle_answer(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id

    user_info = user_data[user_id]
    current_question_index = user_info["current_question_index"]
    question_data = reply.questions[current_question_index]

    selected_answer_idx = int(callback_query.data.split("_")[1])
    correct_answer_idx = question_data["correct"]

    if selected_answer_idx == correct_answer_idx:
        user_info["correct_answers"] += 1

        if current_question_index + 1 < len(reply.questions):
            user_info["current_question_index"] += 1
            next_question_data = reply.questions[user_info["current_question_index"]]
            keyboard = reply.generate_keyboard(next_question_data)

            await callback_query.message.edit_text(
                text=next_question_data["question"],
                reply_markup=keyboard
            )
        else:
            await callback_query.message.edit_text(
                text=f"Тест завершён!\n"
                     f"Правильных ответов: {user_info['correct_answers']} из {len(reply.questions)}."
            )
            del user_data[user_id] 

    else:
        correct_answer_text = question_data["answers"][correct_answer_idx]
        await callback_query.message.edit_text(
            text=f"Неверно!\n"
                 f"Правильный ответ: {correct_answer_text}."
        )
        del user_data[user_id]  

    await callback_query.answer()


