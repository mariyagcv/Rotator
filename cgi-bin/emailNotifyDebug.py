import mysql.connector
from datetime import timedelta, date, datetime


global connection
global cursor

def dailyEmailNotifications():

  # some needed housekeeping
  
  connection = mysql.connector.connect(
    user="mbyxadr2", database="2017_comp10120_z8", password="fA+h0m5_", host = "dbhost.cs.man.ac.uk"
    )
  cursor= connection.cursor(buffered=True)


  # send the notifications
  #calculate day difference (to an hour)
  cursor.execute("SELECT Deadline FROM User_Task_Log WHERE Submitted = 0" 
                         )
  deadlines = cursor.fetchall()
  cursor.execute("SELECT User_ID FROM User_Task_Log WHERE Submitted = 0" 
                         )
  user_ids = cursor.fetchall()

  oneDayPriorSubject = "Tomorrow's Deadline"
  deadlineDaySubject = "Today's Deadline"
  oneDayAfterSubject = "Missed Deadline"
  i = 0


  for deadline in deadlines:

    
    notificationDeadline = timedelta(days=((datetime.now().date() - deadline[0].date()).days))


    print notificationDeadline.days
  
  cursor.close()
  connection.close()

