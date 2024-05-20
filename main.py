from telebot import types
import telebot

token = '7176525161:AAHDhcLYdCiOlto-8ZjmQc0YL5R0fpxJd9c'
bot = telebot.TeleBot(token)
my_chat_id = 855225430


@bot.message_handler(commands=["start"])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Услуги")
    button2 = types.KeyboardButton(text="О нас")
    button3 = types.KeyboardButton(text="Оставить заявку")
    keyboard.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Приветствуем! Добро пожаловать на наш сайт!', reply_markup=keyboard)


def info_func(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на сайт", url="https://vk.com/")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Информация о компании", reply_markup=keyboard)


def send_request(message):
    mes = f'Новая заявка: {message.text}'
    bot.send_message(my_chat_id, mes)
    bot.send_message(message.chat.id, 'Спасибо за заявку! Наши специалисты скоро с вами свяжутся!')


def send_service(message):
    bot.send_message(message.chat.id, '1. VK Реклама\n2. Для бизнеса\n3. Все продукты')


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text.lower() == 'о нас':
        info_func(message)
    elif message.text.lower() == 'оставить заявку':
        bot.send_message(message.chat.id, 'Будем рады вас обслужить! Оставьте свои контактные данные.')
        bot.register_next_step_handler(message, send_request)
    elif message.text.lower() == 'услуги':
        send_service(message)



if __name__ == '__main__':
    bot.infinity_polling()
