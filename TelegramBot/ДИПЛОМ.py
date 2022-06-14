import telebot
import wikipedia, re
import sqlite3
from telebot import types# кнопки

# личный ключ телеграм бота
bot = telebot.TeleBot('5198242757:AAFmurUTSc6Bjqv3Ct8zUhvUreelJvOxHew')

# Устанавливаем русский язык в Wikipedia
wikipedia.set_lang("ru")

# Чистим текст статьи в Wikipedia и ограничиваем его 500 символов
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        # Получаем первую 500 символов
        wikitext=ny.content[:500]
        # Разделяем по точкам
        wikimas=wikitext.split('.')
        # # Создаем пустую переменную для текста
        wikitext2 = ''
        # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
        for x in wikimas:
            if not('==' in x):
# Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем
                    # утерянные при разделении строк точки на место
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        # Теперь при помощи регулярных выражений убираем разметку
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        # Возвращаем текстовую строку
        return wikitext2
    # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
    except Exception as e:
        return 'В энциклопедии нет информации об этом'

# добавляем команту
@bot.message_handler(commands=['start'])

# создаем базу данных
def start(message, res=False):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS login_id(id INTEGER)''')
    connect.commit()

    # добавляем ID в БД
    people_id = message.chat.id
    cursor.execute(f'SELECT id FROM login_id WHERE id = {people_id}')
    data = cursor.fetchone()

    # есть ли ID в списке БД
    if data is None:
        user_id = [message.chat.id]
        cursor.execute('INSERT INTO login_id VALUES(?);', user_id)
        connect.commit()
        bot.send_message(message.chat.id, 'Добро пожаловать')
    else:
        bot.send_message(message.chat.id, 'снова ты')# пользователь с таким ID существует

    # обрабатывающая команду /start
    bot.send_message(message.chat.id, 'значение какого слова хочешь узнать')

# Получение сообщений
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))

bot.polling(none_stop=True, interval=0)
