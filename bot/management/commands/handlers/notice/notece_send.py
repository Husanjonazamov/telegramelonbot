# model import
from main.models import Notice

# kode import
from .notice_funk import client, last_notice_data

# add import
from asgiref.sync import sync_to_async
from asyncio import sleep



async def dynamic_notice_send_task():
    async with client:
        await client.start()
        print("Client started...")

        while True:
            notices = await sync_to_async(list)(Notice.objects.all())
            for notice in notices:
                if notice.id not in last_notice_data or last_notice_data[notice.id]["description"] != notice.description:
                    last_notice_data[notice.id] = {
                        "description": notice.description,
                        "interval": notice.interval
                    }
            await sleep(5)

