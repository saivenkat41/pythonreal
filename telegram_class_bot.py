from telegram import Bot

class Telegram_Module:
    def __init__(self, api_token, group_chat_id):
        self.bot_token = api_token
        self.group_chat_id = group_chat_id

    async def send_test_message(self, message):
        # Create an instance of the telegram bot class
        bot = Bot(token=self.bot_token)
        # Send the message using the bot
        await bot.send_message(chat_id=self.group_chat_id, text=message)
