HELP = """
help - напечатать строку по программе.
add - добавить задачу в рассписание(название задачи запрашиваем у пользователя).
show - показать рассписание
"""
today = []
tomorrow = []
other = []

run = True

while run:
    command = input("Введите комманду:")
    if command == "help":
        print(HELP)
    elif command == "show":
        data1 = input("Введите дату на которую хотите увидеть рассписание:")
        if data1 == "Сегодня":
            print(today)
        elif data1 == "Завтра":
            print(tomorrow)
        else:
            print(other)
    elif command == "add":
        task = input("Введите название задачи:")
        data = input("Введите дату задачи:")
        if data == "Сегодня":
            today.append(task)
        elif data == "Завтра":
            tomorrow.append(task)
        else:
            other.append(task)
        print("Задача добавлена")
    elif command == "exit":
        run = False
    else:
        print("Неизвестная комманда")

print("До свидания")