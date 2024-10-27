# aiogram import 
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext

# kode import
from bot.management.commands.loader import dp
from bot.management.commands.utils import texts, buttons
from bot.management.commands.state import Passenger
from main.models import Location

# add import
from asyncio import create_task




async def passerger_count_task(message: Message, state: FSMContext):
    
    """
    Yo'lovchilar sonini olivchi funksiya
    """
    
    locations = Location.objects.all()
    
    location_buttons = [[KeyboardButton(location.name)] for location in locations] 

    location_button = ReplyKeyboardMarkup(
        keyboard=location_buttons,
        resize_keyboard=True,
        one_time_keyboard=True
    )
    
    count = message.text

    await state.update_data({
        'count': count
    })
    
    await message.answer(texts.PASSENGER_LOCATION_MESSAGE, reply_markup=location_button)
    
    await Passenger.location.set()    

    
@dp.message_handler(content_types=['text'], state=Passenger.count)
async def passerger_count(message: Message, state: FSMContext):
    await create_task(passerger_count_task(message, state))