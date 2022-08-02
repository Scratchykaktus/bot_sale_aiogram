from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_default_commads(bot: Bot):
    return await bot.set_my_commands(
        commands=[
            BotCommand('start', 'Запуск бота'),
            BotCommand('help', 'Вывести справку'),
            BotCommand('menu', 'Показать меню'),
            BotCommand('items', 'Купить товары'),
            BotCommand('test', 'Начать тестирование'),
        ],
        scope=BotCommandScopeDefault()
    )
