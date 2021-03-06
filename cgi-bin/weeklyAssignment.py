from assigningTasksWeekly import query, rank
import mysql.connector
import schedule
from datetime import datetime
from threading import Timer
from emailResponses import dailyEmailNotifications, mailResponseToSubmit, mailResponseToVerify
import time

#tasks assignment
def run():
  connection = mysql.connector.connect(
  user="mbyxadr2", database="2017_comp10120_z8", password="fA+h0m5_", host = "dbhost.cs.man.ac.uk"
  )
  cursor= connection.cursor(buffered=True)
  cursor.execute("SELECT ID FROM WorkGroup")
  groups = cursor.fetchall()
  for group in groups:
    rank(group[0], datetime.now() )
    query(group[0], datetime.now() )
  
  cursor.close()
  connection.close()

#daily deadline reminders
def runDaily():
  dailyEmailNotifications()

#'constant' submit/verify notifications
def runHourly():
  connection = mysql.connector.connect(
  user="mbyxadr2", database="2017_comp10120_z8", password="fA+h0m5_", host = "dbhost.cs.man.ac.uk"
  )
  cursor= connection.cursor(buffered=True)

  # handle submitions
  cursor.execute("SELECT User_ID FROM User_Task_Log WHERE Submitted = 1 AND Submit_Sent = 0")
  submitted_ids = cursor.fetchall()
  for id in submitted_ids:
    mailResponseToSubmit(id[0])
  cursor.execute("UPDATE User_Task_Log SET Submit_Sent = 1 WHERE Submitted = 1 AND Submit_Sent = 0;")


  # handle verifications
  cursor.execute("SELECT User_ID FROM User_Task_Log WHERE Verified = 1 AND Verify_Sent = 0")
  submitted_ids = cursor.fetchall()
  for id in submitted_ids:
    mailResponseToVerify(id[0])
  cursor.execute("UPDATE User_Task_Log SET Verify_Sent = 1 WHERE  Verified = 1 AND Verify_Sent = 0;")

  connection.commit()
  cursor.close()
  connection.close()


    
schedule.every().monday.at('00:01').do(run)
schedule.every().day.at('15:15').do(runDaily)

#real thing
#schedule.every().hour.do(runHourly)
#testing
schedule.every(0.5).minutes.do(runHourly)

while 1:
    schedule.run_pending()
    time.sleep(60)
