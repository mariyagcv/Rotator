import bcrypt
import cgi
import mysql.connector

dataField = cgi.FieldStorage()

userId = dataField.getvalue("user_ID")
password = dataField.getvalue("password")
new_password = bcrypt.hashpw(dataField.getvalue("new_password"), bcrypt.gensalt())

connection = mysql.connector.connect(
  user="mbyxadr2", database="2017_comp10120_z8", password="fA+h0m5_", host = "dbhost.cs.man.ac.uk"
  )

cursor = connection.cursor(buffered = True)

cursor.execute("SELECT Password_Hash FROM User WHERE ID = %s" % userId)

hashed= cursor.fetchall()[0][0]

if bcrypt.checkpw(password, hashed):
  cursor.execute("UPDATE User SET Password_Hash = %s WHERE ID = %s" % (new_password, userId)
  connection.commit()
else
  print "" #wrong password used to change the old password :/
print "" #HTML here


cursor.close()
connection.close()
