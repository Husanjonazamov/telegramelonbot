# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from bot.management.commands.loader import dp
from bot.management.commands.utils import texts, buttons
from bot.management.commands.handlers.start import start_handler

# add import
from asyncio import create_task





async def back_task(message: Message, state: FSMContext):
    
    """
    asosiy ortga qaytish funksiyasi
    """

    await start_handler(message, state)
    await state.finish()

    
@dp.message_handler(
        lambda message: message.text.startswith((
            buttons.BASE_BACK,   
        )),
        state='*')
async def back(message: Message, state: FSMContext):
    await create_task(back_task(message, state))
    



