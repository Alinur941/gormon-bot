from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.faq import FAQ


def main_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📝 Зарегистрироваться на забег", callback_data="reg_start")],
        [InlineKeyboardButton(text="❓ Частые вопросы", callback_data="faq_list")],
        [InlineKeyboardButton(text="📅 Ближайшие события", callback_data="events")],
        [InlineKeyboardButton(text="📞 Связаться с организатором", callback_data="contact")],
    ])


def faq_menu() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text=item["question"], callback_data=f"faq_{item['id']}")]
        for item in FAQ
    ]
    buttons.append([InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def back_to_faq() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Назад к вопросам", callback_data="faq_list")],
        [InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")],
    ])


def back_to_main() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")],
    ])


def reg_step_1() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Открыл сайт, что дальше?", callback_data="reg_step_2")],
        [InlineKeyboardButton(text="🔗 Перейти на сайт", url="https://nomadsport.net")],
        [InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")],
    ])


def reg_step_2() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Выбрал дистанцию", callback_data="reg_step_3")],
        [InlineKeyboardButton(text="📏 Какие дистанции есть?", callback_data="faq_distances")],
        [InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")],
    ])


def reg_step_3() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Заполнил анкету", callback_data="reg_step_4")],
        [InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")],
    ])


def reg_step_4() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Оплатил!", callback_data="reg_step_5")],
        [InlineKeyboardButton(text="💰 Сколько стоит?", callback_data="faq_price")],
        [InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")],
    ])


def reg_done() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📋 Проверить себя в списке", url="https://nomadsport.net")],
        [InlineKeyboardButton(text="❓ Ещё вопросы", callback_data="faq_list")],
        [InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")],
    ])
