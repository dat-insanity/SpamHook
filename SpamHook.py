#!usr/bin/env python3
# Created by dat_insanity
# GitHub: https://github.com/dat-insanity
# Discord dat_insanity#2048

import requests, os, sys, time, random

if sys.platform.startswith('win32'):
	os.system('cls')
else:
	os.system('clear')

print('\33[35m _____                       _   _             _    ')
print('\33[35m/  ___|                     | | | |           | |   ')
print('\33[35m\ `--. _ __   __ _ _ __ ___ | |_| | ___   ___ | | __')
print("\33[35m `--. \ '_ \ / _` | '_ ` _ \|  _  |/ _ \ / _ \| |/ /")
print('\33[35m/\__/ / |_) | (_| | | | | | | | | | (_) | (_) |   < ')
print("\33[35m\____/| .__/ \__,_|_| |_| |_\_| |_/\___/ \___/|_|\_\\")
print('\33[35m	| |                      made by dat_insanity :)')
print('\33[35m	|_|                                         v1.0')
print()

webhook = input('\33[31mPaste in your webhook URL: ')
username = input('\33[31mInput the bot username: ')
amount = int(input('\33[31mHow many times should the message send (input a negative number for unlimited): '))
option =  input('\33[31mWhat mode do you pick, custom message (1), or ascii spammer (2): ') 

if option == '1':
	msg = input('\33[31mPaste in your message: ')
	input('\033[1mPress enter to start, or control-c to quit: ')
	data = {
		"content" : msg,
		"username" : username
	}
	while amount != 0:
		result = requests.post(webhook, json = data)
		try:
			result.raise_for_status()
		except requests.exceptions.HTTPError as err:
			print(err)
			print('\33[40m\033[91mPausing for 10 seconds, you may be rate limited. (usually clears up after a minute)')
			time.sleep(10)
		else:
			print("\33[40m\033[92mMessage sent successfully, code {}.".format(result.status_code))	
			amount = amount - 1
elif option == '2':
	def ascii(length):
		asc = ''
		for x in range(int(length)):
			num = random.randrange(13000)
			asc = asc + chr(num)
		return asc
	
	while amount != 0:
		data = {
			"content" : ascii(1999),
			"username" : username
		}
		result = requests.post(webhook, json = data)
		try:
			result.raise_for_status()
		except requests.exceptions.HTTPError as err:
			print(err)
			print('\33[40m\033[91mPausing for 10 seconds, you may be rate limited. (usually clears up after a minute)')
			time.sleep(10)
		else:
			print("\33[40m\033[92mMessage sent successfully, code {}.".format(result.status_code))	
			amount = amount - 1
else:
	print('Invalid option chosen for mode, quitting!')
	quit()
