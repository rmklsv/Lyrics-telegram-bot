import re
from random import shuffle

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message

import config


def search_lyrics(text: str) -> set:
    with open('lyrics.txt', encoding='utf-8') as tasks:
        words = [word.lower() for word in text.split()]
        results = set()
        lyrics = tasks.readlines()
        for i, line in enumerate(lyrics):
            if len(words) == 1:
                if words[0] in re.sub(r'[^\w\s]', ' ', line.lower()).split():
                    if i > 0:
                        prev_line = lyrics[i-1]
                    else:
                        prev_line = ''
                    if i < len(lyrics) - 1:
                        next_line = lyrics[i+1]
                    else:
                        next_line = ''
                    if prev_line.strip() == '':
                        results.add(line.strip()
                                    + ' \n'
                                    + next_line.strip())
                    else:    
                        results.add(prev_line.strip()
                                    + ' \n'
                                    + line.strip()
                                    + ' \n'
                                    + next_line.strip())
            else:
                if re.search(r'\b'+text.lower()+r'\W', line.lower()):
                    if i > 0:
                        prev_line = lyrics[i-1]
                    else:
                        prev_line = ''
                    if i < len(lyrics) - 1:
                        next_line = lyrics[i+1]
                    else:
                        next_line = ''
                    if prev_line.strip() == '':
                        results.add(line.strip()
                                    + ' \n'
                                    + next_line.strip())
                    else:    
                        results.add(prev_line.strip()
                                    + ' \n'
                                    + line.strip()
                                    + ' \n'
                                    + next_line.strip())
        if len(results) > 0:
            if len(results) > 10:
                random_results = list(results)
                shuffle(random_results)            
                return random_results[:10]
            else:
                return results
        else:
            return []


bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Hi!\nI'll help you to chat "
                        "using lyrics. "
                        "Try me in any chat, "
                        "just type: @'botname' "
                        "and some word or phrase. "
                        "I'll find the matching lines "
                        "from the lyrics and you can "
                        "choose and send them to a chat.")


@dp.inline_handler()
async def inline_search(inline_query: types.InlineQuery):
    if len(inline_query.query) > 0:
        lyrics = search_lyrics(inline_query.query)
        results = []
        for i, lyrics_lines in enumerate(lyrics):
            results.append(types.InlineQueryResultArticle(
                id=i, title='Lyrics',
                description=lyrics_lines,
                input_message_content=types.InputTextMessageContent(
                    message_text=lyrics_lines
                )
            ))
        await bot.answer_inline_query(inline_query.id, results)
    else:
        pass


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
