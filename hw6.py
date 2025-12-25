from colorama import Fore, Style, init

init()

print(Fore.GREEN + "Успешное сообщение")
print(Fore.RED + "Сообщение об ошибке")
print(Style.RESET_ALL + "Обычный текст")