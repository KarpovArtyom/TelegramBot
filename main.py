import telebot
import sqlite3
from telebot import types

bot = telebot.TeleBot('6647728823:AAHVQjeWi0TuSWRK5i5Grq5-Igql4oBusO4')

@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.last_name == None:
        mess = f'Привет, <b>{message.from_user.first_name}</b>! Какая марка вас интересует?'
    else:
        mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>! Какая марка вас интересует?'

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("BMW")
    item2 = types.KeyboardButton("Mercedes-Benz")
    item3 = types.KeyboardButton("Audi")

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)


@bot.message_handler()
def message(message):
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()
    mess = 'Выберите модель данной Марки'
    if message.text == 'BMW':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        item1 = types.KeyboardButton("m5")
        item2 = types.KeyboardButton("X1")
        item3 = types.KeyboardButton("Z4")

        markup.add(item1, item2, item3)

        bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(message, abc)

    elif message.text == 'Mercedes-Benz':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        item1 = types.KeyboardButton("GLA")
        item2 = types.KeyboardButton("G-Class")
        item3 = types.KeyboardButton("E-Class")

        markup.add(item1, item2, item3)

        bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(message, abc)

    elif message.text == 'Audi':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        item1 = types.KeyboardButton("A3")
        item2 = types.KeyboardButton("Q3")
        item3 = types.KeyboardButton("Q6")

        markup.add(item1, item2, item3)

        bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(message, abc)

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("BMW")
        item2 = types.KeyboardButton("Mercedes-Benz")
        item3 = types.KeyboardButton("Audi")

        markup.add(item1, item2, item3)

        bot.send_message(message.chat.id, 'Я не знаю такой марки автомобиля', parse_mode='html', reply_markup=markup)


@bot.message_handler()
def abc(message):
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()

    if message.chat.type == "private":
        if message.text == 'm5':
            result = cursor.execute("SELECT * FROM 'Models' WHERE Model = 'm5'")
            cars = cursor.fetchall()
            info = ''
            for el in cars:
                info += f'Марка: {el[1]}, Модель: {el[2]}, Максимальная скорость: {el[3]} км/ч, Количество мест: {el[4]}, Тип коробки передач: {el[5]}'

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("BMW")
            item2 = types.KeyboardButton("Mercedes-Benz")
            item3 = types.KeyboardButton("Audi")

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, info, reply_markup=markup)
            cursor.close()
            conn.close()

        elif message.text == 'X1':
            result = cursor.execute("SELECT * FROM 'Models' WHERE Model = 'X1'")
            cars = cursor.fetchall()

            info = ''
            for el in cars:
                info += f'Марка: {el[1]}, Модель: {el[2]}, Максимальная скорость: {el[3]} км/ч, Количество мест: {el[4]}, Тип коробки передач: {el[5]}'

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("BMW")
            item2 = types.KeyboardButton("Mercedes-Benz")
            item3 = types.KeyboardButton("Audi")

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, info, reply_markup=markup)
            cursor.close()
            conn.close()

        elif message.text == 'Z4':
            result = cursor.execute("SELECT * FROM 'Models' WHERE Model = 'Z4'")
            cars = cursor.fetchall()

            info = ''
            for el in cars:
                info += f'Марка: {el[1]}, Модель: {el[2]}, Максимальная скорость: {el[3]} км/ч, Количество мест: {el[4]}, Тип коробки передач: {el[5]}'

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("BMW")
            item2 = types.KeyboardButton("Mercedes-Benz")
            item3 = types.KeyboardButton("Audi")

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, info, reply_markup=markup)
            cursor.close()
            conn.close()

        elif message.text == 'GLA':
            result = cursor.execute("SELECT * FROM 'Models' WHERE Model = 'GLA'")
            cars = cursor.fetchall()

            info = ''
            for el in cars:
                info += f'Марка: {el[1]}, Модель: {el[2]}, Максимальная скорость: {el[3]} км/ч, Количество мест: {el[4]}, Тип коробки передач: {el[5]}'

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("BMW")
            item2 = types.KeyboardButton("Mercedes-Benz")
            item3 = types.KeyboardButton("Audi")

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, info, reply_markup=markup)
            cursor.close()
            conn.close()

        elif message.text == 'G-Class':
            result = cursor.execute("SELECT * FROM 'Models' WHERE Model = 'G-Class'")
            cars = cursor.fetchall()

            info = ''
            for el in cars:
                info += f'Марка: {el[1]}, Модель: {el[2]}, Максимальная скорость: {el[3]} км/ч, Количество мест: {el[4]}, Тип коробки передач: {el[5]}'

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("BMW")
            item2 = types.KeyboardButton("Mercedes-Benz")
            item3 = types.KeyboardButton("Audi")

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, info, reply_markup=markup)
            cursor.close()
            conn.close()

        elif message.text == 'E-Class':
            result = cursor.execute("SELECT * FROM 'Models' WHERE Model = 'E-Class'")
            cars = cursor.fetchall()

            info = ''
            for el in cars:
                info += f'Марка: {el[1]}, Модель: {el[2]}, Максимальная скорость: {el[3]} км/ч, Количество мест: {el[4]}, Тип коробки передач: {el[5]}'

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("BMW")
            item2 = types.KeyboardButton("Mercedes-Benz")
            item3 = types.KeyboardButton("Audi")

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, info, reply_markup=markup)
            cursor.close()
            conn.close()

        elif message.text == 'A3':
            result = cursor.execute("SELECT * FROM 'Models' WHERE Model = 'A3'")
            cars = cursor.fetchall()

            info = ''
            for el in cars:
                info += f'Марка: {el[1]}, Модель: {el[2]}, Максимальная скорость: {el[3]} км/ч, Количество мест: {el[4]}, Тип коробки передач: {el[5]}'

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("BMW")
            item2 = types.KeyboardButton("Mercedes-Benz")
            item3 = types.KeyboardButton("Audi")

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, info, reply_markup=markup)
            cursor.close()
            conn.close()

        elif message.text == 'Q3':
            result = cursor.execute("SELECT * FROM 'Models' WHERE Model = 'Q3'")
            cars = cursor.fetchall()

            info = ''
            for el in cars:
                info += f'Марка: {el[1]}, Модель: {el[2]}, Максимальная скорость: {el[3]} км/ч, Количество мест: {el[4]}, Тип коробки передач: {el[5]}'

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("BMW")
            item2 = types.KeyboardButton("Mercedes-Benz")
            item3 = types.KeyboardButton("Audi")

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, info, reply_markup=markup)
            cursor.close()
            conn.close()

        elif message.text == 'Q6':
            result = cursor.execute("SELECT * FROM 'Models' WHERE Model = 'Q6'")
            cars = cursor.fetchall()

            info = ''
            for el in cars:
                info += f'Марка: {el[1]}, Модель: {el[2]}, Максимальная скорость: {el[3]} км/ч, Количество мест: {el[4]}, Тип коробки передач: {el[5]}'

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("BMW")
            item2 = types.KeyboardButton("Mercedes-Benz")
            item3 = types.KeyboardButton("Audi")

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, info, reply_markup=markup)
            cursor.close()
            conn.close()

        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("BMW")
            item2 = types.KeyboardButton("Mercedes-Benz")
            item3 = types.KeyboardButton("Audi")

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, "В моей базе нет такой модели", parse_mode='html', reply_markup=markup)
            cursor.close()
            conn.close()


bot.polling(none_stop=True)