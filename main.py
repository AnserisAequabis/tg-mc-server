import telebot
import sys
from subprocess import Popen, PIPE, STDOUT
import time


tid = 123456789					#telegram id of "admin" as int


bot = telebot.TeleBot('')		#telegram bot token here



def kill_var():
	global server
	del server


@bot.message_handler(commands=['startserver'])
def launch(bot_msg):
	if bot_msg.chat.id == tid:
		if 'server' not in globals():
			try:
					global server
					path = 'E:\папка\paper-1.19.2-125.jar'														#path to mc server jar
					server = Popen(['java', '-jar', path], stdout=PIPE, stdin=PIPE, stderr=STDOUT, text=True) 
					print('launching server')
					time.sleep(60)
					bot.reply_to(bot_msg, 'ну я хз, минута прошла, наверное сервер работает')
			except:
					errorMessage = sys.exc_info()
					print("Server chrashed. The error messge was:", end="")
					raise print(errorMessage)
		else:
			bot.reply_to(bot_msg, 'слишком много серверов хочешь')



@bot.message_handler(commands=['stopserver'])
def kill(bot_msg):
	if bot_msg.chat.id == tid:
		if 'server' in globals():
			try:
				server.stdin.write('save-all\n')
				server.stdin.flush()
				server.stdin.write('stop\n')
				server.stdin.flush()
				server.wait()
				bot.reply_to(bot_msg, 'probably he\'s dead')
				kill_var()
			except Exception as e:
				print(e)
				bot.reply_to(bot_msg, 'хватит ломать')
		else:
			bot.reply_to(bot_msg, 'и что ты пытаешься стопнуть?, я не вижу сервака')


bot.infinity_polling()