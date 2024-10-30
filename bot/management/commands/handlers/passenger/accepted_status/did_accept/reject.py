# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext


# kode import
from bot.management.commands.loader import dp, bot
from bot.management.commands.utils.env import CHANNEL_ID
from bot.management.commands.utils import texts, buttons
from bot.management.commands.handlers.passenger.accepted_status.cencel_func import parse_text

# add import
from asyncio import create_task


async def success_handler_task(message: Message, state: FSMContext):
    """
    ----
    """
    
    data = await state.get_data()
    username = message.from_user.username
    phone_number = data.get('phone_number')
    count = data.get('count') 
    location = data.get('location') 
    
    user_id = message.from_user.id    
    
    await message.delete()

    await bot.send_message(
        chat_id=CHANNEL_ID,
        text=texts.cancel_pesserger_admin(
            username=username,
            count=count,
            location=location,
            phone_number=phone_number
        ),
        reply_markup=buttons.passerger_success_admin(user_id)  
    )
    await message.answer(texts.SUCCES_PESSERGER, reply_markup=buttons.BACK_BUTTON)

    await state.finish()

@dp.message_handler(lambda message: message.text.startswith(buttons.NO), state='*')
async def success_handler(message: Message, state: FSMContext):
    await create_task(success_handler_task(message, state))
    
