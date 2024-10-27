import asyncio
from typing import Any
from aiogram import executor
from .loader import dp, bot

from bot.management.commands.utils.env import ADMIN

from django.core.management.base import BaseCommand
from bot.management.commands.handlers.notice.notece_send import dynamic_notice_send_task

from . import handlers

class Command(BaseCommand):
    help = "run bot file"


    def handle(self, *args: Any, **options: Any):
        async def on_startup(dp):
            await bot.send_message(ADMIN, "Bot ishga tushdi!")
            asyncio.create_task(dynamic_notice_send_task())

        executor.start_polling(dp, skip_updates=False, on_startup=on_startup)