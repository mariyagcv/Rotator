from datetime import timedelta, date, datetime
import mysql.connector
import random
from rotator import Task, SimpleUser, User, User_Group_Log, User_Task_Log

# A few definitions
  
def compareId(idToCompare):
  return groupID == idToCompare

def bubble_sort_users(users): #sorts users in ascending order of score
    for i in range(0, len(users) - 2):
        for j in range(i, len(users) - 1):
            if(users[j].workScore > users[j+1].workScore):
                tempUser = users[j]
                users[j] = users[j+1]
                users[j+1] = tempUser

def bubble_sort_tasks(tasks): #sorts tasks in asc. order of difficulty
    for i in range(len(tasks) - 1, 0, -1):
        for j in range(i):
            if(tasks[j].difficulty < tasks[j+1].difficulty):
                tempTask = tasks[j]
                tasks[j] = tasks[j+1]
                tasks[j+1] = tempTask
                
def addTaskToUser(task, user):
  user.add_task(task)

def assignTasksToUsers(tasks, users):
  dayShift = dateOfCall.weekday()
  dateShift = timedelta(days = (5 - dayShift))
  deadlineArray = []
  for i in range(0, 9):
    if(i == 0):
      dateToAdd = dateOfCall + dateShift
      dateTemp = datetime(dateToAdd.year, dateToAdd.month, dateToAdd.day, 12, 0)      
    elif(i == 1):
      dateToAdd = dateOfCall + dateShift
      dateTemp = datetime(dateToAdd.year, dateToAdd.month, dateToAdd.day, 18, 0)      
    elif(i == 2):
      dateShift2 = dateShift + timedelta(days = 1)
      dateToAdd = dateOfCall + dateShift2
      dateTemp = datetime(dateToAdd.year, dateToAdd.month, dateToAdd.day, 12, 0)      
    elif(i == 3):
      dateShift2 = dateShift + timedelta(days = 1)
      dateToAdd = dateOfCall + dateShift2
      dateTemp = datetime(dateToAdd.year, dateToAdd.month, dateToAdd.day, 18, 0) 
    else:
      dateShift2 = dateShift - timedelta(days = (9 - i))
      dateToAdd = dateOfCall + dateShift2
      dateTemp = datetime(dateToAdd.year, dateToAdd.month, dateToAdd.day, 18, 0) 
      
    deadlineArray.append(dateTemp)
          
  for i in range(0, len(tasks)):
    x = i
    if(x >= len(users)):
      x = x - len(users)
  #  tasks[i].deadline = deadlineArray[i]
   # users[x].add_task(tasks[i])
    #add the assignment of task to db
    #deadlineStr = deadlineArray[i].date().isoformat()
    deadlineStr = deadlineArray[len(users[x].userTasks)].strftime("%Y-%m-%d %H:%M:%S")
    randomId = random.randint(1, 8388607)
    cursor.execute("SELECT ID FROM User_Task_Log WHERE ID = %s" % randomId)
    while(cursor.rowcount ):
      randomId = random.randint(1, 8388607)
      cursor.execute("SELECT ID FROM User_Task_Log WHERE ID = %s" % randomId)

    tasks[i].deadline = deadlineStr
    users[x].add_task(tasks[i])
    data = [randomId, deadlineStr, users[x].id, tasks[i].id]
    cursor.execute("INSERT INTO User_Task_Log(ID, Deadline, User_ID, Task_ID) VALUES (%s, %s, %s, %s)", (data) )
    connection.commit()


#Actual code starts here:
def query(new_groupID, new_dateOfCall):
  groupID = new_groupID
  global dateOfCall
  dateOfCall = new_dateOfCall
  global connection
  connection = mysql.connector.connect(
    user="mbyxadr2", database="2017_comp10120_z8", password="fA+h0m5_", host = "dbhost.cs.man.ac.uk"
    )
  global cursor
  cursor= connection.cursor(buffered=True)
  cursor.execute("SELECT Task.ID, Task.Name, Task.Difficulty FROM Task WHERE Task.Group_ID = %s ORDER BY Task.Difficulty DESC" % groupID
                         )#MySQL query for SELECTing TASKs from the database
  tasks = cursor.fetchall()
  newTasks = []
  
  for element in tasks:
    task = Task(element[0], element[1], element[2], groupID)
    newTasks.append(task)
  
  tasks = newTasks

#  cursor.execute("SELECT Task.Name, Task.Difficulty, User_Task_Log.Deadline, User_Task_Log.Submitted, User_Task_Log.Submitted_Date, User_Task_Log.Verified, User_Task_Log.Verified_Date FROM User_Task_Log INNER JOIN Task ON User_Task_Log.Task_ID = Task.ID WHERE Task.Group_ID = %s ORDER BY Task.Difficulty ASC" % groupID) #MySQL query for SELECTing USER of the group form the db

  cursor.execute("SELECT User.ID, User.Name FROM User INNER JOIN User_Group_Log ON User.ID = User_Group_Log.User_ID WHERE User_Group_Log.Group_ID = %s " % groupID
  )

  users = cursor.fetchall()
  newUsers = []
  
  for element in users:
    user = SimpleUser(element[0], element[1])
    newUsers.append(user)
    
  users = newUsers

  assignTasksToUsers(tasks, users)
    #Since we, hopefully, handled adding the tasks to the users
    # we need to update the database, right?

#  for user in users:
 #     print user.name
  #    for userTask in user.userTasks:
   #       print userTask.name
  
  cursor.close()
  connection.close()
  
def rank(new_groupID, new_dateOfCall):
  groupID = new_groupID
  dateOfCall = new_dateOfCall
  connection = mysql.connector.connect(
    user="mbyxadr2", database="2017_comp10120_z8", password="fA+h0m5_", host = "dbhost.cs.man.ac.uk"
    )
  cursor= connection.cursor(buffered=True)
  cursor.execute("SELECT User_ID, WorkScore FROM User_Group_Log WHERE Group_ID = %s" % (groupId) )
  userScores = cursor.fetchall() # (id, score) (id, score) ...
  for user in userScores:
    cursor.execute("SELECT Deadline, Submitted, Submitted_Date, Verified, Verified_Date, Task_ID FROM User_Task_Log WHERE User_ID = %s" % (user[0])
    tasks = cursor.fetchall() # (dead, sub....) (d, s...)
    for task in tasks:
      cursor.execute("SELECT Difficulty FROM Task WHERE ID = %s " % (task[5]) )
      difficulty = cursor.fetchall()[0][0]
      if task[0] > (dateOfCall - timedelta(days = 7)) and task[0] < dateOfCall:
        if task[1] == 1:
          if task[2] < task[0]:
            user[1] += difficulty
          else:
            user[1] -= difficulty
        else:
          user[1] -= difficulty
      #?????
      user[1] -= 1000
      cursor.execute("UPDATE User SET WorkScore = %s WHERE ID = %s" %s  (user[1], user[0])
      connection.commit()
  
