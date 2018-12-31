from colorama import Fore,Style
import time
import sys
import getpass
import requests
if sys.version > '3':
    pass
else:
    time.sleep(2)
    print(Fore.YELLOW+Style.BRIGHT+"You Running At Python 2 \n [+] Run python3 P3ngM3.py [+]")
    exit()
def chk_internet():
	try:
		url = 'https://start.parrotsec.org/'
		req = requests.get(url)
		http = req.content
		if b'IP' in http:
			pass
		else:
			print(Fore.YELLOW+Style.BRIGHT+"No Internet Connection \n Connect To Network Then Try Again Later")
			exit()
	except requests.exceptions.ConnectionError as e:
		print(Fore.YELLOW+Style.BRIGHT+"You're Not Connected To Any Network\nConnect To Network Then Try Again")
		exit()
		
chk_internet()

Detect_user = getpass.getuser()
print(Fore.RED+Style.BRIGHT+"Hello "+Detect_user.upper())


print(Fore.RED+Style.BRIGHT+"\n Welcome To P3ngMe Tool Please Wait Untill it start ");time.sleep(2)

from script import Banner
time.sleep(2)


print(Fore.BLUE+Style.BRIGHT+"\n Please Read The ReadMe.md First To Know How To Deal With The Tool \n")

print(Fore.YELLOW+Style.BRIGHT+"""\n
		[1] P3ngM3 Basic 
		[2] P3ngM3 Advanced \n \n \n """);time.sleep(2)
while True:
	user = input(Fore.CYAN+Style.BRIGHT+"\n Choose ~~> ")
	if user == "1":
		from script import BasicPing
		break
	elif user == "2":
		from script import AdvancedPing
		break
	else:
		print(Fore.CYAN+Style.BRIGHT+"Choice Not Found,Try Again ~~> ")
	