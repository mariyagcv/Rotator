import cgi
import mysql.connector

dataField = cgi.FieldStorage()

userId = dataField.getvalue("user_ID")

connection = mysql.connector.connect(
  user="mbyxadr2", database="2017_comp10120_z8", password="fA+h0m5_", host = "dbhost.cs.man.ac.uk"
  )

cursor = connection.cursor(buffered = True)

cursor.execute("SELECT Name, E-mail, Phone FROM User WHERE ID = %s" % userId)

details = cursor.fetchall()[0] #details[0] = name, details[1] = email, details[2] = phone

print "" #HTML here


cursor.close()
connection.close()
