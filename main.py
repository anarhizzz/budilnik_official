import telebot
import datetime
import time
from cgf import*
bot=telebot.TeleBot(TOKEN)
def set_alarm(alert_time):
    now=datetime.datetime.now()
    alarm_time =datetime.datetime.combine(now.date(), alert_time)
    time_diff=(alarm_time-now).total_seconds()
    time.sleep(time_diff)
    bot.send_message(chat_id="", text='GEEEEET UP AND GO TO THE GYYYM')
@bot.message_handler(commands=['set_alarm'])
def set_alarm_command(message):
    try:
        time_str=message.text.split(' ')[1]
        alarm_time=datetime.datetime.strptime(time_str, '%H:%M').time()
        set_alarm(alarm_time)
    except Exception as error:
        bot.send_message( 'revbc' )
bot.polling()

