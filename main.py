from colorama import Fore

def setFontColorRed(text):
    return Fore.RED + text

def setFontColorGreen(text):
    return Fore.GREEN + text

def setFontColorBlue(text):
    return Fore.BLUE + text

def setFontColorCyan(text):
    return Fore.CYAN + text

def setFontColorMagenta(text):
    return Fore.MAGENTA + text

def setFontColorGold(text):
    return Fore.YELLOW + text

def setFontColorWhite(text):
    return Fore.WHITE + text

def setFontColorBlack(text):
    return Fore.BLACK + text

def setFontColorLightRed(text):
    return Fore.LIGHTRED_EX + text



print(setFontColorRed("Hello This is Red Text"))
print(setFontColorLightRed("Hello this is Light Red Text"))
print(setFontColorGreen("Hello This is Green Text"))
print(setFontColorBlue("Hello This is Blue Text"))
print(setFontColorMagenta("Hello this is Magenta Text"))
print(setFontColorCyan("Hello this is Cyan Text"))
print(setFontColorGold("Hello this is Gold Text"))
print(setFontColorWhite("Hello this is White Text"))
print(setFontColorBlack("Hello this is Black Text"))