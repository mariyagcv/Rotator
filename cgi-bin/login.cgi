import mysql.connector
import bcrypt
import cgi

dataField = cgi.FieldStorage()

username = dataField.getvalue('username')
password = dataField.getvalue('password')

password = bcrypt.hashpw(password, bcrypt.gensalt())

connection = mysql.connector.connect(
    user="mbyxadr2", database="2017_comp10120_z8", password="fA+h0m5_", host = "dbhost.cs.man.ac.uk"
    )

cursor= connection.cursor()

cursor.execute("SELECT Password_Hash FROM User WHERE Name = %s " % username)
hashed = cursor.fetchall()[0]
if bcrypt.checkpw(password, hashed):
  #login succesful - HTML pls
else:
  #login failed - HTML pls

cursor.close()
connection.close()
