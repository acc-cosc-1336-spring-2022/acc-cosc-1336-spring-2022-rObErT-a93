def get_time(hour, minutes, seconds, time_type, meridiem='AM'):
    if hour < 10:
        hour = "0" + str(hour)

    if minutes < 10:
        minutes  = "0" + str(minutes)

    if seconds < 10:
        seconds = "0" + str(seconds)

    time = str(hour) + ":" + str(minutes) + ":" + str(seconds)

    if time_type == 12:
        time = time + " " + meridiem

    return  time

def get_hour(epoch_seconds):
    return epoch_seconds // 3600

def get_minutes(epoch_seconds):
    return (epoch_seconds // 60) % 60

def get_seconds(epoch_seconds):
    return epoch_seconds % 60

def time_from_utc(utc_offset, utc_zero):
    sum = utc_offset + utc_zero
    return sum % 24