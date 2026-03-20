import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from dotenv import load_dotenv

from data.faq import FAQ
from keyboards import (
    main_menu, faq_menu, back_to_faq, back_to_main,
    reg_step_1, reg_step_2, reg_step_3, reg_step_4, reg_done,
)

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

WELCOME_TEXT = (
    "👋 Привет! Я помощник сообщества *GOrMon* 🏃‍♂️\n\n"
    "Помогу зарегистрироваться на забег и отвечу на вопросы.\n\n"
    "Выбери, что тебя интересует 👇"
)

EVENTS_TEXT = (
    "📅 *Ближайшие события GOrMon:*\n\n"
    "🏃 *Bakai Jaz Demi 2026*\n"
    "📆 12 апреля 2026\n"
    "📍 ФОК «Газпром», ул. Жайыл Баатыра, 66\n"
    "📏 5 км / 10 км / 21,1 км / Kid's Run\n\n"
    "🏃 *Business Run*\n"
    "📆 26 апреля 2026\n"
    "📍 Парк Адинай\n"
    "📏 10 км\n\n"
    "🌙 *Night Run 2026*\n"
    "📆 13 июня 2026\n"
    "📍 Аю Гранд, ул. Чокана Валиханова, 2\n"
    "📏 5 км / 10 км\n\n"
    "🔗 Все события: nomadsport.net"
)


# ─── /start ───────────────────────────────────────────────────────────────────

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(WELCOME_TEXT, parse_mode="Markdown", reply_markup=main_menu())


# ─── Main menu callback ────────────────────────────────────────────────────────

@dp.callback_query(F.data == "main_menu")
async def cb_main_menu(call: CallbackQuery):
    await call.message.edit_text(WELCOME_TEXT, parse_mode="Markdown", reply_markup=main_menu())


# ─── Events ───────────────────────────────────────────────────────────────────

@dp.callback_query(F.data == "events")
async def cb_events(call: CallbackQuery):
    await call.message.edit_text(EVENTS_TEXT, parse_mode="Markdown", reply_markup=back_to_main())


# ─── Contact ──────────────────────────────────────────────────────────────────

@dp.callback_query(F.data == "contact")
async def cb_contact(call: CallbackQuery):
    text = (
        "📞 *Связаться с организаторами GOrMon:*\n\n"
        "Instagram: @nomadsport\n"
        "Сайт: nomadsport.net\n\n"
        "По вопросам регистрации — пишите прямо сюда, постараемся помочь!"
    )
    await call.message.edit_text(text, parse_mode="Markdown", reply_markup=back_to_main())


# ─── FAQ ──────────────────────────────────────────────────────────────────────

@dp.callback_query(F.data == "faq_list")
async def cb_faq_list(call: CallbackQuery):
    await call.message.edit_text(
        "❓ *Частые вопросы*\n\nВыбери интересующий вопрос:",
        parse_mode="Markdown",
        reply_markup=faq_menu()
    )


@dp.callback_query(F.data.startswith("faq_"))
async def cb_faq_item(call: CallbackQuery):
    faq_id = call.data[4:]  # strip "faq_"
    item = next((f for f in FAQ if f["id"] == faq_id), None)
    if item:
        await call.message.edit_text(
            f"*{item['question']}*\n\n{item['answer']}",
            parse_mode="Markdown",
            reply_markup=back_to_faq()
        )
    else:
        await call.answer("Вопрос не найден")


# ─── Registration flow ────────────────────────────────────────────────────────

@dp.callback_query(F.data == "reg_start")
async def cb_reg_start(call: CallbackQuery):
    text = (
        "📝 *Регистрация на забег — шаг 1 из 4*\n\n"
        "Открой официальный сайт *nomadsport.net* и перейди на страницу нужного события.\n\n"
        "👇 Нажми кнопку ниже чтобы перейти на сайт:"
    )
    await call.message.edit_text(text, parse_mode="Markdown", reply_markup=reg_step_1())


@dp.callback_query(F.data == "reg_step_2")
async def cb_reg_step_2(call: CallbackQuery):
    text = (
        "📝 *Регистрация — шаг 2 из 4*\n\n"
        "На странице события выбери дистанцию которая тебе подходит:\n\n"
        "• 5 км (от 14 лет)\n"
        "• 10 км (от 16 лет)\n"
        "• 21,1 км — полумарафон (от 18 лет)\n"
        "• Kid's Run — для детей 3–13 лет\n\n"
        "Нажми кнопку *«Регистрация»* рядом с выбранной дистанцией."
    )
    await call.message.edit_text(text, parse_mode="Markdown", reply_markup=reg_step_2())


@dp.callback_query(F.data == "reg_step_3")
async def cb_reg_step_3(call: CallbackQuery):
    text = (
        "📝 *Регистрация — шаг 3 из 4*\n\n"
        "Заполни анкету участника:\n\n"
        "✏️ Имя и фамилия\n"
        "✏️ Дата рождения\n"
        "✏️ Пол\n"
        "✏️ Контактные данные\n\n"
        "Заполни все поля и нажми «Далее» или «Оплатить»."
    )
    await call.message.edit_text(text, parse_mode="Markdown", reply_markup=reg_step_3())


@dp.callback_query(F.data == "reg_step_4")
async def cb_reg_step_4(call: CallbackQuery):
    text = (
        "📝 *Регистрация — шаг 4 из 4*\n\n"
        "Оплати стартовый взнос удобным способом онлайн.\n\n"
        "⚠️ Подтверждение платежа может занять до *24 часов*.\n"
        "После этого твоё имя появится в списке участников."
    )
    await call.message.edit_text(text, parse_mode="Markdown", reply_markup=reg_step_4())


@dp.callback_query(F.data == "reg_step_5")
async def cb_reg_done(call: CallbackQuery):
    text = (
        "🎉 *Отлично! Регистрация завершена!*\n\n"
        "Проверь своё имя в списке участников на сайте nomadsport.net.\n\n"
        "Если имя не появилось в течение 24 часов после оплаты — "
        "обратитесь к организаторам.\n\n"
        "До встречи на старте! 🏃‍♂️💨"
    )
    await call.message.edit_text(text, parse_mode="Markdown", reply_markup=reg_done())


# ─── Unknown messages ─────────────────────────────────────────────────────────

@dp.message()
async def unknown_message(message: Message):
    await message.answer(
        "Используй меню ниже 👇",
        reply_markup=main_menu()
    )


# ─── Run ──────────────────────────────────────────────────────────────────────

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
