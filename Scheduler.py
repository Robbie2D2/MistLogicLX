import schedule
import time
import datetime

Mist = 3
Wait = 5

def EndTime():
    print "Turn Off Pump End ",datetime.datetime.now()
    return schedule.clear("Event 1")
    #schedule.clear("Event 1")
    #schedule.cancel_job(OnPump)
    #schedule.cancel_job(OffPump)

def OnPump(t):
    print "Turn On Pump ",datetime.datetime.now()
    schedule.every(Mist).seconds.do(OffPump,Mist).tag("Event 1")
    return schedule.CancelJob
    #return schedule.cancel_job(OnPump)

def OffPump(t):
    print "Turn Off Pump ",datetime.datetime.now()
    schedule.every(Wait).seconds.do(OnPump,Wait).tag("Event 1")
    #schedule.every(Mist.seconds.do(OffPump,Mist)
    return schedule.CancelJob

#schedule.every(Mist).seconds.do(OnPump,Mist)
schedule.every().day.at("23:27").do(OnPump,Mist)
schedule.every().day.at("23:28").do(EndTime)
#schedule.every(2).seconds.do(job,2)

#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)


while True:
    schedule.run_pending()
    #schedule.run_continuously(1)
    #time.sleep(1)
