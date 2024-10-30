# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext


# kode import
from bot.management.commands.loader import dp
from bot.management.commands.utils import texts, buttons

# add import
from asyncio import create_task


async def success_handler_task(message: Message, state: FSMContext):
    """
    ----
    """
    
    await message.answer(texts.DID_SUCCESS, reply_markup=buttons.BACK_BUTTON)

    await state.finish()

@dp.message_handler(lambda message: message.text.startswith(buttons.YES), state='*')
async def success_handler(message: Message, state: FSMContext):
    await create_task(success_handler_task(message, state))
    
