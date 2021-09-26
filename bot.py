#jokerpluginn - @jokisback #
from telethon.tl.types import ChannelParticipantsAdmins as cp
from userbot import CMD_HELP, bot
from userbot.events import register as r
from userbot.cmdhelp import CmdHelp 
from time import sleep

@r(outgoing=True, pattern="^.all(?: |$)(.*)")
async def _(q):
	if q.fwd_from:
		return

	if q.pattern_match.group(1):
		seasons = q.pattern_match.group(1)
	else:
		seasons = ""

	chat = await q.get_input_chat()
	a_=0
	await q.delete()
	async for i in bot.iter_participants(chat):
		if a_ == 5000:
			break
		a_+=1
		await q.client.send_message(q.chat_id, "[{}](tg://user?id={}) {}".format(i.first_name, i.id, seasons))
		sleep(4)


@r(outgoing=True, pattern="^.alladmin(?: |$)(.*)")
async def _(q):
	if q.fwd_from:
		return
	

	if q.pattern_match.group(1):
		seasons = q.pattern_match.group(1)
	else:
		seasons = ""

	chat = await q.get_input_chat()
	a_=0
	await q.delete()
	async for i in bot.iter_participants(chat, filter=cp):
		if a_ == 5000:
			break
		a_+=1
		await q.client.send_message(q.chat_id, "[{}](tg://user?id={}) {}".format(i.first_name, i.id, seasons))
		sleep(4)

Help = CmdHelp('all')
Help.add_command('all <sebep>', None, 'Gruptaki kullanıcıları etiketler ')
Help.add_command('alladmin <sebep>', None, 'Tüm adminleri etiketler')
Help.add_info('[𝙅𝙊𝙆](https://t.me/jokisback) tarafından [𝘼𝙎𝙀𝙉𝘼](https://t.me/asenauserbot) için yapıldı')
Help.add()	