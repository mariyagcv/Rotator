import mysql.connector
import cgi

dataField = cgi.FieldStorage()

userId = dataField.getvalue("user_ID")

connection = mysql.connector.connect(
  user="mbyxadr2", database="2017_comp10120_z8", password="fA+h0m5_", host = "dbhost.cs.man.ac.uk"
  )

