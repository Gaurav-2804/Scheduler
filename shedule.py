import pandas as pd
import datetime
from plyer import notification
import time


def sendnot(msg):
    notification.notify(
        title = msg,
        message = "Study Hard",
        app_icon = "./book.ico",
        timeout = 5
    )

if __name__ == "__main__":
    df = pd.read_excel("Tt.xlsx")
    #print(df)
    while True:                       # to continue program
        now = datetime.datetime.now().strftime("%H:%M")
        day = datetime.datetime.now().strftime("%A")
        
        for index, item in df.iterrows():
            #print(index, item['Time'])
            tm = item['Time'].strftime("%H:%M")
            dy = item['Day']
            msg = item['Subject']
            if(dy == day):
                if(tm == now):
                    sendnot(msg)
    time.sleep(60*60)            #program will run for every 1 hr

    # instead of while loop you can use task scheduler in your OS to run your program every time you turn your system on
    # Also you can run pythonw .\shedule.py so that even if you turn off terminal code will run