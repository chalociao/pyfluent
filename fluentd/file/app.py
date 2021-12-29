import json
from json import JSONEncoder
from datetime import datetime
import time





# class DateTimeEncoder(JSONEncoder):
#         #Override the default method
#         def default(self, obj):
#             if isinstance(obj, (datetime.date, datetime.datetime)):
#                 return obj.isoformat()

# print("Printing to check how it will look like")
# print(DateTimeEncoder().encode(logmsg))

while True:
    logmsg = {
    "timestamp" : datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f'),
    "application" : "pylogs-app",
    "message" : "EFK on Docker with Py",
    "message_type" : "Login Start"
}
    # print(logmsg)
    # print(datetime.now())
    # time.sleep(5)
    j = json.dumps(logmsg)
    file_op = open("/pylogs.log", "a")
    # file_op = open("pylogs.log", "a")
    # print(logmsg, file=file_op)
    # # print("Encode DateTime Object into JSON using custom JSONEncoder")
    # # logJson = json.dumps(logmsg, indent=4, cls=DateTimeEncoder)
    print(j, file=file_op)
    time.sleep(5)


#######
# logmsg['date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
 
# def myconverter(o):
#     if isinstance(o, datetime.datetime.now()):
#         return o.__str__()
# while True:
#     file_op = open("/app/pylogs.log", "a")
#     # file_op = open("pylogs.log", "a")
#     # print(log, file=file_op)
#     print(json.dumps(logmsg, default = myconverter), file=file_op)    # {"date": "2016-04-08 11:43:36.309721", "name": "Foo"}
#     time.sleep(5)


# dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# pystring = '{"timestamp":dt, "app":"file-myapp", "message" : "EFK on Docker with Py"}'
# # log = {
#     "timestamp" : None,
#     "application" : None,
#     "message" : None,
# }

# log["timestamp"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# log["application"] = "pylogs-app"
# log["message"] = "EFK on Docker with Py" 

# while True:
#     # file_op = open("/app/pylogs.log", "a")
#     file_op = open("pylogs.log", "a")
#     # print(log, file=file_op)
#     print(pystring)
#     time.sleep(5)
