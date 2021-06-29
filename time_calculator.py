MINS_PER_HOUR = 60
HOURS_PER_DAY = 24
HOURS_PER_SES = 12
WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def add_time(start, duration, day = ''):
    # standardize data
    start_hour = int(start.split()[0].split(':')[0])
    start_min = int(start.split()[0].split(':')[1])
    sessions = start.split()[1]
    if sessions == 'PM':
        start_hour += 12
        sessions = 'AM'
    duration_hour = int(duration.split(':')[0])
    duration_min = int(duration.split(':')[1])
    day = day.lower()
    redundancy = 0
    postfix = ''

    # caculating minutes
    start_min += duration_min
    start_hour += start_min // MINS_PER_HOUR
    start_min %= MINS_PER_HOUR
    start_min = str(start_min)
    if len(start_min) < 2:
        start_min = '0' + start_min

    # caculating hours
    start_hour += duration_hour
    redundancy += start_hour // HOURS_PER_DAY
    start_hour %= HOURS_PER_DAY

    # caculating sessions
    if start_hour >= HOURS_PER_SES:
        sessions = 'PM'
        if start_hour > HOURS_PER_SES:
            start_hour -= HOURS_PER_SES
    elif start_hour == 0:
        start_hour = HOURS_PER_SES
    # caculating days
    if day != '':
        day = ', ' + WEEK[(WEEK.index(day[0].capitalize() + day[1:]) + redundancy) % 7]
    
    # caculating postfix
    if redundancy == 0:
        postfix = ''
    elif redundancy == 1:
        postfix = ' (next day)'
    else:
        postfix = ' (' + str(redundancy) + ' days later)'

    #combining all
    new_time = str(start_hour) + ':' + start_min + ' ' + sessions + day + postfix

    return new_time