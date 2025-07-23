
from pyrogram import Client, filters
from pyrogram.types import Message

api_id = 25432213
api_hash = "dd11cd26b29c5799ada5650afbabb4fc"
bot_token = "7544906726:AAGHcZ9MxezYctpSzbTfwpHfIYJpyitW0Cs"

channel_username = "@darkmine_Uzz"

app = Client("ReaksiyaBot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.channel & filters.chat(channel_username))
async def react_to_new_post(client, message: Message):
    await message.react(["🔥", "💯", "🤩", "👍", "❤️"])

app.run()
