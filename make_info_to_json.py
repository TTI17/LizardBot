import os, json
from aiogram.types import CallbackQuery
from aiogram import Router

#make a directory by group or member
tr = Router()
@tr.callback_query(lambda c: c.data == 'groups')
async def tracking(call: CallbackQuery)->None:
    user_dir = call.message.from_user.username
    os.mkdir(f'{user_dir}')
    with open(f'{user_dir}/groups.json', 'w') as file:
        json.dump({
            'groups': []
        }, file)