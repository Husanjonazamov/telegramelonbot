# kode import
from bot.management.commands.loader import bot
from bot.management.commands.utils import env
from main.models import Notice
from asgiref.sync import sync_to_async
from asyncio import sleep
from asyncio import create_task


async def dynamic_notice_send_task():
    last_notice_data = {}  
    
    while True:
        notices = await sync_to_async(list)(Notice.objects.all())

        for notice in notices:
            if (
                notice.id not in last_notice_data or 
                last_notice_data[notice.id]["description"] != notice.description or
                last_notice_data[notice.id]["interval"] != notice.interval
            ):
                async def send_notice_periodically(notice_id, description, interval):
                    while True:
                        await bot.send_message(chat_id=env.CHANNEL_ID, text=description)
                        await sleep(interval)

                last_notice_data[notice.id] = {
                    "description": notice.description,
                    "interval": notice.interval
                }

                create_task(send_notice_periodically(notice.id, notice.description, notice.interval))

        await sleep(5)  
            
