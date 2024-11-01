import json
import datetime
from aiogram import types, Dispatcher
from parse.main import check_news_update
from aiogram.dispatcher.filters import Text


async def start_bot(message: types.Message):
    start_button = ['Все новости', 'Последние 5 новостей', 'Свежие новости']
    keyword = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyword.add(*start_button)
    await message.answer('Лента новостей', reply_markup=keyword)


async def get_all_news(message: types.Message):
    with open(r'parse\news.json', encoding='utf-8') as file:
        news_dict = json.load(file)
    for k, v in sorted(news_dict.items()):
        new = f'{datetime.datetime.fromtimestamp(v["article_date_timestamp"])}\n' \
              f'{v["article_url"]}'
        await message.answer(new)


async def get_five_news(message: types.Message):
    with open(r'parse\news.json', encoding='utf-8') as file:
        news_dict = json.load(file)

    for k, v in sorted(news_dict.items())[-5:]:
        new = f'{datetime.datetime.fromtimestamp(v["article_date_timestamp"])}\n' \
              f'{v["article_url"]}'
        await message.answer(new)


async def get_fresh_news(message: types.Message):
    fresh_news = check_news_update()

    if len(fresh_news) >= 1:
        for k, v in fresh_news.items():
            new = f'{datetime.datetime.fromtimestamp(v["article_date_timestamp"])}\n' \
                  f'{v["article_url"]}'
            await message.answer(new)
    else:
        await message.reply('Сейчас нет свежих новостей')


def register_handlers_news(dp: Dispatcher):
    dp.register_message_handler(start_bot, commands='start')
    dp.register_message_handler(get_all_news, Text(equals='Все новости'))
    dp.register_message_handler(get_five_news, Text(equals='Последние 5 новостей'))
    dp.register_message_handler(get_fresh_news, Text(equals='Свежие новости'))
