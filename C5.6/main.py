import telebot
import traceback
from extensions import APIException, Convert
from config import TOKEN, keys

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message):
    text = f"Приветствую, {message.chat.first_name}! Чтобы начать работу введите команду в следующем формате:\n" \
           f"<имя валюты> <в какую валюту перевести> <количество переводимой валюты>\n" \
           f"Вы можете увидеть список всех доступных валют введя команду /values"
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message):
    _list = message.text.split(' ')
    try:
        if len(_list) != 3:
            raise APIException('Неверное количество параметров')

        result = Convert.get_price(*_list)
    except APIException as e:
        bot.reply_to(message, f"Ошибка:\n{e}")
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        bot.reply_to(message, f"Неизвестная ошибка:\n{e}")
    else:
        bot.reply_to(message, result)


bot.polling(non_stop=True)