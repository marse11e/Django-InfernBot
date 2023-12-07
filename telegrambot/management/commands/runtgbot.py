from django.core.management.base import BaseCommand
from telegrambot.bot import run_bot  # Подставьте ваш путь к функции запуска бота

class Command(BaseCommand):
    help = 'Run the Telegram bot'

    def handle(self, *args, **options):
        run_bot()
