import mysql.connector
import cgi
from assigningTasksWeekly import query

dataField = cgi.FieldStorage()

userId = dataField.getvalue("user_ID")

connection = mysql.connector.connect(
  user="mbyxadr2", database="2017_comp10120_z8", password="fA+h0m5_", host = "dbhost.cs.man.ac.uk"
  )

cursor = connection.cursor(buffered = True)
cursor.execute("SELECT Group_ID FROM User_Group_Log WHERE User_ID = %s" % userId)
groupId = cursor.fetchall()[0]
query(userId, groupId)
#kill the connection to DB
cursor.close()
connection.close()

print ""#HTML to redirect here <3



