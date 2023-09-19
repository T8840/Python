# -*- coding: utf-8 -*-

import pywifi, time
from pywifi import const

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]
print(iface.name())
def wifi_connect_status():
    if iface.status() in [const.IFACE_CONNECTED,const.IFACE_INACTIVE]:
        print('wifi connected')
        return 1
    else:
        print('wifi not connected')
        return 0



def scan_wifi():
    iface.scan()
    time.sleep(1)
    basewifi = iface.scan_results()
    for i in basewifi:
        print('wifi scan result: {}'.format(i.ssid.encode('utf-8').decode('gbk')))
        print('wifi device address: {}'.format(i.bssid))
    return basewifi

def disconnect_wifi():
    iface.disconnect()
    time.sleep(3)

def connect_wifi():
    profile = pywifi.Profile() # the config
    profile.ssid = "" # the wifi name
    profile.key = "" # the wifi password

    profile.auth = const.Auth_ALG_OPEN # need password
    profile.akm.append(const.AKM_TYPE_WPA2PSK) # crypto type
    profile.cipher = const.CIPHER_TYPE_CCMP # crypto unit

    iface.remove_all_network_profiles() # delete all saved wifi config
    tmp_profile = iface.add_network_profile(profile)
    iface.connect(tmp_profile)
    time.sleep(10)
    if iface.status() == const.IFACE_CONNECTED:
        print("New Wifi Connected!")
    else:
        print("New Wifi Not Connected!")



if __name__ == "__main__":
    disconnect_wifi()

