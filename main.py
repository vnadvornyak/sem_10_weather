from aiogram import Bot, Dispatcher, executor, types
from weather import weather
from dict import create_dict, find_country_name, create_list

API_TOKEN = '5689722623:AAHMZ_X-BTr2dAJNaotC_dCKRhitzUIcnMQ'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
lst = create_list()

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(
        "Привет! Сегодня мы будем выбирать страну для путешествия!\nДля этого нам нужно знать какая в них погода!\n"
        "Введи любую страну.")


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.answer(
        "Введи любую страну.")


@dp.message_handler()
async def country(message: types.Message):
    if message.text in create_list():
        await message.answer(f'{weather(find_country_name(message.text, create_dict()))}')
    else:
        await message.answer(
            'Я обязательно научусь понимать понравилась вам страна или нет,а пока могу предложить посмотреть погоду в другой стране')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
