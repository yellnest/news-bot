from aiogram.utils import executor
from create_bot import dp

print('Если бот до сих пор тупит, то проблемы в коде')


async def on_startup(_):
    print('Бот вышел в онлайн')


from news import all_news

all_news.register_handlers_news(dp)

executor.start_polling(dp, on_startup=on_startup)
