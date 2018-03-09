import cgi
from datetime import datetime
import mysql.connector
from Rotator import LongerTask

dataField = cgi.FieldStorage()

userId = dataField.getvalue("user_ID")

connection = mysql.connector.connect(
  user="mbyxadr2", database="2017_comp10120_z8", password="fA+h0m5_", host = "dbhost.cs.man.ac.uk"
  )

cursor = connection.cursor(buffered = True)
cursor.execute("SELECT User_Task_Log.Task_ID, User_Task_Log.Deadline, User_Task_Log.Submitted, User_Task_Log.Submitted_Date, User_Task_Log.Verified, User_Task_Log.Verified_Date FROM User_Task_Log INNER JOIN User ON User_Task_Log.User_ID = User.ID WHERE User.User_ID = %s" % (userId) )
output = cursor.fetchall()

tasks = []

for element in output:
  cursor.execute("SELECT Name, Difficulty FROM Task WHERE ID = %s" %(element[0]))
  output2 = cursor.fetchall()[0]
  task = LongerTask(element[0], output2[0], output2[1], element[1], element[2], element[3], element[4], element[5])
  tasks.append(task)


cursor.close()
connection.close()

print ""#HTML to here <3
