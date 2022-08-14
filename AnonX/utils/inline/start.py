from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from AnonX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥺 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ ʙᴀʙʏ 🥺",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ👀",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="sᴇᴛᴛɪɴɢs👀", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🌹ᴏᴡɴᴇʀ🌹", user_id=OWNER),
            InlineKeyboardButton(
                text="❤️sᴜᴩᴩᴏʀᴛ❤️", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥺 ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ🥺",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="👀ʜᴇʟᴩ👀", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="🌹ᴏᴡɴᴇʀ🌹", user_id=OWNER),
            InlineKeyboardButton(
                text="❤️sᴜᴩᴩᴏʀᴛ❤️", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                    text="💘sᴏᴜʀᴄᴇ💘", url=f"{config.GITHUB_REPO}"
                ),
        ],
     ]
    return buttons

