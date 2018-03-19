# email notifications response functions
# based on different actions performed by app/users

# !ONLY WORKS ON A MACHINE WHERE NEEDED LIBRARIES ARE DOWNLOADED!
# See "Step 2" here: https://developers.google.com/gmail/api/quickstart/python

# import what we need
from __future__ import print_function
import httplib2
import os

from email.mime.text import MIMEText
import base64
from googleapiclient.errors import HttpError

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import mysql.connector
from datetime import timedelta, date, datetime

global connection
global cursor

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/gmail-python-quickstart.json
# Following credentials allow to create, alter and delete drafts
# and to send massages and draftes.
SCOPES = 'https://www.googleapis.com/auth/gmail.compose'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Quickstart'

# NOT USED ANYMOE: WE CHANGED THE APROACH
# CHECKED
# Method that creates drafts for further reminder emails.
# Should be used when tasks are allocated.
# Parameters: name of the reciever,
#             email of the reciever,
#
#def mailResponseToAssignment(name, email): #taskID):

  

  # create draft for one day prior notification
#  oneDayPriorSubject = "Tomorrow's Deadline"
#  oneDayPriorText = "Dear %s!\nYour task deadline is tomorrow. For more info log in to your Rotator account." % name
#  oneDayPriorTextID = create_draft("me", create_message(email, oneDayPriorSubject, oneDayPriorText))

  # create draft for day of deadline notification
#  deadlineDaySubject = "Today's Deadline"
#  deadlineDayText = "Dear %s!\nYour task deadline is today.\nMake sure You copmlete it in time.\nFor more info log in to your Rotator account." % name
#  deadlineDayTextID = create_draft("me", create_message(email, deadlineDaySubject, deadlineDayText))

  # create draft for one day late notification
#  oneDayAfterSubject = "Missed Deadline"
#  oneDayAfterText = "Dear %s!\nYour task deadline was yesterday. For more info log in to your Rotator account." % name
#  oneDayAfterTextID = create_draft("me", create_message(email, oneDayAfterSubject, oneDayAfterText))

  #for testing
  #draft_ids = []
  #draft_ids.append(oneDayPriorTextID)
  #draft_ids.append(deadlineDayTextID)
  #draft_ids.append(oneDayAfterTextID)
  #return draft_ids





# Method that sends requests to verify the submition
# to other members of the group and freezes reminder drafts.
# Should be used when task is submitted.
# Parameters: array of emails of the people in the group (apart from the one submitted),
#             array of draft ids associated with the task submitted,
#
def mailResponseToSubmit(user_ID):

  # some needed housekeeping
  credentials = get_credentials()
  http = credentials.authorize(httplib2.Http())
  service = discovery.build('gmail', 'v1', http=http)

  # freeze notifications for this task
#  if (len(draftIDs) != 0):
#    for i in range(0, len(draftIDs) - 1):
#      draftIDs[i]

  credentials = get_credentials()
  http = credentials.authorize(httplib2.Http())
  service = discovery.build('gmail', 'v1', http=http)

  connection = mysql.connector.connect(
    user="mbyxadr2", database="2017_comp10120_z8", password="fA+h0m5_", host = "dbhost.cs.man.ac.uk"
    )
  cursor= connection.cursor(buffered=True)

  cursor.execute("SELECT Group_ID FROM User WHERE User_ID = %s" % user_ID)
  groupid = cursor.fetchall()

  cursor.execute("SELECT Email FROM User WHERE Group_Id = %s AND User_ID != %s" % (groupid, user_ID))
  emails = cursor.fetchall()

  # send verification emails
  submitionSubject = "Verification Needed"
  submitionText = "Hello,\nOne of your neighbours submitted their task and needs verification. For more info log in to your Rotator account."
  for email in emails:
    submitionTextID = send_message("me", create_message(email, submitionSubject, submitionText))



# Method that sends notification to the person,
# whose task was verified, and deletes the reminder drafts.
# Should be used when task is verified.
# Parameters: array of draft ids associated with the task verified,
def mailResponseToVerify(task_ID):
  #
  #
  # some needed housekeeping
  credentials = get_credentials()
  http = credentials.authorize(httplib2.Http())
  service = discovery.build('gmail', 'v1', http=http)


# !!!!! inform the person that their task was verified


# Method to send timed notifications daily
# Parameters: array of user IDs such that
#             the task is not submitted and
#             either deadline = today + 1,
#             or     deadline = today,
#             or     deadline = today - 1,
#
def dailyEmailNotifications():

  # some needed housekeeping
  credentials = get_credentials()
  http = credentials.authorize(httplib2.Http())
  service = discovery.build('gmail', 'v1', http=http)

  connection = mysql.connector.connect(
    user="mbyxadr2", database="2017_comp10120_z8", password="fA+h0m5_", host = "dbhost.cs.man.ac.uk"
    )
  cursor= connection.cursor(buffered=True)


  # send the notifications
  #calculate day difference (to an hour)
  cursor.execute("SELECT User_Task_Log.Deadline FROM User_Task_Log WHERE User_Task_Log.Submitted = 0" 
                         )
  deadlines = cursor.fetchall()
  cursor.execute("SELECT User_ID FROM User_Task_Log WHERE User_Task_Log.Submitted = 0" 
                         )
  user_ids = cursor.fetchall()

  oneDayPriorSubject = "Tomorrow's Deadline"
  deadlineDaySubject = "Today's Deadline"
  oneDayAfterSubject = "Missed Deadline"

  for i in range(0, len(deadlines)):
    notificationDeadline = timedelta((today - deadlines[0]).days)
    # tomorrow is deadline
    if notificationDeadline == -1:
      cursor.execute("SELECT User.Email, User.Name FROM User WHERE User.ID = %s" % user_ids[i])
      email =  cursor.fetchall()
      oneDayPriorText = "Dear %s!\nYour task deadline is tomorrow. For more info log in to your Rotator account." % email[1]
      oneDayPriorTextID = send_message("me", create_message(email[0], oneDayPriorSubject, oneDayPriorText))

    # today is deadline
    elif notificationDeadline == 0:
      cursor.execute("SELECT User.Email, User.Name FROM User WHERE User.ID = %s" % user_ids[i])
      email =  cursor.fetchall()
      deadlineDayText = "Dear %s!\nYour task deadline is today.\nMake sure You copmlete it in time.\nFor more info log in to your Rotator account." % email[1]
      deadlineDayTextID = create_draft("me", create_message(email[0], deadlineDaySubject, deadlineDayText))

      
    # yesterday was deadline
    elif notificationDeadline == 1:
      cursor.execute("SELECT User.Email, User.Name FROM User WHERE User.ID = %s" % user_ids[i])
      email =  cursor.fetchall()
      oneDayAfterText = "Dear %s!\nYour task deadline was yesterday. For more info log in to your Rotator account." % email[1]
      oneDayAfterTextID = create_draft("me", create_message(email[0], oneDayAfterSubject, oneDayAfterText))

      


# helper functions

# generates MIME message (an internet standart
# that extends the format of email)
def create_message(to, subject, message_text):
  message = MIMEText(message_text)
  message['to'] = to
  message['from'] = "'Rotator Reminder' <rotator.app@gmail.com>"
  message['subject'] = subject
  return {'raw': base64.urlsafe_b64encode(message.as_string())}


# creates a draft
#def create_draft(user_id, message_body):

  # some needed housekeeping
#  credentials = get_credentials()
#  http = credentials.authorize(httplib2.Http())
#  service = discovery.build('gmail', 'v1', http=http)

#  try:
#    message = {'message': message_body}
#    draft = service.users().drafts().create(userId=user_id, body=message).execute()

    # for testing
    # print 'Draft id: %s\nDraft message: %s' % (draft['id'], draft['message'])

#    return draft["id"]
#  except HttpError, error:
#    print('An error occurred: %s' % error)
#    return None

# deletes a draft

# sends a message
def send_message(user_id, message):

  # some needed housekeeping
  credentials = get_credentials()
  http = credentials.authorize(httplib2.Http())
  service = discovery.build('gmail', 'v1', http=http)

  try:
    message = (service.users().messages().send(userId=user_id, body=message)
               .execute())

    # fot testing
    # print 'Message Id: %s' % message['id']
    return message
  except errors.HttpError, error:
    print('An error occurred: %s' % error)


# sends a draft
def send_draft(user_id, draftID):

  # some needed housekeeping
  credentials = get_credentials()
  http = credentials.authorize(httplib2.Http())
  service = discovery.build('gmail', 'v1', http=http)


  try:
    message = (service.users().drafts().send(userId=user_id, body={'id': str(draftID)})
               .execute())

    # fot testing
    # print 'Message Id: %s' % message['id']
    return message
  except HttpError, error:
    print('An error occurred: %s' % error)



# gets credentials
def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'gmail-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials
