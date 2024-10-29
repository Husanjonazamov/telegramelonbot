from telethon import TelegramClient, events
from bot.management.commands.utils import env
from main.models import Notice
from asgiref.sync import sync_to_async

    
client = TelegramClient(env.PHONE_NUMBER, env.API_ID, env.API_HASH)

chat_id = -1002259911997
last_sent = False
last_notice_data = {}



async def send_notice(notice):
    global last_sent
    await client.send_message(chat_id, notice.description)
    last_sent = True  
    
@client.on(events.NewMessage(chats=chat_id))
async def handler(event):
    global last_sent
    if not event.out and not last_sent:  
        notices = await sync_to_async(list)(Notice.objects.all())
        if notices:  
            await send_notice(notices[0]) 
    elif not event.out: 
        last_sent = False  