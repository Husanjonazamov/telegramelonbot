# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from bot.management.commands.loader import dp
from bot.management.commands.utils import texts, buttons
from users.models import User
from asgiref.sync import sync_to_async

# add import
from asyncio import create_task




async def start_handler_task(message: Message, state: FSMContext):
    
    """
    /start, /help commandalari uchun. Botga birichi kirgan userni anilash
    va uni ro'yxatdan o'rtkazishga jo'natish yoki ro'yxatdan  o'tgan userni
    asosiy menuga o'tqazish 
    """
    
    user_id = message.from_user.id
    username = message.from_user.username
    
    user, created = await sync_to_async(User.objects.get_or_create)(
            user_id=user_id,
            username=username
        )
    
    await message.answer(texts.START_MESSAGE.format(message.from_user.first_name), reply_markup=buttons.START_BUTTON)
    

@dp.message_handler(commands=['start'], state='*')
async def start_handler(message: Message, state: FSMContext):
    await create_task(start_handler_task(message, state))