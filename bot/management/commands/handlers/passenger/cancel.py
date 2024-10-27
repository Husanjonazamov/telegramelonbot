# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from bot.management.commands.loader import dp, bot
from bot.management.commands.utils import texts, buttons
from bot.management.commands.state import Passenger
from bot.management.commands.utils.env import CHANNEL_ID

# add import
from asyncio import create_task



async def passerger_cancel_task(message: Message, state: FSMContext):
    
    """
    ---------
    """    
    
    await message.answer(texts.PASSENGER_PHONE_MESSAGE, reply_markup=buttons.PHONE)
    await Passenger.phone.set()  
    
    
    
@dp.message_handler(
        lambda message: message.text.startswith((
            buttons.CANCEL,   
        )),
        state='*')
async def passerger_cancel(message: Message, state: FSMContext):
    await create_task(passerger_cancel_task(message, state))
    
    
    
