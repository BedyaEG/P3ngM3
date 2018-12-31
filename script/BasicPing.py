from colorama import Fore,Style
import time 
import requests
file = input(Fore.YELLOW+Style.BRIGHT+"[-] Enter The File Name ~~> ")
fileopen = open(file,'r').readlines()
timeoutvar = input(Fore.YELLOW+Style.BRIGHT+"Set TimeOut Between Every Request to ~~> ")

for urls in fileopen:
    try:
        headers = {'GET':'HTTP/1.1',
                    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
                    'Content-Type':'text/plain'}
        url = urls.strip()
        enc_url_non_ssl = 'http://'+url
        enc_url_ssl = 'https://'+url
        req = requests.get(enc_url_non_ssl,headers=headers,allow_redirects=False,verify=True,timeout=(int(timeoutvar)))
        req2 = requests.get(enc_url_ssl,headers=headers,allow_redirects=False,verify=True,timeout=(int(timeoutvar)))
        code = req.status_code
        code2 = req2.status_code
        #Non SSL Requests 
        if code == 200:
            print(Fore.GREEN+Style.BRIGHT+"[+] Live With Status Code [200] "+enc_url_non_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_non_ssl)
            fo.close()
            continue
        elif code == 201:
            print(Fore.GREEN+Style.BRIGHT+"[+] Live With Status Code [201] "+enc_url_non_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_non_ssl)
            fo.close()
            continue
        elif code == 202:
            print(Fore.GREEN+Style.BRIGHT+"[+] Live With Status Code [202] "+enc_url_non_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_non_ssl)
            fo.close()
            continue
        elif code ==204:
            print(Fore.GREEN+Style.BRIGHT+"[+] Live With Status Code [204] "+enc_url_non_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_non_ssl)
            fo.close()
            continue
        elif code == 203:
            print(Fore.GREEN+Style.BRIGHT+"[+] Live With Status Code [203] "+enc_url_non_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_non_ssl)
            fo.close()
            continue
        elif code == 205:
            print(Fore.GREEN+Style.BRIGHT+"[+] Live With Status Code [205] "+enc_url_non_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_non_ssl)
            fo.close()
            continue
        elif code == 207:
            print(Fore.GREEN+Style.BRIGHT+"[+] Live With Status Code [207] "+enc_url_non_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_non_ssl)
            fo.close()
            continue
        elif code == 100:
            print(Fore.GRAY+Style.BRIGHT+"[+] Live With Status Code [100] "+enc_url_non_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_non_ssl)
            fo.close()
            continue
        elif code == 101:
            print(Fore.GRAY+Style.BRIGHT+"[+] Live With Status Code [101] "+enc_url_non_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_non_ssl)
            fo.close()
            continue
        elif code == 301:
            print(Fore.CYAN+Style.BRIGHT+"[+] Live With Status Code [301] "+enc_url_non_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_non_ssl)
            fo.close()
            continue
        elif code == 302:
            print(Fore.CYAN+Style.BRIGHT+"[+] Live With Status Code [302] "+enc_url_non_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_non_ssl)
            fo.close()
            continue
        elif code == 404:
            print(Fore.YELLOW+Style.BRIGHT+"[+] Live With Status Code [404] "+enc_url_non_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_non_ssl)
            fo.close()
            continue
        elif code == 304:
            print(Fore.CYAN+Style.BRIGHT+"[+] Live With Status Code [304] "+enc_url_non_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_non_ssl)
            fo.close()
            continue
        elif code == 403:
            print(Fore.YELLOW+Style.BRIGHT+"[+] Live With Status Code [403] "+enc_url_non_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_non_ssl)
            fo.close()
            continue
        elif code == 400:
            print(Fore.YELLOW+Style.BRIGHT+"[+] Live With Status Code [400] "+enc_url_non_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_non_ssl)
            fo.close()
            continue
        elif code == 401:
            print(Fore.YELLOW+Style.BRIGHT+"[+] Live With Status Code [401] "+enc_url_non_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_non_ssl)
            fo.close()
            continue
        elif code == 402:
            print(Fore.YELLOW+Style.BRIGHT+"[+] Live With Status Code [402] "+enc_url_non_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_non_ssl)
            fo.close()
            continue
        elif code == 405:
            print(Fore.YELLOW+Style.BRIGHT+"[+] Live With Status Code [405] "+enc_url_non_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_non_ssl)
            fo.close()
            continue
        elif code == 307:
            print(Fore.CYAN+Style.BRIGHT+"[+] Live With Status Code [307] "+enc_url_non_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_non_ssl)
            fo.close()
            continue
        elif code == 308:
            print(Fore.CYAN+Style.BRIGHT+"[+] Live With Status Code [308] "+enc_url_non_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_non_ssl)
            fo.close()
            continue
        elif code == 300:
            print(Fore.CYAN+Style.BRIGHT+"[+] Live With Status Code [300] "+enc_url_non_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_non_ssl)
            fo.close()
            continue
    #-----------------------------------**************************-------------------------------------------------#
    #SSL Requests
        elif code2 == 200:
            print(Fore.GREEN+Style.BRIGHT+"[+] Live With Status Code [200] "+enc_url_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_ssl)
            fo.close()
            continue
        elif code2 == 201:
            print(Fore.GREEN+Style.BRIGHT+"[+] Live With Status Code [201] "+enc_url_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_ssl)
            fo.close()
            continue
        elif code2 == 202:
            print(Fore.GREEN+Style.BRIGHT+"[+] Live With Status Code [202] "+enc_url_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_ssl)
            fo.close()
            continue
        elif code2 == 204:
            print(Fore.GREEN+Style.BRIGHT+"[+] Live With Status Code [204] "+enc_url_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_ssl)
            fo.close()
            continue
        elif code2 == 203:
            print(Fore.GREEN+Style.BRIGHT+"[+] Live With Status Code [203] "+enc_url_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_ssl)
            fo.close()
            continue
        elif code2 == 205:
            print(Fore.GREEN+Style.BRIGHT+"[+] Live With Status Code [205] "+enc_url_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_ssl)
            fo.close()
            continue
        elif code2 == 207:
            print(Fore.GREEN+Style.BRIGHT+"[+] Live With Status Code [207] "+enc_url_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_ssl)
            fo.close()
            continue
        elif code2 == 100:
            print(Fore.GRAY+Style.BRIGHT+"[+] Live With Status Code [100] "+enc_url_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_ssl)
            fo.close()
            continue
        elif code2 == 101:
            print(Fore.GRAY+Style.BRIGHT+"[+] Live With Status Code [101] "+enc_url_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_ssl)
            fo.close()
            continue
        elif code2 == 301:
            print(Fore.CYAN+Style.BRIGHT+"[+] Live With Status Code [301] "+enc_url_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_ssl)
            fo.close()
            continue
        elif code2 == 302:
            print(Fore.CYAN+Style.BRIGHT+"[+] Live With Status Code [302] "+enc_url_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_ssl)
            fo.close()
            continue
        elif code2 == 404:
            print(Fore.YELLOW+Style.BRIGHT+"[+] Live With Status Code [404] "+enc_url_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_ssl)
            fo.close()
            continue
        elif code2 == 304:
            print(Fore.CYAN+Style.BRIGHT+"[+] Live With Status Code [304] "+enc_url_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_ssl)
            fo.close()
            continue
        elif code2 == 403:
            print(Fore.YELLOW+Style.BRIGHT+Style.BRIGHT+"[+] Live With Status Code [403] "+enc_url_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_ssl)
            fo.close()
            continue
        elif code2 == 400:
            print(Fore.YELLOW+Style.BRIGHT+"[+] Live With Status Code [400] "+enc_url_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_ssl)
            fo.close()
            continue
        elif code2 == 401:
            print(Fore.YELLOW+Style.BRIGHT+"[+] Live With Status Code [401] "+enc_url_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_ssl)
            fo.close()
            continue
        elif code2 == 402:
            print(Fore.YELLOW+Style.BRIGHT+"[+] Live With Status Code [402] "+enc_url_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_ssl)
            fo.close()
            continue
        elif code2 == 405:
            print(Fore.YELLOW+Style.BRIGHT+"[+] Live With Status Code [405] "+enc_url_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_ssl)
            fo.close()
            continue
        elif code2 == 307:
            print(Fore.CYAN+Style.BRIGHT+"[+] Live With Status Code [307] "+enc_url_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_ssl)
            fo.close()
            continue
        elif code2 == 308:
            print(Fore.CYAN+Style.BRIGHT+"[+] Live With Status Code [308] "+enc_url_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_ssl)
            fo.close()
            continue
        elif code2 == 300:
            print(Fore.CYAN+Style.BRIGHT+"[+] Live With Status Code [300] "+enc_url_ssl)
            fo = open('../HostnameLive.txt','a')
            fo.write('\n')
            fo.write(enc_url_ssl)
            fo.close()
            continue
    except requests.exceptions.ConnectionError:
        print(Fore.RED+"[-] Hostname Error "+enc_url_ssl) or print(Fore.RED+"[-] Hostname Error "+enc_url_non_ssl)
        fo = open('../HostnameDead.txt','a')
        fo.write('\n')
        fo.write(enc_url_ssl)
        fo.write('\n')
        fo.write(enc_url_non_ssl)
        fo.close()
        continue

    except KeyboardInterrupt:
        ask = input(Fore.CYAN+Style.BRIGHT+'\n'+"Are You Want to Exit or Continue ? Yes(Exit) No(Continue)"+'\n'+"PingME~$ ")
        if 'yes' in ask or 'Yes' in ask:
            exit()
        elif 'no' in ask or 'No' in ask:
            continue
        else:
            print("Invalid Answer")
            input(ask)
    except requests.exceptions.ReadTimeout:
        continue
    except requests.exceptions.InvalidURL:
        print(Fore.RED+Style.BRIGHT+"[=] Invalid URL "+enc_url_ssl) or print(Fore.RED+Style.BRIGHT+"[=] Invalid URL "+enc_url_non_ssl)
        continue
spcf_time = str(time.asctime())
print('\n'+Fore.MAGENTA+Style.BRIGHT+"Finished in {0} Successfuly".format(spcf_time)+"\n"+"\n {0}@BedyaEG - Hossam Abdel Hamid".format(Fore.CYAN+Style.BRIGHT)+"\n")
