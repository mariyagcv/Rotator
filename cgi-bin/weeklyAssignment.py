from assigningTasksWeekly import query, rank
import mysql.connector
from datetime import datetime
from threading import Timer

def run():
  connection = mysql.connector.connect(
  user="mbyxadr2", database="2017_comp10120_z8", password="fA+h0m5_", host = "dbhost.cs.man.ac.uk"
  )
  cursor= connection.cursor(buffered=True)
  cursor.execute("SELECT ID FROM WorkGroup")
  groups = cursor.fetchall()
  for group in groups:
    rank(group[0], datetime.now() )
    query(group[0], datetime.now() )
  
  cursor.close()
  connection.close()
    
schedule.every().monday.at('00:01').do(run)
