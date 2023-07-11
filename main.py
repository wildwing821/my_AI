from hashlib import new
import logging,os,pathlib
import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import configparser,requests
from os import environ
import openai
import time,json
import asyncio
import pdb

openai.api_key = environ.get("OPENAI_API_KEY")

#pip install python-telegram-bot
dirpath = pathlib.Path(__file__).parent.resolve().parent.resolve()
os.chdir(dirpath)
config = configparser.ConfigParser()
config.read('config.ini')
TOKEN = config['TELEGRAM']['ACCESS_TOKEN_GPT']
new_model = "gpt-4"#"gpt-3.5-turbo"
pic_model = "davinci"
last_talk = ""

def get_translation(text):
        
        completion = openai.ChatCompletion.create(
            model=new_model,
            temperature=0.7,
            messages=[
                {
                    "role": "system",
                    "content": environ.get("OPENAI_API_SYS_MSG") or "",
                },
                {
                    "role": "user",
                    "content": text
                    
                },
            ],
        )
        t_text = (
            completion["choices"][0]
            .get("message")
            .get("content")
            .encode("utf8")
            .decode()
        )
        return t_text

# set up log
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
#print("AI model:",openai.Model.list())
def telegram_bot_sendimage(image_url,group_id, msg_id):
    data = {'chat_id': group_id, 'photo': image_url,'reply_to_message_id': msg_id}
    url = 'https://api.telegram.org/bot' + TOKEN + '/sendPhoto'
    
    response = requests.post(url, data=data)
    return response.json()

def genImage(text):
    response = openai.Image.create(
    #engine=pic_model,
    prompt=text,
    size= "512x512",
    #max_tokens=2048,
    n=1,
    
    )
    # 取得生成的圖片 URL
    
    image_url = response['data'][0]['url']
    return image_url

def start(update: Update, context: CallbackContext):
    global last_talk
    last_talk = ""
    update.message.reply_text("你好！我是基於ChatGpt的機器人。有什麼問題都可以問我，我很樂意為您服務。")

def echo(update: Update, context: CallbackContext):
    try:
        #pdb.set_trace()
        global last_talk
        message = update.message.text
        chat_id = update.message.chat.id
        message_id = update.message.message_id
        #print("Received message: %s from chat: %d" % (message, chat_id))
        
        if 'genImg:' in message:
            prompt = message.replace("genImg:", "")
            image_url = genImage(prompt)   
        elif last_talk == "" and 'genImg:' not in message:
            text = get_translation(message)
            last_talk = message + "\n\n " + text
        elif last_talk != "" and 'genImg:' not in message:
            text = get_translation(last_talk + "\n\n " + message)
            last_talk += message + "\n\n " + text
        

    except Exception as e:
            logging.error(str(e))
            text = "對不起，程式出現問題。"

    if 'genImg:' in message: 
        telegram_bot_sendimage(image_url,chat_id, message_id)       
    else:        
        update.message.reply_text(f"{text}")

async def main():
    while True:
        updater = Updater(token=TOKEN, use_context=True)

        # process message
        dp = updater.dispatcher
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
        
        # start robot and receive command
        updater.start_polling()
        updater.idle()
        await asyncio.sleep(1)



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
