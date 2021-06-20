# برای اولین بار در تلگرام
# Coded by @doctor_phoenix
from telethon.sync import TelegramClient
from telethon import functions, types
from os import system

# Color
class color :
	red = '\033[91m'
	green = '\033[92m'
	under = '\033[0m'
	cyan = '\033[96m'
	yellow = '\033[93m'
	blue = '\033[94m'

api_id = 6998686 # Api id
api_hash = "185254b169c059babc307e789625ed3e" # Api hash

def clear():
	try:
		system('clear')
	except:
		system('cls')

clear()
print(color.green+''' ____  _____ ____   ___  ____ _____ _____ ____    |  _ \| ____|  _ \ / _ \|  _ \_   _| ____|  _ \\'''+color.under+'''
| |_) |  _| | |_) | | | | |_) || | |  _| | |_) |  |  _ <| |___|  __/| |_| |  _ < | | | |___|  _ <'''+color.red+'''
|_| \_\_____|_|    \___/|_| \_\|_| |_____|_| \_\\''')
print(color.green+"\n==> "+color.yellow+"Telegram reporter script")
print(color.green+">>> "+color.red+"Coded by "+color.blue+"dr.phoenix")
print(color.green+">>> "+color.red+"Github : "+color.blue+"https://github.com/DRPH03NIX")
print(color.green+">>> "+color.red+"Telegram : "+color.blue+"https://t.me/doctor_phoenix\n")
username = input(color.green+"[+] "+color.cyan+"Enter channel or group username : "+color.yellow)
username = username.replace('@', '')
message_id = input(color.green+"[+] "+color.cyan+"Enter message id : "+color.yellow)
tread = input(color.green+"[+] "+color.cyan+"Enter number of reports : "+color.yellow)
report_message = input(color.green+"[+] "+color.cyan+"Enter report message : "+color.yellow)
print(color.green+"[+] "+color.cyan+"Please wait ... (Press CTRL + C to exit)\n")
i = 0
while i <= int(tread):
	i = i + 1
	with TelegramClient("phoenix", api_id, api_hash) as client:
		result = client(functions.messages.ReportRequest(peer=username, id=[int(message_id)], reason=types.InputReportReasonSpam(), message=report_message))
		print(color.red+'[+] '+color.yellow+'Request sent successfully '+color.green+'Result '+color.blue+'>'+color.cyan,result)