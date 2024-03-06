print("__   __ _    ____   ____ ___")
print("\ \ / // \  |  _ \ / ___|_ _|")
print(" \ V // _ \ | |_) | |  _ | |")
print("  | |/ ___ \|  _ <| |_| || |")
print("  |_/_/   \_\_| \_\\____|___|")

import subprocess

def main():
    answer = input("Do you want to start YARGI session sploit? (y/n): ").lower()
    
    if answer == 'y': 
        subprocess.Popen(r"C:\Users\User\Desktop\YARGI-Session-hacking\yargi\YARGI.exe")

    elif answer == 'n':
        exit()
    else:
        print("Invalid input! Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()