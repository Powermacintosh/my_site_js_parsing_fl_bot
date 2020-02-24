from telegram import Bot
from telegram import Update
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.utils.request import Request
import json
from telegram import ParseMode
from time import sleep
import datetime
import sqlite3



# --------------------------- sqlite3 -------------------------------
# def sql_request(sql_req):
    # zapros = ('SELECT * FROM pars_fl')
    # zapros = ('SELECT * FROM pars_fl WHERE show LIKE "%парс%"')
    # zapros = ('SELECT * FROM pars_fl WHERE date_p="{}"').format(datetime.date.today())
    # zapros = ('SELECT * FROM pars_fl WHERE date_p="{}" AND time_p > "16:30"').format(datetime.date.today())
    # zapros = ('SELECT * FROM pars_fl WHERE date_p="{}" AND time_p > "15:00" ORDER BY time_p').format(datetime.date.today())
    # zapros = ('SELECT * FROM pars_fl WHERE date_p="{}" AND show LIKE "%парс%" ORDER BY time_p').format(datetime.date.today())
    # zapros = ('SELECT * FROM pars_fl WHERE show LIKE "%арс%" OR ref_link LIKE "%Django%" ORDER BY date_p, time_p')
    # zapros = ('SELECT * FROM pars_fl WHERE show LIKE "%арс%" ORDER BY date_p, time_p')
# --------------------------- sqlite3 -------------------------------
def sql_fetch(con):
    old_max_id = open('txt/sql_id.txt').read().split('\n')[0]
    # print(old_max_id)
    db = []
    db_id = []
    sql_request = ('SELECT * FROM pars_fl WHERE show LIKE "%арс%" OR show LIKE "%jang%" OR ref_link LIKE "%арс%" OR ref_link LIKE "%jang%" ORDER BY date_p, time_p')
    cursorObj = con.cursor()
    cursorObj.execute(sql_request)
    rows = cursorObj.fetchall()
    for index, row in enumerate(rows):
        # print(row)
        # if index in [1, 2, 3]:
        for index, i in enumerate(row):
            # print(index, i)
            if index == 0:
                db_id_t = i
            if index == 2:
                link = i 
            if index == 3:
                show = i
            if index == 4:
                body = i
            if index == 5:
                date = i
            if index == 6:
                time = i
            if index == 8:
                price = i
        line = '--------------------------- sql -------------------------------'
        text = '<b>' + show + '</b>' + '\n' + '<i>' + 'Оплата: ' + price + '</i>' + '\n' + body + '\n' + '<b><i>' + date + ' ' + time + '</i></b>' + '\n' + link + '\n' + line
        # text = price + '\n' + link + '\n' + date + ' ' + time
        if db_id_t > int(old_max_id):
            # print(db_id_t)
            # print(text)
            db_id.append(db_id_t)
            db.append(text)
    
    # print('db_id', db_id)
    # print(text)
    try:
        max_id = refind_db_id(db_id)
    except:
        max_id = old_max_id
    m = str(max_id)
    text_a = m.split('\n')
    with open(r"txt/sql_id.txt", "w") as file:
        file.writelines("%s\n" % line for line in text_a)
    return db
# --------------------------- sqlite3 -------------------------------
def refind_db_id(db_id):
    # print(len(db_id))
    # print(db_id)
    max_db_id = max(db_id)
    # print(max_db_id)
    return max_db_id



button_Parsing = 'Поиск заказов по парсингу'


def log_error(f):

    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            print(f'Ошибка: {e}')
            raise e

    return inner


def button_Parsing_handler(update: Update, context: CallbackContext):
    con = sqlite3.connect('db.sqlite3')
    while True:
        sql_message = sql_fetch(con)
        if sql_message != '':
            # print(sql_message)
            for i in sql_message:
                sleep(2)
                try:
                    update.message.reply_text(
                        text="{}".format(i),
                        disable_web_page_preview = True,
                        parse_mode=ParseMode.HTML,
                        reply_markup=ReplyKeyboardRemove(),
                    )
                except:
                    print('except: button_Parsing_handler')
                    print(i.split('</i></b>')[1])
                    print(i)
                    continue
        sleep(3)


@log_error
def message_handler(update: Update, context: CallbackContext):
    text = update.message.text
    if text == button_Parsing:
        return button_Parsing_handler(update=update, context=context)
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
        [
                KeyboardButton(text=button_Parsing),
            ],
        ],
        resize_keyboard=True,
        )
    update.message.reply_text(
        text="Бот агрегатор фриланс бирж",
        reply_markup=reply_markup,
        )



def main():

    print('Start')

    req = Request(
        connect_timeout=0.5,
    )
    bot = Bot(
        request=req,
        token='929657905:AAE49SUBEZmO_mLi29QM-LqEybelJ5ClPhc',
        base_url='https://telegg.ru/orig/bot',
    )
    updater = Updater(
        bot=bot,
        use_context=True,
    )
    print(updater.bot.get_me())

    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))

    updater.start_polling()
    updater.idle()

    print('Finish')


if __name__ == '__main__':
    main()
