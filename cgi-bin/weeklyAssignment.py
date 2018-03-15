from assigningTasksWeekly import query
import mysql.connector
from datetime import datetime


connection = mysql.connector.connect(
user="mbyxadr2", database="2017_comp10120_z8", password="fA+h0m5_", host = "dbhost.cs.man.ac.uk"
)
cursor= connection.cursor(buffered=True)
cursor.execute("SELECT ID FROM WorkGroup")
groups = cursor.fetchall()
for group in groups:
  query(group[0], datetime.now() )
