#python 3.9
# dev : @Ziazl | santrich
#pip install pyromod
#pip install pyrogram
import os
from pyromod import listen
from pyrogram.types import Message, ReplyKeyboardMarkup
from pyrogram import Client, idle
admin = 1900060993
session_name = 'MetiwzPmBot' #session_name
api_id = 2591609
api_hash = "dbe01607cc2d434e3b94dc0a85c8c9c7"
#app hash
bot_token = "2063741967:AAGKSbtsyyGF68LS-OvKk8-MWMwbIZqXR6k"#token
app = Client(session_name=session_name, api_hash=api_hash, api_id=api_id, bot_token=bot_token) #dont touch
kybo = ReplyKeyboardMarkup( [[ "pv"], ["Account"],], resize_keyboard=True,)       
kyb = ReplyKeyboardMarkup( [[ "cancel"],],resize_keyboard=True,)       
@app.on_message()
async def xx(client,message):
    count = 0
    text = message.text
    fromid= message.from_user.id    
    if text == "/start":
        await message.reply("Hi dear Please connect me with [pv]",message.chat.id,reply_markup=kybo)
    if text == "Account":
        first = message.from_user.first_name
        last = message.from_user.last_name
        stat = message.from_user.status
        ssr_= await app.get_profile_photos(fromid) 
        user = message.from_user.username
        await message.reply("first name: %s \n last name: %s \n UserId : %i \n Username : @%s \n status : %s" % (first, last,fromid,user,stat),message.chat.id)
    send_to = admin
    if message.text == "pv":
        if message.text != 'cancel':
             x = await app.ask(message.chat.id, "please send me your message", reply_markup=kyb)        
             await app.send_message(send_to,'new message ->')        
             await message.reply("your message was send!",reply_markup=kybo)
             msgid= x.message_id              
             await app.forward_messages(send_to,message.chat.id,msgid )
    if message.reply_to_message:
         reply = message.reply_to_message.forward_from.id
         await app.send_message(reply,"answer : %s " % message.text)   
app.start(), print(f"The Bot Was Runned !"), idle(), app.stop()