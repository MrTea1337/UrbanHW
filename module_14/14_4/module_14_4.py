from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from crud_functions import get_all_products


api = "8080940443:AAHRxDhT5XBKgGhSuS5aLJbi7-3teCgkRow"
bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

products = get_all_products()

kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='Рассчитать'), KeyboardButton(text='Информация')],
    [KeyboardButton(text='Купить')],
])

in_line_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
    InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories'),
    InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
    ]
])

in_line_kb_2 = InlineKeyboardMarkup(inline_keyboard=[
    [
    InlineKeyboardButton('Product1', callback_data='product_buying'),
    InlineKeyboardButton('Product2', callback_data='product_buying'),
    InlineKeyboardButton('Product3', callback_data='product_buying'),
    InlineKeyboardButton('Product4', callback_data='product_buying')
    ]
])

@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await  message.answer('Выберите опцию:', reply_markup=in_line_kb)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()

@dp.message_handler(text=['/start'])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb)

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories = (10 * float(data['weight'])) + (6.25 * float(data['growth'])) - (5 * float(data['age'])) + 5
    await message.answer(f'Ваша норма калорий {calories}')
    await state.finish()

@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    for title, description, price in products:
        with open('product.png', "rb") as img:
            await message.answer(f'Название: {title} | Описание: {description} | Цена: {price}')
            await message.answer_photo(img)
    await message.answer("Выерите продукт для покупки", reply_markup=in_line_kb_2)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()

@dp.message_handler()
async def all_massages(message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
