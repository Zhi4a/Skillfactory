import telebot
import requests
import json

bot = telebot.TeleBot('TOKEN')


keys = {
    'доллар': 'USD',
    'евро': 'EUR',
    'рубль': 'RUB'
}

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
    f, t, a = message.text.split(' ')
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={t}&from={f}&amount={a}"
    r = requests.get(url, {"apikey": "key"})
    resp = json.loads(r.content)
    text = f"{a} {f} = {resp['result']} {t}"
    bot.reply_to(message, text)


bot.polling(non_stop=True)