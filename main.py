# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
from colorama import init, Fore, Back, Style
from alive_progress import alive_bar


def printOK(message):
    print(Style.RESET_ALL + Fore.GREEN + "✅" +  message + Style.RESET_ALL)

def printWarning(message):
    print(Style.RESET_ALL + Fore.YELLOW + "❗" + message + Style.RESET_ALL)

init()
print(Fore.CYAN + "Pfizer firmware v2021.1 🌡" + Style.RESET_ALL)
with alive_bar(0,spinner="classic",title="Checking if the vaccine is applied...") as bar:
    bar.text("Checking...")
    for i in range(100):
        time.sleep(0.03)
        bar()
printOK("Ok, vaccine SoC 'Comirnaty, ver. 2021' is applied.")
print("Welcome to the NWO family!")
time.sleep(0.2)
with alive_bar(0,spinner="classic",title="Mutating DNA") as bar:
    for i in range(100):
        time.sleep(0.05)
        bar()
printWarning("DNA was altered.")
time.sleep(0.5)
printWarning("Your aura might have changed.")
time.sleep(0.75)
print("Preparing to setup 5G connectivity...")
time.sleep(0.75)
printOK("You are now 5G hotspot with id 'VIKTOR-0x53de1'")
with alive_bar(0,spinner="classic",title="Checking the connection") as bar:
    for i in range(100):
        time.sleep(0.05)
        bar()
with alive_bar(0,spinner="classic",title="Generating certificates") as bar:
    for i in range(100):
        time.sleep(0.1)
        bar()

with alive_bar(100,title="Registering to Bill Gates VPN") as bar:
    for i in range(100):
        time.sleep(0.05)
        bar()
printOK("You are now connected with Bill Gates")

# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
