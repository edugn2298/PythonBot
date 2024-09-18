import pywhatkit
import datetime

def whastapp(number,message):
  now = datetime.datetime.now()

  pywhatkit.sendwhatmsg(number, message, now.hour, now.minute + 2)