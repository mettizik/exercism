import datetime
import calendar


def meetup_day(year, month, day, desc):
    days_mapping = dict(zip(calendar.day_name, range(7)))
    expectedDay = days_mapping[day]
    matchingDays = [d[expectedDay] for d in calendar.monthcalendar(
        year, month) if d[expectedDay] != 0]
    if 'last' == desc:
        dayToSet = matchingDays[-1]
    elif 'first' == desc:
        dayToSet = matchingDays[0]
    elif 'teenth' == desc:
        dayToSet = [d for d in matchingDays if d > 10][0]
    else:
        dayToSet = matchingDays[int(desc[:1]) - 1]

    return datetime.date(year, month, dayToSet)
