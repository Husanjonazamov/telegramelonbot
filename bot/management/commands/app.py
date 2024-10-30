# aiogram import
from aiogram import executor

# kode import
from .loader import dp, bot
from bot.management.commands.utils.env import ADMIN
from bot.management.commands.handlers.notice.notece_send import dynamic_notice_send_task
from bot.management.commands.handlers.notice.notice_funk import client

# add import
import asyncio
from typing import Any
from django.core.management.base import BaseCommand

from . import handlers 




class Command(BaseCommand):
    help = "run bot file"
    
    def handle(self, *args: Any, **options: Any):
        async def on_startup(dp):
            await bot.send_message(ADMIN, "Bot ishga tushdi!")

            asyncio.create_task(run_client_with_task())

        executor.start_polling(dp, skip_updates=False, on_startup=on_startup)


async def run_client_with_task():
    async with client:
        await client.start()
        print("Client started...")

        await asyncio.gather(
            dynamic_notice_send_task(),
            client.run_until_disconnected()
        )