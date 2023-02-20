from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message

from search_multiple_artists import search_lyrics_artist1, search_lyrics_artist2

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
        results_artist1 = search_lyrics_artist1(inline_query.query)
        results_artist2 = search_lyrics_artist2(inline_query.query)
        items = []
        if results_artist1 != None:
            items.append(types.InlineQueryResultArticle(
                id=1, title='Artist1',
                thumb_url='url1',
                description=results_artist1,
                input_message_content=types.InputTextMessageContent(
                    message_text=results_artist1)
                ))
        else:
            pass
        if results_artist2 != None:
            items.append(types.InlineQueryResultArticle(
                id=2, title='Artist2',
                thumb_url='url2',
                description=results_artist2,
                input_message_content=types.InputTextMessageContent(
                    message_text=results_artist2)
                ))
        else:
            pass
        await bot.answer_inline_query(inline_query.id, results=items)
    else:
        pass


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
