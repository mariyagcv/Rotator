import cgi
from datetime import datetime
import mysql.connector

dataField = cgi.FieldStorage()

userTaskId = dataField.getvalue("user_task_ID")

connection = mysql.connector.connect(
  user="mbyxadr2", database="2017_comp10120_z8", password="fA+h0m5_", host = "dbhost.cs.man.ac.uk"
  )

cursor = connection.cursor(buffered = True)
cursor.execute("UPDATE User_Task_Log SET Verified = 1, Verified_Date = %s WHERE ID = %s" % (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), userTaskId) )
#kill the connection to DB
connection.commit()
cursor.close()
connection.close()

print ""#HTML to redirect here <3
