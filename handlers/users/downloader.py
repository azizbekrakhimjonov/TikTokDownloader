from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import dp
from tiktokdownload import tk

def run():
    @dp.message_handler(Text(startswith="https://"))
    async def test(message: types.message):
        await message.answer("🇺🇿Iltimos biroz kuting...🇺🇿\n🇺🇸Please wait...🇺🇸\n🇷🇺Пожалуйста подождите...🇷🇺")
        natija = tk(message.text)
        global qoshiq
        qoshiq = natija['music']
        btn = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Musiqani yuklab olish", callback_data="www")]
            ]
        )
        await message.answer_video(natija['video'], reply_markup=btn)


    @dp.message_handler()
    async def echo(message: types.message):
        await message.delete()
        await message.answer(
            f"Salom, {message.from_user.full_name}!\n🇺🇿Men TikTokdan video yuklovchi botman🇺🇿\n🇺🇸I am a video uploader from TikTok🇺🇸\n🇷🇺Я загружаю видео из TikTok🇷🇺")


    @dp.callback_query_handler(text="www")
    async def www_call(callback_query: types.CallbackQuery):
        await callback_query.message.answer_voice(qoshiq, caption="#Music")



