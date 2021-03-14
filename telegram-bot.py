from telegram import *
from telegram.ext import *

bot=Bot("1615689344:AAFuaWDIiHk1HTwIFaTaXJ4UXuyHgAbvG7A")
print(bot.get_me())
updater=Updater("1615689344:AAFuaWDIiHk1HTwIFaTaXJ4UXuyHgAbvG7A",use_context=True)
dispatcher=updater.dispatcher

def test_function(update:Update,context:CallbackContext):
    bot.send_message(chat_id=update.effective_chat.id,text=f"Hello this is {bot.username} how can I help you \nHere are some command  such as \n**\n/start\n/my_project\n/my_portfolio\n/bye\n/end\n**",)


start_value=CommandHandler('start',test_function)
dispatcher.add_handler(start_value)


def test_function1(update:Update,context:CallbackContext):
    bot.send_message(chat_id=update.effective_chat.id,text=f"Yes Sure...Bye  {bot.commands}",)


start_value=CommandHandler('bye',test_function1)
dispatcher.add_handler(start_value)



def test_function1(update:Update,context:CallbackContext):
    bot.send_message(chat_id=update.effective_chat.id,text=f"Nice To meet You...  {bot.close}",)


start_value=CommandHandler('end',test_function1)
dispatcher.add_handler(start_value)



def test_function1(update:Update,context:CallbackContext):
    bot.send_message(chat_id=update.effective_chat.id,text=f"Here is My Portfolio....\nhttps://bit.ly/3r0IBZi")


start_value=CommandHandler('my_portfolio',test_function1)
dispatcher.add_handler(start_value)

def test_function1(update:Update,context:CallbackContext):
    bot.send_message(chat_id=update.effective_chat.id,text=f"Here is My Porject....\nhttps://bit.ly/2OUGpUU")


start_value=CommandHandler('my_project',test_function1)
dispatcher.add_handler(start_value)


def test_function1(update:Update,context:CallbackContext):
    bot.send_message(chat_id=update.effective_chat.id,text=f"Here {update.poll}")


start_value=CommandHandler('my',test_function1)
dispatcher.add_handler(start_value)
updater.start_polling()
