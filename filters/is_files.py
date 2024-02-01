import re
from aiogram.filters import BaseFilter
from aiogram.types import Message


class FileCheck(BaseFilter):

    async def __call__(self, message: Message) -> bool:
        pattern_mega = re.compile(r'https://mega\.nz{1,2}/(file|folder)/\w{1,8}#[^\s]+$')
        pattern_media = re.compile(r'https://www\.mediafire\.com/file/\w{1,15}/\w+\.(zip|gts)/file')

        if pattern_mega.match(message.text) or pattern_media.match(message.text):
            return True
        else:
            await message.answer('Incorrect file url input')
            return False
