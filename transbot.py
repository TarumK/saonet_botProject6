import telebot
import scrap
# Создаем экземпляр бота
bot = telebot.TeleBot('6263282365:AAHyuz23Pmnt1cCzyXYoDnvugp_2d41tczI')
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Русско-черкесский бот-переводчик. v0.1(beta)\n'
                                'Обратная связь и претензии: kyabishev72@gmail.ru\n'
                                'Наберите слово на русском языке...')
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, (scrap.translate(message.text)).capitalize())
    # bot.send_message(message.chat.id, 'Перевод: ' + (scrap.translate(message.text)).title())
    # bot.send_message(message.chat.id, f'Длина вашего сообщения: {len(message.text)}')
# Запускаем бота
bot.polling(none_stop=True, interval=0)