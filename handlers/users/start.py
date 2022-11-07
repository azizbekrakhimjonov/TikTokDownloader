
import sqlite3

import requests
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

import keyboards.inline.knopka as nav
from data.config import BOT_TOKEN
from handlers.users.downloader import run
from loader import dp, bot


conn = sqlite3.connect('db.db')
cur = conn.cursor()
cur.execute(
    'CREATE TABLE IF NOT EXISTS users(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,user_name TEXT,user_id INTEGER);')
conn.commit()


def add_sql(user_name, user_id):
    cur.execute('INSERT INTO users(user_name, user_id) VALUES(?, ?)', (user_name, user_id))
    conn.commit()


def check_sub_chanel(chat_member):
    return chat_member['status'] != 'left'


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if check_sub_chanel(await bot.get_chat_member(chat_id=-1001563560957, user_id=message.from_user.id)):
        await message.answer(
            f"Salom {f'[{message.from_user.first_name}]({message.from_user.url})'}\n🇺🇿Men TikTokdan video yuklovchi botman🇺🇿\n🇺🇸I am a video uploader from TikTok🇺🇸\n🇷🇺Я загружаю видео из TikTok🇷🇺",
            parse_mode='MarkdownV2')
        if message.from_user.id not in [x[0] for x in cur.execute('SELECT user_id FROM users;').fetchall()]:
            add_sql(message.from_user.first_name, message.from_user.id)
        run()
    else:
        if message.from_user.id not in [x[0] for x in cur.execute('SELECT user_id FROM users;').fetchall()]:
            add_sql(message.from_user.full_name, message.from_user.id)
        await message.answer(
            f"Hurmatli {f'[{message.from_user.first_name}]({message.from_user.url})'} kanalimizga azo emassiz kanalga obuna bo'ling",
            reply_markup=nav.channel_menu, parse_mode='MarkdownV2')
        await message.delete()
@dp.message_handler(commands=['Usrers'])
async def users(message: types.Message):
    for ret in cur.execute('SELECT * FROM users').fetchall():
        n = []
        n.append(ret[0])
    await message.answer(f'Foydalanuvchilar soni {n[0]}taga yetdi')


@dp.message_handler(commands=['add_reklama'])
async def add_reklama(message: types.Message):
    await message.answer("Textni kiriting: ")
    @dp.message_handler(content_types=['text'])
    async def add_reklama_id(message: types.Message):
        for ret in cur.execute('SELECT * FROM users').fetchall():
            txt=message.text
            API_LINK = f'https://api.telegram.org/bot{BOT_TOKEN}'
            updates = requests.get(API_LINK + '/getUpdates?offset=-1').json()
            send_message = requests.get(API_LINK + f'/sendMessage?chat_id={ret[2]}&text={txt}')
