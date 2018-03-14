import cgi
import mysql.connector

dataField = cgi.FieldStorage()

userId = dataField.getvalue("user_ID")
name = dataField.getvalue("name")
email = dataField.getvalue("email")
phone = dataField.getvalue("phone")

connection = mysql.connector.connect(
  user="mbyxadr2", database="2017_comp10120_z8", password="fA+h0m5_", host = "dbhost.cs.man.ac.uk"
  )

cursor = connection.cursor(buffered = True)

cursor.execute("UPDATE User SET Name = %s, E-mail = %s, Phone = %s WHERE ID = %s" % (name, email, phone, userId)
connection.commit()

#probably we should have some HTML here or just close the tab ???

cursor.close()
connection.close()
