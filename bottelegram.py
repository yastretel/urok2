from random import choice

import telebot

token = "5430873360:AAFw8O5aXpYAjjJ-Vt9MLT090A-6IEVmSBM"

bot = telebot.TeleBot(token)




todos = dict()


HELP = '''
Список доступных команд:
/show  - напечать все задачи на заданную дату
/add  - добавить задачу
/help - Напечатать help
'''


def add_todo(date, task):
    date = date.lower()
    if todos.get(date) is not None:
        todos[date].append(task)
    else:
        todos[date] = [task]


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)




@bot.message_handler(commands=['add'])
def add(message):
    _, date, tail = message.text.split(maxsplit=2)
    task = ' '.join([tail])
    # TODO: 1
    if len(task) < 3:
        bot.send_message(message.chat.id, 'Задачи должны быть больше 3х символов')
    add_todo(date, task)
    bot.send_message(message.chat.id, f'Задача {task} добавлена на дату {date}')


@bot.message_handler(commands=['show'])
def print_(message):
    # TODO: 2
    dates = message.text.split(maxsplit=1)[1].lower().split()
    response  = ''
    for date in dates:
        tasks = todos.get(date)
        response += f'{date}: \n'
        for task in tasks:
            response += f'[ ] {task}\n'
        response += '\n'
    bot.send_message(message.chat.id, response)


bot.polling(none_stop=True)