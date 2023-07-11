import os
import ctypes
import platform
import subprocess
import winreg
import urllib.request
import socket

def delete_temp_files():
    temp_path = os.environ.get("TEMP")
    if temp_path:
        for root, dirs, files in os.walk(temp_path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")

def set_wallpaper_to_black():
    try:
        # Change wallpaper to black
        SPI_SETDESKWALLPAPER = 0x0014
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, " ", 3)
        print("Wallpaper set to black.")
    except Exception as e:
        print(f"Failed to set wallpaper to black: {e}")

def set_performance_settings():
    try:
        if platform.system() == "Windows":
            if platform.release() == "10":
                # Set performance settings through the registry on Windows 10
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                     "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VisualEffects",
                                     0, winreg.KEY_WRITE)
                winreg.SetValueEx(key, "VisualFXSetting", 0, winreg.REG_DWORD, 2)
                winreg.CloseKey(key)
                print("Performance settings adjusted for best performance.")
            else:
                print("Performance settings can only be adjusted on Windows 10.")
        else:
            print("Performance settings adjustment is only supported on Windows.")
    except Exception as e:
        print(f"Failed to adjust performance settings: {e}")

def turn_off_background_apps():
    try:
        if platform.system() == "Windows":
            if platform.release() == "10":
                # Disable background apps through the registry on Windows 10
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                     "Software\\Microsoft\\Windows\\CurrentVersion\\BackgroundAccessApplications",
                                     0, winreg.KEY_WRITE)
                winreg.SetValueEx(key, "GlobalUserDisabled", 0, winreg.REG_DWORD, 1)
                winreg.CloseKey(key)
                print("Background apps turned off.")
            else:
                print("Background apps can only be turned off on Windows 10.")
        else:
            print("Turning off background apps is only supported on Windows.")
    except Exception as e:
        print(f"Failed to turn off background apps: {e}")

def enable_game_mode():
    try:
        if platform.system() == "Windows":
            if platform.release() == "10":
                # Enable Game Mode through the registry on Windows 10
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                     "Software\\Microsoft\\GameBar",
                                     0, winreg.KEY_WRITE)
                winreg.SetValueEx(key, "AllowAutoGameMode", 0, winreg.REG_DWORD, 1)
                winreg.CloseKey(key)
                print("Game Mode enabled.")
            else:
                print("Game Mode can only be enabled on Windows 10.")
        else:
            print("Enabling Game Mode is only supported on Windows.")
    except Exception as e:
        print(f"Failed to enable Game Mode: {e}")

def turn_off_xbox_game_bar():
    try:
        if platform.system() == "Windows":
            if platform.release() == "10":
                # Disable Xbox Game Bar through the registry on Windows 10
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                     "Software\\Microsoft\\Windows\\CurrentVersion\\GameDVR",
                                     0, winreg.KEY_WRITE)
                winreg.SetValueEx(key, "AppCaptureEnabled", 0, winreg.REG_DWORD, 0)
                winreg.CloseKey(key)
                print("Xbox Game Bar turned off.")
            else:
                print("Xbox Game Bar can only be turned off on Windows 10.")
        else:
            print("Turning off Xbox Game Bar is only supported on Windows.")
    except Exception as e:
        print(f"Failed to turn off Xbox Game Bar: {e}")

def set_max_processors():
    try:
        if platform.system() == "Windows":
            # Set the maximum number of processors through the registry
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                 "SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment",
                                 0, winreg.KEY_WRITE)
            winreg.SetValueEx(key, "NUMBER_OF_PROCESSORS", 0, winreg.REG_SZ, "*")
            winreg.CloseKey(key)
            print("Number of processors set to maximum.")
        else:
            print("Setting the number of processors is only supported on Windows.")
    except Exception as e:
        print(f"Failed to set the number of processors: {e}")

def run_ooshutup():
    try:
        if platform.system() == "Windows":
            # Run O&O ShutUp10 script in the background on Windows
            subprocess.Popen(["ooshutup\\OOSU10.exe", "/silent"])
            print("O&O ShutUp10 script executed.")
        else:
            print("Running O&O ShutUp10 is only supported on Windows.")
    except Exception as e:
        print(f"Failed to run O&O ShutUp10 script: {e}")

def download_ooshutup():
    try:
        if platform.system() == "Windows":
            # Download O&O ShutUp10 if not found
            if not os.path.exists("ooshutup\\OOSU10.exe"):
                print("Downloading O&O ShutUp10...")
                url = "https://dl5.oo-software.com/files/ooshutup10/OOSU10.exe"
                urllib.request.urlretrieve(url, "ooshutup\\OOSU10.exe")
                print("O&O ShutUp10 downloaded.")
            else:
                print("O&O ShutUp10 already exists.")
        else:
            print("Downloading O&O ShutUp10 is only supported on Windows.")
    except Exception as e:
        print(f"Failed to download O&O ShutUp10: {e}")

def check_ping(hostname):
    try:
        response_time = float('inf')
        for i in range(3):
            response = os.system("ping -n 1 -w 1000 " + hostname)
            if response == 0:
                response_time = min(response_time, get_ping_time(hostname))
        return response_time
    except Exception as e:
        print(f"Failed to check ping to DNS server: {e}")
        return float('inf')

def get_ping_time(hostname):
    try:
        response = os.system("ping -n 1 -w 1000 " + hostname)
        if response == 0:
            ping_time = subprocess.check_output("ping -n 1 -w 1000 " + hostname + " | findstr 'Average='", shell=True)
            ping_time = ping_time.decode().strip().split("=")[1].split("ms")[0].strip()
            return float(ping_time)
    except Exception as e:
        print(f"Failed to get ping time to DNS server: {e}")
        return float('inf')

def set_dns_server(dns_server):
    try:
        if platform.system() == "Windows":
            subprocess.check_output("netsh interface ip set dns name='Wi-Fi' static " + dns_server + " primary", shell=True)
            subprocess.check_output("netsh interface ip add dns name='Wi-Fi' addr=" + dns_server + " index=2", shell=True)
            print(f"DNS server set to {dns_server}.")
        else:
            print("Setting DNS server is only supported on Windows.")
    except Exception as e:
        print(f"Failed to set DNS server: {e}")

def main():
    delete_temp_files()
    set_wallpaper_to_black()
    set_performance_settings()
    turn_off_background_apps()
    enable_game_mode()
    turn_off_xbox_game_bar()
    set_max_processors()

    # Check and run O&O ShutUp10
    if not os.path.exists("ooshutup"):
        os.mkdir("ooshutup")
    if os.path.exists("ooshutup\\OOSU10.exe"):
        run_ooshutup()
    else:
        download_ooshutup()
        run_ooshutup()

    # Perform DNS ping and set DNS server to the highest ping
    dns_servers = ["8.8.8.8", "1.1.1.1", "9.9.9.9"]  # Add more DNS servers if needed
    highest_ping = float('-inf')
    highest_ping_dns = ""
    for dns_server in dns_servers:
        ping_time = check_ping(dns_server)
        if ping_time > highest_ping:
            highest_ping = ping_time
            highest_ping_dns = dns_server
    if highest_ping_dns:
        set_dns_server(highest_ping_dns)

if __name__ == "__main__":
    main()
