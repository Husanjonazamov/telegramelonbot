# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from bot.management.commands.loader import dp, bot
from bot.management.commands.utils import texts, buttons
from bot.management.commands.utils.env import CHANNEL_ID

# add import
from asyncio import create_task


async def chat_handler_task(message: Message, state: FSMContext):
    """
    Gurpada foydalanuvchilar xabariga javob beruvchi funksiya
    """
    
    user_id = message.from_user.id
    print(user_id)
    
    keywords = ["pochta", "beshariqga ketaman", "farg'onaga ketaman", "fargonaga ketaman", "taxi kerak", "taksi kerak"]

    if message.text and any(keyword in message.text.lower() for keyword in keywords):
        username = message.from_user.username or "No username" 
        mail = message.text
        try:
            await bot.send_message(
                chat_id=CHANNEL_ID,
                text=texts.text_to_send(
                    username=username,
                    mail=mail
                ),
                reply_markup=buttons.group_mail_success_admin(user_id)
            )
            await message.reply(texts.MAIL_SEND_MESSAGE.format(message.from_user.first_name))
        except Exception as e:
            return

@dp.message_handler(content_types=['text'], state='*')
async def chat_handler(message: Message, state: FSMContext):
    if message.chat.type in ['group', 'supergroup']:  
        await create_task(chat_handler_task(message, state))


