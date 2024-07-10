#!/usr/bin/env python3

class Time:
    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def time_to_sec(time):
    '''convert a time object to a single integer representing the number of seconds from mid-night'''
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):   
    '''convert a given number of seconds to a time object in hour, minute, second format'''
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes,60)
    return time

def sum_times(t1, t2):
    '''Add two time objects and return the sum.'''
    seconds1 = time_to_sec(t1)
    seconds2 = time_to_sec(t2)
    total_seconds = seconds1 + seconds2
    return sec_to_time(total_seconds)

def change_time(time, seconds):
    '''Change the time object by adding a number of seconds'''
    total_seconds = time_to_sec(time) + seconds
    new_time = sec_to_time(total_seconds)
    time.hour, time.minute, time.second = new_time.hour, new_time.minute, new_time.second
    return None

def valid_time(t):
    '''Check for the validity of the time object attributes'''
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True
