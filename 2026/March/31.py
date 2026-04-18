def alarm_check(alarm_time, wake_time):
    a=int(alarm_time.replace(':',''))
    w=int(wake_time.replace(':',''))
    if w<a:
        return "early"
    elif w==a or (w-a)<11:
        return "on time"
    elif w>a:
        return "late"