from telegram import Bot
#Please install the telegram module
#pip install telegram

class Telegram_Module():
    '''
      Steps to create Bot

      1. Import the Bot class from telegram module.
      2. create an instance of the Telegram bot by passing to the 
         Bot constructor method the API ID which you have created in telegram.
      3. Using this BOT instance call the send_test_message function and invoke it
         with the Telegram Group chat ID. The group has already been created by you.
    
    '''
    def __init__(self,api_token,group_chat_id) :
        self.bot_token = api_token
        self.group_chat_id = group_chat_id
    async def send_test_message(self, message):
        
        #Create an instance of the Telegram Bot class
        bot = Bot(token=self.bot_token)#you need to the pass the BOT token ID
        await bot.send_message(chat_id=self.group_chat_id, text=message)

        
