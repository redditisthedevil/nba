from NBABot import NBABot
import sys

bot = NBABot()

while(True):
    try:
        bot.update_gamethreads()
        bot.sleep(600)
    except:
        print('HOLY SHIT AN EXCEPTION!!!!!!')
        print ('Error: ', sys.exc_info())
        bot.sleep(120) #try again in 2 min


