import bcrypt
import cgi
import mysql.connector
import random
import rotator


dataField = cgi.FieldStorage()

password = dataField.getvalue("password")
password = bcrypt.hashpw(password, bcrypt.gensalt())

connection = mysql.connector.connect(
    user="mbyxadr2", database="2017_comp10120_z8", password="fA+h0m5_", host = "dbhost.cs.man.ac.uk"
    )

cursor= connection.cursor()

randomId = random.randint(1, 16777216)
cursor.execute("SELECT ID FROM User WHERE ID = %s" % randomId)
while(cursor.rowcount):
  randomId = random.randint(1, 16777216)
  cursot.execute("SELECT ID FROM User WHERE ID = %s" % randomId)
  
cursor.execute("""
INSERT INTO User (ID, Name, Password_Hash, E-mail, Phone)
VALUES (%s, %s, %s, %s, %s) 
""" % randomId, dataField.getvalue("name"), password, dataField.getvalue("e-mail"),
dataField.getvalue("phone"))

#some HTML here probably ^^


cursor.close()
connection.close()
