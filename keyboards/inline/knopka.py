# import requests
from aiogram.types import   InlineKeyboardButton, InlineKeyboardMarkup

import data.config as cfg

btnUrlChanel = InlineKeyboardButton(text="Bizning kanal", url=cfg.CHANEL_URL)

channel_menu = InlineKeyboardMarkup(row_width=1).insert(btnUrlChanel)
