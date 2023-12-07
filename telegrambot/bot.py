import logging
import telebot
from telebot import types
from django.conf import settings
from main.models import TelegramUser, Notes
from telegrambot.keyboards import get_main_keyboard, get_cancel_keyboard

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN, parse_mode="HTML")


@bot.message_handler(commands=["start"])
def handle_start(message):
    user = message.from_user
    telegram_user, created = TelegramUser.objects.get_or_create(user_id=user.id)
    if created:
        telegram_user.username = user.username
        telegram_user.first_name = user.first_name
        telegram_user.last_name = user.last_name
        telegram_user.language_code = user.language_code
        telegram_user.save()
    bot.reply_to(message, f"Привет, {telegram_user.get_name()}!")
    bot.send_message(
        message.chat.id, "Выберите действие:", reply_markup=get_main_keyboard()
    )


@bot.message_handler(func=lambda message: message.text == "Профиль")
def handle_profile(message):
    user = message.from_user
    telegram_user, _ = TelegramUser.objects.get_or_create(user_id=user.id)

    profile_message = (
        f"<b>ID:</b> {telegram_user.user_id}\n"
        f"<b>Имя пользователя:</b> {telegram_user.username}\n"
        f"<b>Имя:</b> {telegram_user.first_name}\n"
        f"<b>Фамилия:</b> {telegram_user.last_name}\n"
        f"<b>Код языка:</b> {telegram_user.language_code}\n"
        f"<b>Бот:</b> {telegram_user.is_bot}\n"
        f"<b>Создан:</b> {telegram_user.created_at}"
    )

    bot.reply_to(message, profile_message, reply_markup=get_main_keyboard())


@bot.message_handler(func=lambda message: message.text == "Создать заметку")
def handle_create_note(message):
    bot.send_message(
        message.chat.id, "Введите текст заметки:", reply_markup=get_cancel_keyboard()
    )
    bot.register_next_step_handler(message, process_create_note)


def process_create_note(message):
    if message.text.lower() == "отменить":
        bot.send_message(
            message.chat.id,
            "Создание заметки отменено.",
            reply_markup=get_main_keyboard(),
        )
    else:
        telegram_user, _ = TelegramUser.objects.get_or_create(
            user_id=message.from_user.id
        )
        note = Notes(user=telegram_user, text=message.text)
        note.save()
        bot.send_message(
            message.chat.id, "Заметка сохранена!", reply_markup=get_main_keyboard()
        )


def send_notes_page(chat_id, notes_page):
    if notes_page:
        notes_text = "\n\n".join([f"{note.id}. {note.text}" for note in notes_page])
        message_text = f"<b>Заметки:</b>\n{notes_text}"

        markup = types.InlineKeyboardMarkup(row_width=2)
        buttons = []

        if notes_page.has_previous():
            buttons.append(
                types.InlineKeyboardButton(
                    text="<< Назад",
                    callback_data=f"Страница {notes_page.previous_page_number()}",
                )
            )
        if notes_page.has_next():
            buttons.append(
                types.InlineKeyboardButton(
                    text="Вперед >>",
                    callback_data=f"Страница {notes_page.next_page_number()}",
                )
            )

        markup.add(*buttons)

        bot.send_message(chat_id, message_text, reply_markup=markup, parse_mode="HTML")
    else:
        bot.send_message(
            chat_id, "У вас пока нет заметок.", reply_markup=get_main_keyboard()
        )


@bot.message_handler(func=lambda message: message.text == "Заметки")
def handle_notes(message):
    user = message.from_user
    telegram_user, _ = TelegramUser.objects.get_or_create(user_id=user.id)

    notes_page = telegram_user.get_notes()

    send_notes_page(message.chat.id, notes_page)


@bot.callback_query_handler(func=lambda call: call.data.startswith("Страница "))
def handle_page_change(call):
    page_number = int(call.data.split()[1])

    user = call.from_user
    telegram_user, _ = TelegramUser.objects.get_or_create(user_id=user.id)

    notes_page = telegram_user.get_notes(page_number)

    send_notes_page(call.message.chat.id, notes_page)


@bot.message_handler(func=lambda message: message.text == "Удалить заметку")
def handle_delete_note(message):
    bot.send_message(
        message.chat.id,
        "Введите ID заметки, которую хотите удалить:",
        reply_markup=get_cancel_keyboard(),
    )
    bot.register_next_step_handler(message, process_delete_note)


def process_delete_note(message):
    if message.text.lower() == "отменить":
        bot.send_message(
            message.chat.id,
            "Удаление заметки отменено.",
            reply_markup=get_main_keyboard(),
        )
    else:
        try:
            note_id = int(message.text)
            note = Notes.objects.get(id=note_id)
            note.delete()
            bot.send_message(
                message.chat.id,
                f"Заметка с ID {note_id} удалена!",
                reply_markup=get_main_keyboard(),
            )
        except Notes.DoesNotExist:
            bot.send_message(
                message.chat.id,
                f"Заметка с ID {note_id} не найдена.",
                reply_markup=get_main_keyboard(),
            )
        except ValueError:
            bot.send_message(
                message.chat.id,
                "Введите корректный ID заметки.",
                reply_markup=get_main_keyboard(),
            )
        except Exception as e:
            bot.send_message(
                message.chat.id,
                f"Произошла ошибка при удалении заметки: {e}",
                reply_markup=get_main_keyboard(),
            )


def run_bot():
    try:
        logger.info("Бот начал работу")
        bot.polling()
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")
    finally:
        logger.info("Бот завершил работу")
