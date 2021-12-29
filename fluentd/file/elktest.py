import json
import random
from datetime import datetime
import time

log = {
    "timestamp" : None,
    "application" : None,
    "component" : None,
    "instance" : None,
    "version" : None,
    "kind" : None,
    "level" : None,
    "transaction" : None,
    "message_type" : None,
    "message" : None,
    "traceback_object" : None
}

application = ["MTS", "SMSS"]
component = ["EMAIL_BACKEND", "FRONTEND", "MDW", "BATCH_JOB"]
instance = ["POD01", "POD02", "POD03", "POD04"]
kind = ["B", "T"]
level = ["INFO", "WARN", "ERROR", "CRITICAL", "FATAL"]
message_type = ["LOGIN01", "EMAILTR", "UPDBILL"]

log["timestamp"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
log["application"] = random.choice(application)
log["component"] = random.choice(component)
log["instance"] = random.choice(instance)
log["kind"] = random.choice(kind)
log["level"] = random.choice(level)
log["message_type"] = random.choice(message_type)


while True:
    file_op = open("/app/pylogs.log", "a")
    # file_op = open("../file/pylogs.log", "a")
    print(log, file=file_op)
    time.sleep(5)
    # print(log, file_op)
    # file_op.close()
