from emailResponses import mailResponseToAssignment
from emailResponses import dailyEmailNotifications

# test data 1
reciever_name = "Daria"
reciever_email = "daritolm@gmail.com"
draft_ids1 = mailResponseToAssignment(reciever_name, reciever_email)

# test data 2
reciever_name = "Ms Tolmacheva"
reciever_email = "daria.tolmacheva@student.manchester.ac.uk"
draft_ids2 = mailResponseToAssignment(reciever_name, reciever_email)

# actual test
draft_ids = draft_ids1 + draft_ids2
#for i in range(0, (len(draft_ids) - 1)):
#  print(draft_ids)

dailyEmailNotifications(draft_ids)
