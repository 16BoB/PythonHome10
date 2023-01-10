from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from credits1 import bot_token

from getweather import request_weather
from getweather import url

bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(update.effective_chat.id, f"{update.effective_chat.first_name}, Привет! \nУ меня доступны следующие комманды: \n/gettemperature")

def get_temperature(update, context):
    keyboard = [
        [InlineKeyboardButton('Погода в Москве', callback_data= '1')],
        [InlineKeyboardButton('Погода в Уфе', callback_data= '2')]
    ]
    update.message.reply_text('Выберете действие', reply_markup=InlineKeyboardMarkup(keyboard))

def button(update, context):
    query = update.callback_query
    query.answer()
    if query.data == '1':
        context.bot.send_message(update.effective_chat.id, f'Температура в Москве: {request_weather(url[0])}')
    elif query.data == '2':
        context.bot.send_message(update.effective_chat.id, f'Температура в Уфе: {request_weather(url[1])}')
    

def unknow(update, context):
    context.bot.send_message(update.effective_chat.id, 'Эта комманда мне не известна(')


button_handler = CallbackQueryHandler(button)
start_handler = CommandHandler('start', start)
get_day_handler = CommandHandler('gettemperature', get_temperature)
unknow_handler = MessageHandler(Filters.command, unknow)



dispatcher.add_handler(start_handler)
dispatcher.add_handler(get_day_handler)
dispatcher.add_handler(unknow_handler)
dispatcher.add_handler(button_handler)

updater.start_polling()
updater.idle()