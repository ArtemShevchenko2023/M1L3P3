import config
import telebot
import random
import requests
bot = telebot.TeleBot(f"{config.token}", parse_mode=None)
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Привет!")
@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Помощь:/")
@bot.message_handler(commands=['random'])
def random_handler(message):
    bot.reply_to(message, 'Пожалуйста, введите второе число:')
    bot.register_next_step_handler(message, process_second_number)
def process_second_number(message):
    try:
        second_number = int(message.text)
        n = random.randint(1, second_number)
        bot.reply_to(message, f'Случайное число от 1 до {second_number}: {n}')
    except ValueError:
        bot.reply_to(message, 'Ошибка! Пожалуйста, введите число.')
@bot.message_handler(commands=['info'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Бот создан в целях практики создания других экземпляров, служит шаблоном!")
@bot.message_handler(commands=['coin'])
def coin_handler(message):
    coin = random.choice(["Орёл", "Решка"])
    if coin == "Орёл":
        bot.reply_to(message, "Выпал", coin)
    else:
        bot.reply_to(message, "Выпала", coin)
@bot.message_handler(commands=['joke'])
def shutka(message):
    spisok = ["Горит крыша - 01, нужна крыша - 02, едет крыша - 03.",
              "Кто не рискует... тот пьёт водку на поминках того, кто рисковал.",
              "Ничто так не бодрит с утра, как незамеченный дверной косяк.",
              "Давая совет, о котором вас не просили, приготовьтесь пойти, куда не собирались.",
              "Самый редкий вид дружбы - это дружба с собственной головой."
              ]
    bot.send_message(message.chat.id, "Банальная шутка: ", random.choice(spisok))
@bot.message_handler(commands=['quote'])
def quote(message):
    spisok = [
             "Подавая руку помощи, не забудь увернуться от пинка благодарности.",
             "Ненависть – удел побежденных. Конфуций",
             "Бог нас всегда окружает теми людьми, с которыми нам необходимо исцелиться от своих недостатков. Симеон Афонский.",
             "Мы должны признать очевидное: понимают лишь те, кто хочет понять. Бернар Вербер",
             "Гений состоит в умении отличать трудное от невозможного. Наполеон Бонапарт"
                ]
    bot.send_message(message.chat.id, "Цитата: ", random.choice(spisok))
@bot.message_handler(commands=['fact'])
def fact(message):
    spisok = [
             "Автором электрического стула был простой дантист.",
             "Длина всех кровеносных сосудов человеческого тела — около девяносто шести тысяч километров.",
             "Три самые богатые семьи в мире имеют больше активов, чем сорок восемь беднейших стран.",
             "Во время полета в самолете скорость роста волос у человека удваивается.",
             "Люди теряют около шестиста тысяч частиц кожи каждый час."
                ]
    bot.send_message(message.chat.id, "Факт: ", random.choice(spisok))
#@bot.message_handler(commands=['weather'])
#def weather(message):
    #s_city = "Saratov,RU"
    #city_id = 498677
    #appid = "9eae125691ce0ffdcfa5e00694181fe5"
    #res = requests.get("http://api.openweathermap.org/data/2.5/weather",
     #            params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    #data = res.json()
    #dat1 = data['weather'][0]['description']
    #dat2 = data['main']['temp']
    #dat3 = data['main']['temp_min']
    #dat4 = data['main']['temp_max']
    #bot.send_message(message.chat.id, "Прогноз: ", dat1)
    #bot.send_message(message.chat.id, "Температура: ", dat2)
    #bot.send_message(message.chat.id, "Минимальная температура: ", dat3)
    #bot.send_message(message.chat.id, "Максимальная температура: ", dat4)
@bot.message_handler(commands=['class'])
def handle_car_command(message):
    # Извлечение аргументов команды
    
    arguments = telebot.util.extract_arguments(message.text)
    class Pythonist:
        def __init__(self, wp = 50, dwp = 50, projects = 100, sobp = 1000, experience = 2):
            self.wp = wp
            self.dwp = dwp
            self.projects = projects
            self.sobp = sobp
            self.experience = experience
        def write_prog(self):
            bot.send_message(message.chat.id, "Ты написал программу! Но не рабочую:)")
        def tweic(self):
            bot.send_message(message.chat.id, "Ты думаешь уже полчаса, но так и не понял где ошибка!")
        def useai(self):
            bot.send_message(message.chat.id, "Ты использовал ИИ и написал рабочую программу!")
    wp = arguments[0]
    dwp = arguments[1]
    projects = arguments[2]
    sobp = arguments[3]
    experience = arguments[4]
    # Создание экземпляра класса Car
    proger = Pythonist(wp=wp, dwp=dwp, projects=projects, sobp=sobp, experience=experience)
    bot.send_message(message.chat.id, "Кол-во рабочих проектов: ", proger.wp, "\nКол-во нерабочих проектов: ", proger.dwp, "\nКол-во всех проектов: ", proger.projects, "\nКол-во строк в лучшем проекте: ", proger.sobp, "\nОпыт использования Python: ", proger.experience)
    
    # Отправка информации о машине в чат
    proger.write_prog()
    proger.tweic()
    proger.useai()
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    photo = message.photo[-1]  # Получаем информацию о последнем фото из сообщения
    file_id = photo.file_id  # Получаем идентификатор файла фото
    file_info = bot.get_file(file_id)  # Получаем информацию о файле фото
    file_path = file_info.file_path  # Получаем путь к файлу фото
    bot.send_message(message.chat.id, "Спасибо за фото!")
@bot.message_handler(commands=['ban'])
def ban_user(message):
    if message.reply_to_message: #проверка на то, что эта команда была вызвана в ответ на сообщение 
        chat_id = message.chat.id # сохранение id чата
         # сохранение id и статуса пользователя, отправившего сообщение
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status 
         # проверка пользователя
        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Невозможно забанить администратора.")
        else:
            bot.ban_chat_member(chat_id, user_id) # пользователь с user_id будет забанен в чате с chat_id
            bot.reply_to(message, f"Пользователь @{message.reply_to_message.from_user.username} был забанен.")
    else:
        bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите забанить.")
@bot.chat_join_request_handler()
def make_some(message: telebot.types.ChatJoinRequest):
    bot.send_message(message.chat.id, 'У нас новый пользователь!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)
@bot.message_handler(func=lambda message: 'https://' in message.text)
def ban_usere(message):
    chat_id = message.chat.id # сохранение id чата
    # сохранение id и статуса пользователя, отправившего сообщение
    user_id = message.reply_to_message.from_user.id
    user_status = bot.get_chat_member(chat_id, user_id).status 
    # проверка пользователя
    if user_status == 'administrator' or user_status == 'creator':
        bot.reply_to(message, "Невозможно забанить администратора.")
    else:
        bot.ban_chat_member(chat_id, user_id) # пользователь с user_id будет забанен в чате с chat_id
        bot.reply_to(message, f"Пользователь @{message.reply_to_message.from_user.username} был забанен.")

bot.polling()

bot.infinity_polling(none_stop=True)
print("Бот запущен.")
