from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message

from search_lyrics import search_lyrics
import config


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
