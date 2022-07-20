from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.raw.functions.bots import SetBotCommands
from pyrogram.raw.types import BotCommand, BotCommandScopeDefault
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, UserIsBlocked, MessageNotModified, PeerIdInvalid
import os
import asyncio
import time
import threading
import mdisk
import split

BOT_USERNAME = os.environ.get("BOT_USERNAME", "MdiskDownloadersBot")
BOT_NAME = os.environ.get("BOT_NAME", "Mdisk Downloader Bot")
bot_token = os.environ.get("TOKEN", "5336784270:AAHLLAdyoCKLt5_XdV_Aj1UAqHLB5b_Li1g") 
api_hash = os.environ.get("HASH", "db62aa57ef8162bb4c95d0cf81e1c09b") 
api_id = os.environ.get("ID", "7651392") 

app = Client("my_bot",api_id=api_id, api_hash=api_hash,bot_token=bot_token)

TG_SPLIT_SIZE = 2097151000

@app.on_message(filters.command(["start"]))
def echo(client, message):
       app.send_message(message.chat.id, f'**Hi 👋\n\nI Am {BOT_NAME}\n\nUse Me To Download Mdisk Link To Video\n\nSend Me The Mdisk Link Like /mdisk Link\n\nFor More Info Watch Below 👇 Turtorial Video**',
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📹 Turtorial Video",
                        url=f"https://youtu.be/VdONGctjnNk",
                    )
                ],
                [InlineKeyboardButton("📣 Update Channel", url=f"https://t.me/HindiMovieSearchBotz")],
                [
                    InlineKeyboardButton("〽️disk Search Group", url=f"https://t.me/Hindi_Movie_Search_Mdisk_Group"),
                    InlineKeyboardButton("❤️ Donate", url=f"https://t.me/DKBOTZHELP"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 Official Group", url=f"https://t.me/DK_BOTZ"
                    ),
                    InlineKeyboardButton(
                        "📣 Official Channel", url=f"https://t.me/DKBOTZ"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🌐 Source Code", url="https://t.me/Killer_XMan"
                    )
                ],
            ]
        ),
        disable_web_page_preview=False,
    ) 

@app.on_message(filters.command(["help"]))
def echo(client, message):
       app.send_message(message.chat.id, f'**Hi 👋\n\nI Am {BOT_NAME}\n\nUse Me To Download Mdisk Link To Video\n\nSend Me The Mdisk Link Like /mdisk Link\n\nFor More Info Watch Below 👇 Turtorial Video**',
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📹 Turtorial Video",
                        url=f"https://youtu.be/VdONGctjnNk",
                    )
                ],
                [InlineKeyboardButton("📣 Update Channel", url=f"https://t.me/HindiMovieSearchBotz")],
                [
                    InlineKeyboardButton("〽️disk Search Group", url=f"https://t.me/Hindi_Movie_Search_Mdisk_Group"),
                    InlineKeyboardButton("❤️ Donate", url=f"https://t.me/DKBOTZHELP"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 Official Group", url=f"https://t.me/DK_BOTZ"
                    ),
                    InlineKeyboardButton(
                        "📣 Official Channel", url=f"https://t.me/DKBOTZ"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🌐 Source Code", url="https://t.me/Killer_XMan"
                    )
                ],
            ]
        ),
        disable_web_page_preview=False,
    )
    
@app.on_message(filters.command(["tutorial"]))
def echo(client, message):
       app.send_message(message.chat.id, '**Watch This Video For More Info 👉 :- https://youtu.be/VdONGctjnNk**',
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📹 Turtorial Video",
                        url=f"https://youtu.be/VdONGctjnNk",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🌐 Source Code", url="https://t.me/Killer_XMan"
                    )
                ],
            ]
        ),
    )

def down(v,a,message,link):
    app.send_message(message.chat.id, '📥 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠....\n\n**Its Take Time Depend On Your File Size**',
     reply_markup=InlineKeyboardMarkup(
         [
             [
                 InlineKeyboardButton(
                     "📹 Turtorial Video",
                     url=f"https://youtu.be/VdONGctjnNk",
                 )
             ],
             [
                 InlineKeyboardButton(
                     "✨ Support Group", url=f"https://t.me/DK_BOTZ"
                 )
             ],
         ]
     ),
     disable_web_page_preview=False,
 )
    file = mdisk.mdow(link,v,a,message)
    #size = split.get_path_size(file)
    #if(size > 2097151000):
        #app.send_message(message.chat.id, '𝗦𝗽𝗹𝗶𝘁𝗶𝗻𝗴')
        #flist = split.split_file(file,size,file,".", TG_SPLIT_SIZE)
        #os.remove(file)
        #app.send_message(message.chat.id, '𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠',
         #reply_markup=InlineKeyboardMarkup(
             #[
                 #[
                     #InlineKeyboardButton(
                         #"📹 Turtorial Video",
                         #url=f"https://youtu.be/VdONGctjnNk",
                     #)
                 #],
                 #[
                     #InlineKeyboardButton(
                         #"✨ Support Group", url=f"https://t.me/DK_BOTZ"
                     #)
                 #],
             #]
         #),
         #disable_web_page_preview=False,
     #)
        #i = 1
        #for ele in flist:
            #app.send_document(message.chat.id,document=ele,caption=f"part {i}")
            #i = i + 1
            #os.remove(ele)
    #else:
    try:
        app.send_message(message.chat.id, '𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠')
        app.send_document(message.chat.id,document=file,caption=f"**Uploaded By @{BOT_USERNAME}**\n\n©️ @DKBOTZ And @DK_BOTZ")
        os.remove(file)


@app.on_message(filters.command(["mdisk"]))
def echo(client, message):
    try:
        link = message.text.split("mdisk ")[1]
        if "mdisk" in link:
            out = mdisk.req(link)
            app.send_message(message.chat.id, out)
            app.send_message(message.chat.id, 'Send VideoID,AudioID Like >> 2,1\n\nFor More Info Watch Below 👇 Turtorial Video',
             reply_markup=InlineKeyboardMarkup(
                 [
                     [
                         InlineKeyboardButton(
                             "📹 Turtorial Video",
                             url=f"https://youtu.be/VdONGctjnNk",
                         )
                     ],
                     [
                         InlineKeyboardButton(
                             "✨ Support Group", url=f"https://t.me/DK_BOTZ"
                         )
                     ],
                 ]
             ),
             disable_web_page_preview=False,
         )
            with open(f"{message.chat.id}.txt","w") as ci:
                ci.write(link)
    except:
        app.send_message(message.chat.id, '**Wrong Method Send /mdisk Link\n\nFor More Info Watch Below 👇 Turtorial Video**',
         reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "📹 Turtorial Video",
                         url=f"https://youtu.be/VdONGctjnNk",
                     )
                 ],
                 [
                     InlineKeyboardButton(
                         "✨ Support Group", url=f"https://t.me/DK_BOTZ"
                     )
                 ],
             ]
         ),
         disable_web_page_preview=False,
     ) 

              
@app.on_message(filters.text)
def echo(client, message):
        if os.path.exists(f"{message.chat.id}.txt"):
            with open(f"{message.chat.id}.txt","r") as li:
                link = li.read()
            link = link.split("\n")[0] 
            os.remove(f"{message.chat.id}.txt")
            ids = message.text.split(",")
            d = threading.Thread(target=lambda:down(ids[0],ids[1],message,link),daemon=True)
            d.start()
            #await down(ids[0],ids[1],message,link)
        else:
            app.send_message(message.chat.id, "**First Send Me Link With /mdisk\n\nFor More Info Watch Below 👇 Turtorial Video**",
             reply_markup=InlineKeyboardMarkup(
                 [
                     [
                         InlineKeyboardButton(
                             "📹 Turtorial Video",
                             url=f"https://youtu.be/VdONGctjnNk",
                         )
                     ],
                     [
                         InlineKeyboardButton(
                             "✨ Support Group", url=f"https://t.me/DK_BOTZ"
                         )
                     ],
                 ]
             ),
             disable_web_page_preview=False,
         ) 



app.run()
app.start()
print("\n\nMdisk Link Downloader Bot Started, Join @DKBOTZ!")
