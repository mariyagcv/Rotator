
class Task: #can have more stuff depending on the database structure
  def __init__(self, new_task_id, new_name, new_diff, new_group_id):
    self.id = new_task_id
    self.name = new_name
    self.difficulty = new_diff
    self.group_id = new_group_id

  def compareIdWithUser(self, userToCompare):
    return self.group_id == userToCompare.group_id

"""    
class SimpleTask:
  def __init__(self, new_task_id, new_name, new_diff):
    self.task_id = new_task_id
    self.name = new_name
    self.difficulty = new_diff
    self.deadline = None
    self.verified = None
    self.group_id = None
    
  def compareIdWithUser(self, userToCompare):
    return self.group_id == userToCompare.group_id
"""
    
class User: #can have more stuff depending on the database structure
  def __init__(self, new_id, new_password, new_name, new_email, new_phone, new_group_id):
    self.id = new_id
    self.password = new_password
    self.name = new_name
    self.email = new_email
    self.phone = new_phone
    self.group_id = new_group_id
    self.userTasks = []

  def add_task(self, task):
    self.userTasks.append(task)
    
class SimpleUser: #can have more stuff depending on the database structure
  def __init__(self, new_id, new_name):
    self.id = new_id
    self.name = new_name
    self.userTasks = []

  def add_task(self, task):
    self.userTasks.append(task)
    
class User_Group_Log:
  def __init__(self, new_id, new_workScore, new_userId, new_groupId):
    self.id = new_id
    self.workScore = new_workScore
    self.userId = new_userId
    self.groupId = new_groupId
    
class User_Task_Log:
  def __init__(self, new_id, new_deadline, new_submitted, new_submitted_date, new_verified, new_verified_date, new_userId, new_taskId):
    self.id = new_id
    self.deadline = new_dealine
    self.submitted = new_submitted
    self.submitted_date = new_submitted_date
    self.verified = new_verified
    self.verified_date = new_verified_date
    self.userId = new_userId
    self.taskId = new_taskId
    
class Group:
  def __init__(self, new_id, new_name):
    self.id = new_id
    self.name = new_name

