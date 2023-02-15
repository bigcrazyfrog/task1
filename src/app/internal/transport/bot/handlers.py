from asgiref.sync import sync_to_async
from telegram import Update
from telegram.ext import ContextTypes

from app.models import UserProfile
import re


def log_errors(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            print(f'error {e}')
            raise e
    return inner


@log_errors
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await sync_to_async(UserProfile.objects.get_or_create, thread_sensitive=True)(
        telegram_id=update.message.chat_id,
    )

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Привет! \nЭто бот для записи номеров телефона "
    )


@log_errors
async def set_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        rule = re.compile(r'(^[+0-9]{1,3})*([0-9]{10,11}$)')
        number = context.args[0]

        if not rule.search(number):
            raise ValueError

        user, _ = await sync_to_async(UserProfile.objects.get_or_create, thread_sensitive=True)(
            telegram_id=update.message.chat_id,
        )

        text = "Номер перезаписан"
        if user.phone_number is None:
            text = "Номер успешно записан ✅"

        user.phone_number = number
        await sync_to_async(user.save)(update_fields=["phone_number"])

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=text
        )

    except (IndexError, ValueError):
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="❗ Введите корректный номер"
        )


@log_errors
async def me(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user, _ = await sync_to_async(UserProfile.objects.get_or_create, thread_sensitive=True)(
        telegram_id=update.message.chat_id,
    )

    number = user.phone_number
    text = f'Ваш номер {number}'

    if number is None:
        text = "Вы еще не ввели номер :з"

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text
    )
