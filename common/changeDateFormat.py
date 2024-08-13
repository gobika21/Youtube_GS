from datetime import datetime

def change_date_format(currentDate):
    try:
        # Attempt to parse the datetime with microseconds
        dt = datetime.strptime(currentDate, '%Y-%m-%dT%H:%M:%S.%fZ')
    except ValueError:
        # Fallback if no microseconds are present
        dt = datetime.strptime(currentDate, '%Y-%m-%dT%H:%M:%SZ')
    
    newDate = dt.strftime('%Y-%m-%d %H:%M:%S')
    return newDate
