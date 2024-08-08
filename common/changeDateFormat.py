
from datetime import datetime

def change_date_format(currentDate):
    dt = datetime.strptime(currentDate, '%Y-%m-%dT%H:%M:%SZ')
    newDate = dt.strftime('%Y-%m-%d %H:%M:%S')
    return newDate