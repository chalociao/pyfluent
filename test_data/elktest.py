import json, pprint
import random
from datetime import datetime

# Logging Format
# log = {
#     "timestamp" : None,
#     "application" : None,
#     "component" : None,
#     "instance" : None,
#     "version" : None,
#     "kind" : None,
#     "level" : None,
#     "transaction" : None,
#     "message_type" : None,
#     "message" : None,
#     "traceback_object" : None
# }

# Definition of possible log fields
application = ["MTS.NOM", "SMSS", "FPM", "FPT"]
component = ["EMAIL_BACKEND", "FRONTEND", "MDW", "BATCH_JOB"]
instance = ["POD01", "POD02", "POD03", "POD04"]
kind = ["B", "T"]
level = ["INFO", "WARN", "ERROR", "CRITICAL", "FATAL"]
message_type = ["LOGIN01", "EMAILTR", "UPDBILL"]

# Filling file
print( "Pasting logs into ´elk.log´...\nPress Ctrl-C to stop" )

try:
    while( True ):
        with open( 'elk.log', 'a') as logfile:
            logfile.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + ' - ' + 
                        random.choice(application)+ ' - ' +
                        random.choice(component)+ ' - ' +
                        random.choice(instance)+ ' - ' +
                        random.choice(kind)+ ' - ' +
                        random.choice(level)+ ' - ' +
                        random.choice(message_type)+'\n')
                        
except KeyboardInterrupt:
    print( "\nStopped" )
    pass