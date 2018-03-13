import cgi
import mysql.connector

dataField = cgi.FieldStorage()

userId = dataField.getvalue("user_ID")

connection = mysql.connector.connect(
  user="mbyxadr2", database="2017_comp10120_z8", password="fA+h0m5_", host = "dbhost.cs.man.ac.uk"
  )

cursor = connection.cursor(buffered = True)

cursor.execute("SELECT Group_ID FROM User_Group_Log WHERE User_ID = %s" % (userId) )

group_Id = cursor.fecthall()[0][0]

cursor.execute("SELECT Name, Difficulty FROM Task WHERE Group_ID - %s" % (group_Id) )

tasks = cursor.fetchall() # tasks contains now tuples in form (name, diff)

print "" #HTML here

cursor.close()
connection.close()
