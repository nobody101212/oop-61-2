class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role


ALLOWED_COMMANDS = {
    "admin": ["start", "ban", "stop", "message"],
    "user": ["start", "message"]
}


def check_permission(command):
    def decorator(func):
        def wrapper(self, user):
            if command not in ALLOWED_COMMANDS.get(user.role, []):
                print(f'❌ Пользователь {user.username} не может выполнять команду "{command}"')
                return
            print(f'Пользователь {user.username} ({user.role}) выполняет команду {command}')
            func(self, user)
        return wrapper
    return decorator


class CommandHandler:

    @check_permission("start")
    def start(self, user):
        print("Команда start выполнена")

    @check_permission("ban")
    def ban(self, user):
        print("Пользователь забанен")

    @check_permission("stop")
    def stop(self, user):
        print("Команда stop выполнена")

    @check_permission("message")
    def message(self, user):
        print("Пользователь отправил сообщение")


admin = User("Alice", "admin")
user = User("Bob", "user")

handler = CommandHandler()

handler.start(admin)
handler.ban(admin)
handler.stop(admin)

print()

handler.start(user)
handler.ban(user)
handler.message(user)