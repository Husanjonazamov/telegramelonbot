# aiogram import
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext

# kode import
from bot.management.commands.loader import dp
from bot.management.commands.utils import buttons, texts
from bot.management.commands.state import Mail
from main.models import Location

# add import
from asyncio import create_task



async def mail_handler_task(message: Message, state: FSMContext):
    """
    Foydalanuvchilar pochta sini yuboradigan funksiya
    """
    
    locations = Location.objects.all()
    
    location_buttons = [[KeyboardButton(location.name)] for location in locations] 
    location_buttons.append([KeyboardButton(text=buttons.BASE_BACK)])

    location_button = ReplyKeyboardMarkup(
        keyboard=location_buttons,
        resize_keyboard=True,
        one_time_keyboard=True
    )
    
    
    await message.answer(texts.MAIL_LOCATION, reply_markup=location_button)
    await Mail.location.set()
    
    
@dp.message_handler(
        lambda message: message.text.startswith((
            buttons.MAIL,   
        )),
        state='*')
async def mail_handler(message: Message, state: FSMContext):
    await create_task(mail_handler_task(message, state))

