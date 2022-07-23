import telebot




HELP = """
help - напечатать строку по программе.
add - добавить задачу в рассписание(название задачи запрашиваем у пользователя).
show - показать рассписание на определённое число
"""
today = []
tomorrow = []
other = []

run = True

def show():
    global data1
    data1 = input("Введите дату на которую хотите увидеть рассписание:")
    if data1 == "Сегодня":
        print('-', today)
    elif data1 == "Завтра":
        print('-', tomorrow)
    else:
        print('-', other)

def add():
    task = input("Введите название задачи:")
    data = input("Введите дату задачи:")
    if data == "Сегодня":
        today.append(task)
    elif data == "Завтра":
        tomorrow.append(task)
    else:
        other.append(task)
    print("Задача", task, "на дату", data, "Добавлена")

while run:
    command = input("Введите комманду:")
    if command == "help":
        print(HELP)
    elif command == "show":
        show()

    elif command == "add":
        add()
    else:
        print("Неизвестная комманда")

print("До свидания")