import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("__**Salam mən tağ botuyam**, Məni qruplara əlavə edərək qrup üzvlərini tağ edə bilərsən 👻\nBas **/help** kömək al__\n\n Sahibimlə əlaqə : @ABISHOV_27",
                    buttons=(
                      [Button.url('📣 Qrupumuz', 'https://t.me/darkchatgroup12'),
                      Button.url('📦 Digər mənbələr', 'https://t.me/YusifinBiosu')]
                    ),
                    link_preview=False
                   )
@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "**Kömək Menyusu**\n\nTağ etmə qaydası: /mentionall\n__Tağ etmə səbəbiniz.__\n`Nümunə: /mentionall Səsliyə gəlin!`\n__Bot hərkəsi Səsliyə gəlin deyərək tağ edəcək.Bütün üzvlər aiddir__.\n\nSahib [ @ABISHOV_27 ]"
  await event.reply(helptext,
                    buttons=(
                      [Button.url('📣 Qrupumuz', 'https://t.me/darkchatgroup12'),
                      Button.url('📦 Digər mənbələr', 'https://t.me/YusifinBiosu')]
                    ),
                    link_preview=False
                   )
  
@client.on(events.NewMessage(pattern="^/mentionall ?(.*)"))
async def mentionall(event):
  if event.is_private:
    return await event.respond("__Bu əmri yalnızca qrup və kanallarda istifadə edə bilərsiniz!__")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("__Sadəcə adminlər bəhs edə bilərlər!__")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Əvvəlki mesajlara tağ edə bilmirəm! (Qrupa əlavə edilməmişdən əvvəlki mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Give me one argument!__")
  else:
    return await event.respond("__Bir mesaja yanıt verin və ya tağ üçün səbəb yazın!__")
  
  if mode == "text_on_cmd":
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  if mode == "text_on_reply":
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
print(">> BOT STARTED <<")
client.run_until_disconnected()
