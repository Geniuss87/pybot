import telebot
from decouple import config
from telebot import types

bot = telebot.TeleBot(config("TOKEN_BOT"))

@bot.message_handler(commands=["start", "hi!"])
def get_start_msg(msg):
    full_name = f"{msg.from_user.last_name} {msg.from_user.first_name}"
    text = f"Welcome {full_name}"
    bot.send_message(msg.chat.id, text)

@bot.message_handler(content_types=["text"])
def get_msg(msg):
    markup = types.InlineKeyboardMarkup(row_width=2)
    if msg.text.lower() == "menu":
        text = "Please, choose:"
        btn_1 = types.InlineKeyboardButton("Coffee", callback_data="Coffee")
        btn_2 = types.InlineKeyboardButton("Tea", callback_data="Tea")
        markup.add(btn_1, btn_2)
        bot.send_message(msg.chat.id, text, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def get_callback_data(call):
    global text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if call.data == "Tea":
        text = f"Choose tea"
        btn_1 = types.KeyboardButton("black")
        btn_2 = types.KeyboardButton("green")
        btn_3 = types.KeyboardButton("fruit")
        markup.add(btn_1, btn_2, btn_3)
    if call.data == "Coffee":
        text = f"Choose coffee"
        btn_1 = types.KeyboardButton("Americano")
        btn_2 = types.KeyboardButton("Espresso")
        btn_3 = types.KeyboardButton("Latte")
        markup.add(btn_1, btn_2, btn_3)

    bot.send_message(call.message.chat.id, text, reply_markup=markup)









bot.polling()