# aiogram import
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext

# kode import
from bot.management.commands.loader import dp, bot
from bot.management.commands.utils import buttons, texts

# add import
from asyncio import create_task



async def mail_success_task(callback_query: CallbackQuery, state: FSMContext):
    parts = callback_query.data.split('_')
    
    user_id = parts[1]  
    taxi_id = callback_query.from_user.id 
    taxi_username = callback_query.from_user.username 
    current_taxi_id = callback_query.from_user.id 

    try:
        await bot.edit_message_reply_markup(
            chat_id=callback_query.message.chat.id, 
            message_id=callback_query.message.message_id, 
            reply_markup=buttons.mail_success_user(user_id, taxi_id, current_taxi_id)
        )
    except Exception as e:
        print(f"Xatolik yuz berdi: {str(e)}")

    await bot.answer_callback_query(callback_query.id, text=texts.SUCCESS_MAIL, show_alert=True)



@dp.callback_query_handler(lambda callback_query: callback_query.data and callback_query.data.startswith("mail_success_"), state="*")
async def mail_success(callback_query: CallbackQuery, state: FSMContext):
    await create_task(mail_success_task(callback_query, state))
