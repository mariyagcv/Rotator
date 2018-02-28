
class Task: #can have more stuff depending on the database structure
  def __init__(self, new_task_id, new_name, new_diff, new_deadline, new_verified, new_group_id):
    self.task_id = new_task_id
    self.name = new_name
    self.difficulty = new_diff
    self.deadline = new_deadline
    self.verified = new_verified
    self.group_id = new_group_id

  def compareIdWithUser(self, userToCompare):
    return self.group_id == userToCompare.group_id
    
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
    
class User: #can have more stuff depending on the database structure
  def __init__(self, new_id, new_password, new_name, new_email, new_phone_no, new_group_id, new_workScore):
    self.id = new_id
    self.password = new_password
    self.name = new_name
    self.email = new_email
    self.phone_no = new_phone_no
    self.group_id = new_group_id
    self.workScore = new_workScore
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
  def __init__(self, new_id, new_deadline, new_submitted, new_submitted_date, new_verified, new_verified_date, new_userId, new_groupId):
    self.id = new_id
    self.deadline = new_dealine
    self.submitted = new_submitted
    self.submitted_date = new_submitted_date
    self.verified = new_verified
    self.verified_date = new_verified_date
    self.userId = new_userId
    self.groupId = new_groupId

