from telebot import types


def get_main_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Профиль")
    button2 = types.KeyboardButton("Заметки")
    button3 = types.KeyboardButton("Создать заметку")
    button4 = types.KeyboardButton("Удалить заметку")

    keyboard.row(button1, button2)
    keyboard.row(button3, button4)

    return keyboard


def get_cancel_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_cancel = types.KeyboardButton("Отменить")
    keyboard.row(button_cancel)
    return keyboard
