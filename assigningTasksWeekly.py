import mysql.connector


# A few definitions

class Task: #can have more stuff depending on the database structure
  def __init__(self, task_id, new_name, new_diff, group_id):
    self.name = new_name
    self.difficulty = new_diff
    self.slot = -1 #value of -1 means an unassigned slot -- this can be used in timetable viewing
  

class User: #can have more stuff depending on the database structure
  def __init__(self, new_id)
    self.id = new_id
    self.userTasks = []
    self.freeSlot = 0

  def add_task(self, task)
    self.userTasks.append(task)
    self.freeSlot += 1

def addTaskToUser(task, user):
  task.slot = user.freeSlot
  user.add_task(task)

#Actual code starts here:

connection = mysql.connector.connect(
  #Our database details for connection
  )

tasks = connection.cursor()
tasksQuery = () #MySQL query for SELECTing TASKs IDs from the database
tasks.execute(tasksQuery)
taskLength = len(tasks)


userIds = connection.cursor()
userIdsQuery = () #MySQL query for SELECTing USER IDs of the group form the db
userIds.execute(userIdsQuery)
userIdsLength = len(userIds)

# Question: DO WE NEED ANYTHING ELSE FOR THIS PURPOSE?

for i in range(0, taskLength):
  x = i
  if(x >= userIdsLength):
    x = x - userLength
  addTaskToUser(tasks[i], userIds[x])
  #Since we, hopefully, handled adding the tasks to the users
  # we need to update the database, right?

tasks.close()
userIds.close()
connection.close()

