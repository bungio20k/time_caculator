MINS_PER_HOUR = 60
HOURS_PER_DAY = 24
HOURS_PER_SES = 12
WEEK = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def add_time(start, duration, day = ''):
    # standardize data
    start_hour = int(start.split()[0].split(':')[0])
    start_min = int(start.split()[1].split(':')[1])
    sessions = start.split()[1]
    if sessions == 'PM':
        start_hour += 12
        sessions = 'AM'
    duration_hour = duration.split(':')[0]
    duration_min = duration.split(':')[1]
    day = day.lower()
    redundancy = 0
    postfix = ''

    # caculating minutes
    start_min += duration_min
    start_hour += start_min % MINS_PER_HOUR
    start_min /= MINS_PER_HOUR
    
    # caculating hours
    start_hour += duration_hour
    redundancy += start_hour / HOURS_PER_DAY
    start_hour /= HOURS_PER_DAY

    # caculating sessions
    if start_hour / HOURS_PER_SES >= 1:
        start_hour = start_hour % HOURS_PER_SES
        sessions = 'PM'
    
    # caculating days
    if day != '':
        day = ', ' + WEEK[(WEEK.index(day) + redundancy) % 7]
    
    # caculating postfix
    if redundancy == 0:
        postfix = ''
    elif redundancy == 1:
        postfix = '(next day)'
    else:
        postfix = ' (' + str(redundancy) + ' days later)'

    #combining all
    new_time = str(start_hour) + ':' + str(start_min) + ' ' + sessions + day + postfix

    return new_time