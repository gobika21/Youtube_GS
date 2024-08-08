from datetime import timedelta

def change_time_format(currentTime):
    # Remove the 'PT' prefix
    duration_str = currentTime[2:]

    # Initialize hours, minutes, and seconds
    hours, minutes, seconds = 0, 0, 0

    # Parse the duration string
    if 'H' in duration_str:
        hours, duration_str = duration_str.split('H')
        hours = int(hours)
    if 'M' in duration_str:
        minutes, duration_str = duration_str.split('M')
        minutes = int(minutes)
    if 'S' in duration_str:
        seconds = int(duration_str.replace('S', ''))

    # Create a timedelta object
    td = timedelta(hours=hours, minutes=minutes, seconds=seconds)

    # Calculate total seconds
    total_seconds = int(td.total_seconds())

    # Format the total seconds as HH:MM:SS
    formatted_time = f'{total_seconds // 3600:02}:{(total_seconds % 3600) // 60:02}:{total_seconds % 60:02}'

    return formatted_time
