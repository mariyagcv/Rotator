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


tasks = []
taskLength = #MySQL (or sth else) to give me the total number of TASKS in the GROUP

for i in range(0, taskLength):
  next_task = Task(#MySQL to give the next task's details)
  tasks.append(new_task)

users = []
userLength = #MySQL to give me the total number of USERS in the GROUP

for i in range(0, userLength):
  next_user = User(#MySQL shit here to get his/her id and all)
  next_userLength = #MySQL shit
  for x in range(0, next_userLength):
    next_user.add_task(#MySQL to get his/her task)
  users.append(next_user)


for i in range(0, taskLength):
  x = i
  if(x >= userLength):
    x = x - userLength
  addTaskToUser(tasks[i], users[x])
  #Since we, hopefully, handled adding the tasks to the users
  # we need to update the database, right?


connection.close()

