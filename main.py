from time import sleep
import time

from telebot import TeleBot
from telebot.types import Message
from countryinfo import CountryInfo


tb = TeleBot(token='7012017137:AAHAN3aNP032eItm8FZGhXoZ9zTN4fSA0Nw')
country = CountryInfo('Russia')
time.


@tb.message_handler(commands=['start'])
def welcome(message: Message):
    """Приветствует пользователя"""
    tb.send_message(message.chat.id, 'Привет')
    sleep(5)
    tb.send_message(message.chat.id, 'Picture gallery message')
    sleep(5)
    msk_time =
    tb.send_message(message.chat.id, 'Picture gallery message')


if __name__ == 'main':
    tb.polling(non_stop=True)
