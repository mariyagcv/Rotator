import cgi
from datetime import datetime
import mysql.connector
import random

dataField = cgi.FieldStorage()

userId = dataField.getvalue("user_ID")
name = dataField.getvalue("name")
difficulty = dataField.getvalue("difficulty")

connection = mysql.connector.connect(
  user="mbyxadr2", database="2017_comp10120_z8", password="fA+h0m5_", host = "dbhost.cs.man.ac.uk"
  )

cursor = connection.cursor(buffered=True)

cursor.execute("SELECT Group_ID FROM User_Group_Log WHERE User_ID = %s" % (userId) )

groupId = cursor.fetchall()[0]

randomId = random.randint(1, 8388607)
cursor.execute("SELECT ID FROM User WHERE ID = %s" % randomId)
while(cursor.rowcount):
  randomId = random.randint(1, 8388607)
  cursor.execute("SELECT ID FROM User WHERE ID = %s" % randomId)
  
cursor.execute("INSERT INTO Task(ID, Name, Difficulty, Group_ID) VALUES (%s, %s, %s, %s)" % (randomId, name, difficulty, groupId) )
connection.commit()
cursor.close()
connection.close()

print "" #HTML to redirect/close or whatever
