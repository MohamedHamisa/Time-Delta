#import datetime modules
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# Complete the time_delta function below.
def time_delta(t1, t2):
    #convert string into datetime object with datetime.strptime(date_time_string_input, format input)
    date1 = datetime.strptime(t1,"%a %d %b %Y %H:%M:%S %z")
    date2 = datetime.strptime(t2,"%a %d %b %Y %H:%M:%S %z")
    #calculate timedelta
    timedelta = date1 - date2
    #convert timedelta to total_seconds
    timedelta = abs(timedelta.total_seconds())
    #format string number of total second
    tdelta = ("{:.0f}".format(timedelta))
    return tdelta

