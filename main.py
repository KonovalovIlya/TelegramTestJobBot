from time import sleep

import telebot.types as types
from telebot import TeleBot
from telebot.types import Message
from datetime import datetime
import pytz


moscow_time = datetime.now(pytz.timezone('Europe/Moscow')).strftime('%H')
tb = TeleBot(token='7012017137:AAHAN3aNP032eItm8FZGhXoZ9zTN4fSA0Nw')
image_list = [
    'https://www.istockphoto.com/ru/%D1%84%D0%BE%D1%82%D0%BE/%D0%B4%D0%BE%D1%81%D0%BA%D0%B0-%D0%B4%D0%BB%D1%8F-%D1%81%D0%B5%D1%80%D1%84%D0%B8%D0%BD%D0%B3%D0%B0-%D0%B8-%D0%BF%D0%B0%D0%BB%D1%8C%D0%BC%D0%B0-%D0%BD%D0%B0-%D0%BF%D0%BB%D1%8F%D0%B6%D0%B5-%D0%BB%D0%B5%D1%82%D0%BE%D0%BC-gm1370813651-440284328',
    'https://www.istockphoto.com/ru/%D1%84%D0%BE%D1%82%D0%BE/%D0%BC%D0%B0%D0%BB%D1%8C%D0%B4%D0%B8%D0%B2%D1%8B-%D1%82%D1%80%D0%BE%D0%BF%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9-%D0%BE%D1%81%D1%82%D1%80%D0%BE%D0%B2-gm1360554439-433537932',
    'https://www.istockphoto.com/ru/%D1%84%D0%BE%D1%82%D0%BE/%D1%82%D1%80%D0%BE%D0%BF%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9-%D0%BF%D0%BB%D1%8F%D0%B6-%D0%BF%D0%B0%D0%BB%D1%8C%D0%BC%D1%8B-%D0%BC%D0%BE%D1%80%D1%81%D0%BA%D0%B0%D1%8F-%D0%B2%D0%BE%D0%BB%D0%BD%D0%B0-%D0%B8-%D0%B1%D0%B5%D0%BB%D1%8B%D0%B9-%D0%BF%D0%B5%D1%81%D0%BE%D0%BA-gm1300296030-392666571',
]
polls = {}


def send_poll(chat_id):
    q_list = ['Первая строка', 'Вторая строка', 'Третья строка', 'Четвертая строка']
    if int(moscow_time) < 13:
        tb.send_poll(
            chat_id=chat_id,
            options=q_list,
            allows_multiple_answers=True,
            question='Выбери несколько вариантов',
            type='regular',
            is_anonymous=False,
        )
    else:
        tb.send_poll(
            chat_id=chat_id,
            options=list(reversed(q_list)),
            allows_multiple_answers=True,
            question='Выбери несколько вариантов',
            type='regular',
            is_anonymous=False,
        )


def send_photo_gallery(chat_id):
    media_group = []
    for i in image_list:
        media_group.append(types.InputMediaPhoto(media=i))

    tb.send_media_group(chat_id=chat_id, media=media_group)


@tb.message_handler(commands=['start'])
def wellcome(message: Message):
    """Приветствует пользователя"""
    tb.send_message(message.chat.id, 'Привет')
    sleep(5)
    send_photo_gallery(message.chat.id)
    sleep(5)
    send_poll(message.chat.id)


@tb.poll_answer_handler()
def handle_poll_answer(poll_answer: types.PollAnswer):
    global polls
    poll_id = int(poll_answer.poll_id)
    user_id = poll_answer.user.id
    answers = poll_answer.option_ids
    if poll_id in polls and user_id in polls[poll_id]:
        polls[poll_id][user_id] = answers
    else:
        polls[poll_id] = {user_id: answers}


@tb.poll_handler(lambda active_poll: active_poll.is_closed is True)
def just_poll_answer(active_poll: types.Poll):
    global polls
    print(polls)


tb.polling(non_stop=True)
