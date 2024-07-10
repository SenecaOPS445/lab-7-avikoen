#!/usr/bin/env python3

from lab7a import Time, valid_time

def change_time(time, seconds):
    time.second += seconds

    while time.second >= 60:
        time.second -= 60
        time.minute += 1
    while time.minute >= 60:
        time.minute -= 60
        time.hour += 1
    while time.second < 0:
        time.second += 60
        time.minute -= 1
    while time.minute < 0:
        time.minute += 60
        time.hour -= 1
    while time.hour < 0:
        time.hour += 24
    while time.hour >= 24:
        time.hour -= 24

    return None

def format_time(t):
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    
    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1
    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1
    
    return sum

if __name__ == "__main__":
    t1 = Time(8, 0, 0)
    t2 = Time(8, 55, 0)
    t3 = Time(9, 50, 0)

    td = Time(0, 50, 0)

    tsum1 = sum_times(t1, td)
    tsum2 = sum_times(t2, td)
    change_time(t3, 1800)

    ft = format_time
    print(ft(t1), '+', ft(td), '-->', ft(tsum1))
    print(ft(t2), '+', ft(td), '-->', ft(tsum2))
    print('09:50:00 + 1800 sec', '-->', ft(t3))
