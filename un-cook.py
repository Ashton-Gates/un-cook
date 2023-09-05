
import os
from mitmproxy import http

print("""

__/\\\________/\\\_        __/\\\\\_____/\\\_        _______________        ________/\\\\\\\\\_        _____/\\\\\\\____        _____/\\\\\\\____        __/\\\________/\\\_        
 _\/\\\_______\/\\\_        _\/\\\\\\___\/\\\_        _______________        _____/\\\////////__        ___/\\\/////\\\__        ___/\\\/////\\\__        _\/\\\_____/\\\//__       
  _\/\\\_______\/\\\_        _\/\\\/\\\__\/\\\_        _______________        ___/\\\/___________        __/\\\____\//\\\_        __/\\\____\//\\\_        _\/\\\__/\\\//_____      
   _\/\\\_______\/\\\_        _\/\\\//\\\_\/\\\_        __/\\\\\\\\\\\_        __/\\\_____________        _\/\\\_____\/\\\_        _\/\\\_____\/\\\_        _\/\\\\\\//\\\_____     
    _\/\\\_______\/\\\_        _\/\\\\//\\\\/\\\_        _\///////////__        _\/\\\_____________        _\/\\\_____\/\\\_        _\/\\\_____\/\\\_        _\/\\\//_\//\\\____    
     _\/\\\_______\/\\\_        _\/\\\_\//\\\/\\\_        _______________        _\//\\\____________        _\/\\\_____\/\\\_        _\/\\\_____\/\\\_        _\/\\\____\//\\\___   
      _\//\\\______/\\\__        _\/\\\__\//\\\\\\_        _______________        __\///\\\__________        _\//\\\____/\\\__        _\//\\\____/\\\__        _\/\\\_____\//\\\__  
       __\///\\\\\\\\\/___        _\/\\\___\//\\\\\_        _______________        ____\////\\\\\\\\\_        __\///\\\\\\\/___        __\///\\\\\\\/___        _\/\\\______\//\\\_ 
        ____\/////////_____        _\///_____\/////__        _______________        _______\/////////__        ____\///////_____        ____\///////_____        _\///________\///__

""")

def response(flow: http.HTTPFlow) -> None:
    # Remove Set-Cookie header from all responses
    if "Set-Cookie" in flow.response.headers:
        del flow.response.headers["Set-Cookie"]

    flow.response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    flow.response.headers["Pragma"] = "no-cache"
    flow.response.headers["Expires"] = "0"

def launch_browser(os_choice, browser_choice):
    proxy_command = '--proxy-server="http://localhost:8080"'
    
    if os_choice == "1":  # macOS
        if browser_choice == "1":  # Safari
            print("Safari does not support command-line proxy settings. Please set it manually.")
        elif browser_choice == "2":  # Chrome
            os.system(f'"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" {proxy_command}')
        elif browser_choice == "3":  # Firefox
            os.system(f'"/Applications/Firefox.app/Contents/MacOS/firefox" {proxy_command}')
        # Add commands for other browsers on macOS...

    elif os_choice == "2":  # Linux
        if browser_choice == "1":  # Firefox
            os.system(f'firefox {proxy_command}')
        elif browser_choice == "2":  # Chrome
            os.system(f'google-chrome {proxy_command}')
        elif browser_choice == "3":  # Chromium
            os.system(f'chromium {proxy_command}')
        # Add commands for other browsers on Linux...

    elif os_choice == "3":  # Windows
        if browser_choice == "1":  # Edge
            os.system(f'cmd /c "start msedge {proxy_command}"')
        elif browser_choice == "2":  # Chrome
            os.system(f'cmd /c "start chrome {proxy_command}"')
        elif browser_choice == "3":  # Firefox
            os.system(f'cmd /c "start firefox {proxy_command}"')
        elif browser_choice == "4":  # Safari
            print("Safari is not available for Windows.")
        elif browser_choice == "5":  # Tor Browser
            # Assuming default installation path, adjust if necessary
            os.system(f'cmd /c "start "C:\\Users\\{os.getlogin()}\\Desktop\\Tor Browser\\Browser\\firefox.exe" {proxy_command}"')
        # Add commands for other browsers on Windows...


def main():
    print("Select your operating system:")
    print("1. macOS")
    print("2. Linux")
    print("3. Windows")
    os_choice = input("Enter your choice (1/2/3): ")

    print("\nSelect your browser:")
    print("1. Safari")
    print("2. Chrome")
    print("3. Edge")
    print("4. Firefox")
    print("5. Tor Browser")
    browser_choice = input("Enter your choice (1/2/3/4/5): ")

    launch_browser(os_choice, browser_choice)

if __name__ == "__main__":
    main()