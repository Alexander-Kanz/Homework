import telebot
import random
from telebot import types

token = '6136739277:AAFnBIMz3QQ45tve0FCbv_SBeuSMo1CA6SA'
bot = telebot.TeleBot(token)

def create_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    drink_btn = types.InlineKeyboardButton(text='Хочу пить', callback_data='1')
    eat_btn = types.InlineKeyboardButton(text='Хочу есть', callback_data='2')
    tell_a_joke = types.InlineKeyboardButton(text='Рассказать анекдот', callback_data='3')
    sleep = types.InlineKeyboardButton(text='Хочу спать', callback_data='4')

    keyboard.add(drink_btn, eat_btn,tell_a_joke,sleep)
    return keyboard

@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id, 'Приветствую. Выберите, что вы хотите: ', reply_markup=create_keyboard())

@bot.message_handler(commands=['end'])
def end_bot(message):
    bot.send_message(message.chat.id, 'До свидания! ')

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.message:
        if call.data == '1':
            img = 'https://upload.wikimedia.org/wikipedia/commons/c/c0/Water_drop_impact_on_a_water-surface_-_%282%29.jpg'
            bot.send_photo(chat_id=call.message.chat.id,photo=img,caption='Картинка воды', reply_markup=create_keyboard())
        if call.data == '2':
            img = 'https://www.ixbt.com/img/n1/news/2021/9/5/d5d11c91b095686fcaa0f14cf8bbb7fa-600x450_large.jpg'
            bot.send_photo(chat_id=call.message.chat.id, photo=img, caption='Картинка еды',reply_markup=create_keyboard())
        if call.data == '3':
            joke = random.randint(1, 4)
            if joke == 1:
                joke = ''' Вопрос: Как взломать банкомат?
Ответ: Берете кувалду, ноутбук, подходите к банкомату, разбиваете его кувалдой и забираете деньги.
Вопрос: А зачем ноутбук?
Ответ: А какой ты нафиг хакер без ноутбука?'''
            elif joke == 2:
                joke = '''День, когда Микрософт выпустит хоть что-то, что не будет тормозить, будет днем, когда они начнут производить автомобили'''
            elif joke == 3:
                joke = '''Разговор двух программистов:
- Что пишешь?
- Сейчас запустим - узнаем!'''
            elif joke == 4:
                joke = '''- "Hе" с глаголами пишется вместе или отдельно?
- Через пробел!'''
            bot.send_message(chat_id=call.message.chat.id,text=joke,reply_markup=create_keyboard())
        if call.data == '4':
            img = 'https://png.pngtree.com/element_our/20190528/ourmid/pngtree-world-sleep-day-child-sleeping-image_1148840.jpg'
            bot.send_photo(chat_id=call.message.chat.id, photo=img, caption='Сон', reply_markup=create_keyboard())

bot.polling(none_stop=True)
