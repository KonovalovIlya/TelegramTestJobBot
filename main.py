from time import sleep
from telebot import TeleBot
from telebot.types import Message
from datetime import datetime
import pytz     #   pip install pytz


moscow_time = datetime.now(pytz.timezone('Europe/Moscow')).strftime('%H')
# print(moscow_time)
tb = TeleBot(token='7012017137:AAHAN3aNP032eItm8FZGhXoZ9zTN4fSA0Nw')


@tb.message_handler(commands=['start'])
def welcome(message: Message):
    """Приветствует пользователя"""
    tb.send_message(message.chat.id, 'Привет')
    sleep(5)
    tb.send_message(message.chat.id, 'Picture gallery message')
    sleep(5)
    # msk_time =
    if int(moscow_time) < 13:
        tb.send_message(message.chat.id, 'Moscow time < 13')
    else:
        tb.send_message(message.chat.id, 'Moscow time > 13')


tb.polling(non_stop=True)
# if __name__ == 'main':
#     pass
