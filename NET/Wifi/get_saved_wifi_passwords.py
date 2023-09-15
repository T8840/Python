def saved_wifi_passwords():
    """
    Used in Windows
    """
    import subprocess
    import re
    # Execute the command 'netsh wlan show profiles' to get a list of all saved profiles
    result = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True, text=True).stdout

    # Extracting all the WiFi names
    wifi_names = re.findall(r"所有用户配置文件 : (.*)", result)

    # Dictionary to hold the WiFi names and their respective passwords
    passwords = {}

    # Looping through each WiFi to get its password
    for name in wifi_names:
        # Running the 'key=clear' command to get all details of a particular WiFi
        wifi_result = subprocess.run(['netsh', 'wlan', 'show', 'profile', 'name={}'.format(name), 'key=clear'], capture_output=True, text=True).stdout
        # Extracting the password using regex
        if wifi_result:
            password_search = re.search(r"关键内容\s*:\s*(.*)", wifi_result)
            if password_search:
                password = password_search.group(1)
                print(f"SSID: {name}, Password: {password}")
            else:
                print(f"SSID: {name} has no password!")
        else:
            print(f"Failed to retrieve details for SSID: {name}")
    return passwords

def get_saved_wifi_passwords():
    wifi_passwords = saved_wifi_passwords()
    for name, password in wifi_passwords.items():
        if password:
            print(f"SSID: {name}, Password: {password}")
        else:
            print(f"SSID: {name} has no password!")

if __name__ == "__main__":
    get_saved_wifi_passwords()