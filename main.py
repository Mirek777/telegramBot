import telebot
from telebot import types

name = ''
surname = ''
city = ''
quantityVacancies = 4000
technology = ''
textQuantityVacancies = '' + 'базе ' + str(quantityVacancies) + ' вакансий'

bot = telebot.TeleBot("5100500044:AAESD-UOYikG3MH8JRv_vdOfuoxZzh3_34I")

@bot.message_handler(func= lambda message: True)
def echo_all(message):
    global quantityVacancies
    global textQuantityVacancies
    welcomeMessage = 'Здравуствуй! Сейчас в ' + textQuantityVacancies
    bot.reply_to(message, welcomeMessage)
    bot.send_message(message.from_user.id, "Давай познакомимся! Как тебя зовут?")
    bot.register_next_step_handler(message, reg_name)

def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, name + ' , а какая у тебя фамилия?')
    bot.register_next_step_handler(message, reg_surname)

def reg_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'В каком городе искать вакансии?')
    bot.register_next_step_handler(message, reg_city)

def reg_city(message):
    global city
    city = message.text
    # пересчет
    bot.send_message(message.from_user.id, 'В ' + textQuantityVacancies + ' по городу ' + str(city))

    #выбор удаленной работы
    keyboard = types.InlineKeyboardMarkup()
    key_office = types.InlineKeyboardButton(text='офис', callback_data='office')
    keyboard.add(key_office)
    key_remote = types.InlineKeyboardButton(text='удаленно', callback_data='remote')
    keyboard.add(key_remote)
    question = "Работа в офисе или удаленно ?"
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    bot.register_next_step_handler(message, reg_experience)

def reg_experience(message):
    # выбор опыта
    keyboard = types.InlineKeyboardMarkup()
    key_junior = types.InlineKeyboardButton(text='junior', callback_data='junior')
    keyboard.add(key_junior)
    key_middle = types.InlineKeyboardButton(text='middle', callback_data='middle')
    keyboard.add(key_middle)
    key_senior = types.InlineKeyboardButton(text='senior', callback_data='senior')
    keyboard.add(key_senior)
    question = "Какую позицию ты рассматриваешь (опыт работы)?"
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    bot.register_next_step_handler(message, reg_techno)

def reg_techno(message):
    bot.send_message(message.from_user.id, 'Напиши ключевые технологии, которыми владеешь')
    global technology
    technology = message.text
    bot.send_message(message.from_user.id, 'Отлично. Сейчас поищем результат для ' + technology)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "office":
        # пересчет
        bot.send_message(call.message.chat.id, 'Сейчас в ' + textQuantityVacancies + ' офисной работы')
    elif call.data == "remote":
        # пересчет
        bot.send_message(call.message.chat.id, 'Сейчас в ' + textQuantityVacancies + ' удаленной работы')
    elif call.data == "junior":
        # пересчет
        bot.send_message(call.message.chat.id, 'Сейчас в ' + textQuantityVacancies + ' для junior-разработчика')
    elif call.data == "middle":
        # пересчет
        bot.send_message(call.message.chat.id, 'Сейчас в ' + textQuantityVacancies + ' для middle-разработчика')
    elif call.data == "senior":
        # пересчет
        bot.send_message(call.message.chat.id, 'Сейчас в ' + textQuantityVacancies + ' для senior-разработчика')

bot.infinity_polling()