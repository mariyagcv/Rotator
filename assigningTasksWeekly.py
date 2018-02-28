import mysql.connector
from datetime import timedelta, date, datetime
from rotator import Task, User, User_Group_Log, User_Task_Log

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
    if(tasks[i].compareIdWithUser(users[x])):
      tasks[i].deadline = deadlineArray[i]
      users[x].add_task(tasks[i])
   # else:
     #   print "Error: There is a user (or a task) with a different group id!"


#Actual code starts here:
def query(new_groupID, new_dateOfCall):
  global groupID
  groupID = new_groupID
  global dateOfCall
  dateOfCall = new_dateOfCall
  connection = mysql.connector.connect(
    user="mbyxadr2", database="2017_comp10120_z8", password="fA+h0m5_", host = "dbhost.cs.man.ac.uk"
    )

  cursor= connection.cursor()
  cursor.execute("SELECT Task.ID, Task.Name, Task.Difficulty FROM Task WHERE Task.Group_ID = %s ORDER BY Task.Difficulty DESC" % groupID
                         )#MySQL query for SELECTing TASKs from the database
  tasks = cursor.fetchall()
                        
 # for Task.ID in tasks:
 #  print Task.ID
  #tasks = []
  #tasks.append(Task(0, "EasyTaskId0", 10, 0))
  #tasks.append(Task(1, "EasiestTaskId1", 0, 0))
  #tasks.append(Task(3, "HardTaskId3", 30, 0))
  #tasks.append(Task(4, "MediumTaskId4", 20, 0))
  #tasks.append(Task(5, "HardestTaskId5", 40, 0))
  #tasks.append(Task(6, "MediumTaskId6", 20, 0))
  #users = []
  #users.append(User(0,"UserId0ScoreHigh", 0, 40))
  #users.append(User(1, "UserId1ScoreLow", 0, 10))
  #users.append(User(2, "UserId2ScoreHigh", 0, 40))
  #users.append(User(3, "UserId3ScoreMedium", 0, 20))


  cursor.execute("SELECT Task.Name, Task.Difficulty, User_Task_Log.Deadline, User_Task_Log.Submitted, User_Task_Log.Submitted_Date, User_Task_Log.Verified, User_Task_Log.Verified_Date FROM User_Task_Log INNER JOIN Task ON User_Task_Log.Task_ID = Task.ID WHERE Task.Group_ID = %s ORDER BY Task.Difficulty ASC" % groupID) #MySQL query for SELECTing USER of the group form the db
  users = cursor.fetchall()
  
 # for user in users:
   # print user

  # Question: DO WE NEED ANYTHING ELSE FOR THIS PURPOSE?
  #Answer = YES! Need to sort the users and tasks just-in-case

  #bubble_sort_users(users)

  #bubble_sort_tasks(tasks)
  
  taskArray = []
  for task in tasks:
    newTask = SimpleTask(task[0], task[1], task[2])
    taskArray.append(newTask)

  assignTasksToUsers(taskArray, users)
    #Since we, hopefully, handled adding the tasks to the users
    # we need to update the database, right?

  for user in users:
      print user.name
      for userTask in user.userTasks:
          print userTask.name
          
  tasks.close()
  users.close()
  connection.close()
