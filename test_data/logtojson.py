import json
import csv
from datetime import datetime
import time

# Reads the csv file, adds the curent time to each object then prints it to stdOUT as JSON
with open( 'test_data.csv', 'r+' ) as csvfile:
    reader = csv.DictReader( csvfile )
    for lines in reader:
        lines[ "timestamp" ] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        
        # remove 'indent=4' for single line per JSON object
        # indent flag is to have a pretty output
        time.sleep(.1)
        print (json.dumps(lines))
#        print( json.dumps( lines, indent=4 ) )
