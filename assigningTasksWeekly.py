#import mysql.connector


# A few definitions

class Task: #can have more stuff depending on the database structure
  def __init__(self, new_task_id, new_name, new_diff, new_group_id):
    self.task_id = new_task_id
    self.name = new_name
    self.difficulty = new_diff
    self.group_id = new_group_id
    self.slot = -1 #value of -1 means an unassigned slot -- this can be used in timetable viewing

  def compareIdWithUser(self, userToCompare):
    return self.group_id == userToCompare.group_id


class User: #can have more stuff depending on the database structure
  def __init__(self, new_id, new_name, new_group_id, new_rankScore):
    self.id = new_id
    self.name = new_name
    self.group_id = new_group_id
    self.rankScore = new_rankScore
    self.userTasks = []
    self.freeSlot = 0

  def add_task(self, task):
    self.userTasks.append(task)
    self.freeSlot += 1

  def addTaskToUser(task, user):
    task.slot = user.freeSlot
    user.add_task(task)


def bubble_sort_users(users): #sorts users in ascending order of score
    for i in range(0, len(users) - 2):
        for j in range(i, len(users) - 1):
            if(users[j].rankScore > users[j+1].rankScore):
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

def assignTasksToUsers(tasks, users):
    for i in range(0, len(tasks)):
      x = i
      if(x >= len(users)):
        x = x - len(users)
      if(tasks[i].compareIdWithUser(users[x])):
          users[x].add_task(tasks[i])
      else:
          print "Error: There is a user (or a task) with a different group id!"


#Actual code starts here:

#connection = mysql.connector.connect(
  #Our database details for connection
#  )

#tasks = connection.cursor()
#tasksQuery = () #MySQL query for SELECTing TASKs IDs from the database
#tasks.execute(tasksQuery)
tasks = []
tasks.append(Task(0, "EasyTaskId0", 10, 0))
tasks.append(Task(1, "EasiestTaskId1", 0, 0))
tasks.append(Task(3, "HardTaskId3", 30, 0))
tasks.append(Task(4, "MediumTaskId4", 20, 0))
tasks.append(Task(5, "HardestTaskId5", 40, 0))
tasks.append(Task(6, "MediumTaskId6", 20, 0))


users = []
users.append(User(0,"UserId0ScoreHigh", 0, 40))
users.append(User(1, "UserId1ScoreLow", 0, 10))
users.append(User(2, "UserId2ScoreHigh", 0, 40))
users.append(User(3, "UserId3ScoreMedium", 0, 20))


#userIds = connection.cursor()
#userIdsQuery = () #MySQL query for SELECTing USER IDs of the group form the db
#userIds.execute(userIdsQuery)
#userIdsLength = len(userIds)

# Question: DO WE NEED ANYTHING ELSE FOR THIS PURPOSE?
#Answer = YES! Need to sort the users and tasks just-in-case

bubble_sort_users(users)

bubble_sort_tasks(tasks)

assignTasksToUsers(tasks, users)
  #Since we, hopefully, handled adding the tasks to the users
  # we need to update the database, right?

for user in users:
    print user.name
    for userTask in user.userTasks:
        print userTask.name
#tasks.close()
#userIds.close()
#connection.close()
