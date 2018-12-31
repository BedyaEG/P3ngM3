from colorama import Fore,Style
import time 
import subprocess
#BetaVersion More Features Later .... 
file = input(Fore.YELLOW+Style.BRIGHT+"[-] Enter The File Name ~~> ")
fileopen = open(file,'r').readlines()


def using_count():
    count_request  = input(Fore.YELLOW+Style.BRIGHT+"Enter how many count you need ? ")
    for a in fileopen:
        url = a.strip()
        results = subprocess.call("ping -c {0} {1} ".format(count_request,url),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        #ping = subprocess.run(["ping ", "-c {0} {1}".format(count_request)])
        if results == 0:
            print("[+] Live Host  "+url)
            fo = open('../AdvancedHostname-Live.txt','a')
            fo.write('\n')
            fo.write(url)
            fo.close()

        else:
            print("[-] Dead Host "+url)
            fo = open('../AdvancedHostname-Die.txt','a')
            fo.write('\n')
            fo.write(url)
            fo.close()

def using_mark():
    count_request  = input(Fore.YELLOW+Style.BRIGHT+"Enter how many count you need ? ")
    mark_request  = input(Fore.YELLOW+Style.BRIGHT+"Enter how many mark you need ? ")
    for a in fileopen:
        url = a.strip()
        results = subprocess.call("ping -c {0} -m {1} {2} ".format(count_request,mark_request,url),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        #ping = subprocess.run(["ping ", "-c {0} {1}".format(count_request)])
        if results == 0:
            print("[+] Live Host  "+url)
            fo = open('../AdvancedHostname-Live.txt','a')
            fo.write('\n')
            fo.write(url)
            fo.close()
        else:
            print("[-] Dead Host "+url)
            fo = open('../AdvancedHostname-Die.txt','a')
            fo.write('\n')
            fo.write(url)
            fo.close()
def using_interface():
    interface_request = input(Fore.YELLOW+Style.BRIGHT+"Enter The Interface Type ~$  ")
    count_request  = input(Fore.YELLOW+Style.BRIGHT+"Enter how many count you need ? ")
    mark_request  = input(Fore.YELLOW+Style.BRIGHT+"Enter how many mark you need ? ")
    for a in fileopen:
        url = a.strip()
        results = subprocess.call("ping -I {0} -c {1} -m {2} {3} ".format(interface_request,count_request,mark_request,url),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        #ping = subprocess.run(["ping ", "-c {0} {1}".format(count_request)])
        if results == 0:
            print("[+] Live Host "+url)
            fo = open('../AdvancedHostname-Live.txt','a')
            fo.write('\n')
            fo.write(url)
            fo.close()
        else:
            print("[-] Dead Host "+url)
            fo = open('../AdvancedHostname-Die.txt','a')
            fo.write('\n')
            fo.write(url)
            fo.close()
def using_packetsize():
    count_request  = input(Fore.YELLOW+Style.BRIGHT+"Enter how many count you need ? ")
    packet_request = input(Fore.YELLOW+Style.BRIGHT+"Enter how many packet you need to send? ")
    for a in fileopen:
        url = a.strip()
        results = subprocess.call("ping -s {0} -c {1} {2}".format(packet_request,count_request,url),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        #ping = subprocess.run(["ping ", "-c {0} {1}".format(count_request)])
        if results == 0:
            print("[+] Live Host  "+url)
            fo = open('../AdvancedHostname-Live.txt','a')
            fo.write('\n')
            fo.write(url)
            fo.close()
        else:
            print("[-] Dead Host "+url)
            fo = open('../AdvancedHostname-Die.txt','a')
            fo.write('\n')
            fo.write(url)
            fo.close()
def using_howmany_request():
    deadline_request = input(Fore.YELLOW+Style.BRIGHT+"Enter how many deadline you need ?  ")
    for a in fileopen:
        url = a.strip()
        results = subprocess.call("ping -w {0} {1}".format(deadline_request,url),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        #ping = subprocess.run(["ping ", "-c {0} {1}".format(count_request)])
        if results == 0:
            print("[+] Live Host "+url)
            fo = open('../AdvancedHostname-Live.txt','a')
            fo.write('\n')
            fo.write(url)
            fo.close()
        else:
            print("[-] Dead Host "+url)
            fo = open('../AdvancedHostname-Die.txt','a')
            fo.write('\n')
            fo.write(url)
            fo.close()
def using_time_interval():
    interval_request = input(Fore.YELLOW+Style.BRIGHT+"Enter how many time interval you need ?  ")
    for a in fileopen:
        url = a.strip()
        results = subprocess.call("ping -i {0} {1}".format(interval_request,url),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        #ping = subprocess.run(["ping ", "-c {0} {1}".format(count_request)])
        if results == 0:
            print("[+] Live Host "+url)
            fo = open('../AdvancedHostname-Live.txt','a')
            fo.write('\n')
            fo.write(url)
            fo.close()
        else:
            print("[-] Dead Host "+url)
            fo = open('../AdvancedHostname-Die.txt','a')
            fo.write('\n')
            fo.write(url)
            fo.close()

#functions
print(Fore.RED+Style.BRIGHT+"\n For Ping using Count Choose 1 \n For Ping Using Mark Choose 2 \n For Ping Using Interface Type Choose 3 \n For Ping Using Packet Size Choose 4 \n For Ping Using DeadLine requests choose 5 \n For Ping Using Time Interval Choose 6 \n ")
time.sleep(2)
#Now The Selection of the user 
user_select = input(Fore.GREEN+Style.BRIGHT+"Enter Choice \n PingMe ~$ ")
if user_select == "1":
    print(Fore.BLUE+Style.BRIGHT+" \n The Module Has Been Loaded Please Wait..\n")
    time.sleep(2)
    using_count()
elif user_select == "2":
    print(Fore.BLUE+Style.BRIGHT+" \n The Module Has Been Loaded Please Wait..\n")
    time.sleep(2)
    using_mark()
elif user_select == "3":
    print(Fore.BLUE+Style.BRIGHT+" \n The Module Has Been Loaded Please Wait..\n")
    time.sleep(2)
    using_interface()
elif user_select == "4":
    print(Fore.BLUE+Style.BRIGHT+" \n The Module Has Been Loaded Please Wait..\n")
    time.sleep(2)
    using_packetsize()
elif user_select== "5":
    print(Fore.BLUE+Style.BRIGHT+" \n The Module Has Been Loaded Please Wait..\n")
    time.sleep(2)
    using_howmany_request()
elif user_select== "6":
    print(Fore.BLUE+Style.BRIGHT+" \n The Module Has Been Loaded Please Wait..\n")
    time.sleep(2)
    using_time_interval()
else:
    print("Incorrect Choice")
    exit()

spcf_time = str(time.asctime())
print('\n'+Fore.MAGENTA+Style.BRIGHT+"Finished in {0} Successfuly".format(spcf_time)+"\n"+"\n {0}@BedyaEG - Hossam Abdel Hamid".format(Fore.CYAN+Style.BRIGHT)+"\n")
