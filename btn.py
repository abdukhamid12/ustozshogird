from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.row("Sherik kerak", "Ish joyi kerak")
menu.row("Hodim kerak", "Ustoz kerak")
menu.row("Shogird kerak")