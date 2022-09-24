#!/bin/python
from datetime import datetime

minute_to_words = {
        0: "",
        5: "fem över ",
        10: "tio över ",
        15: "kvart över ",
        20: "tjugo över ",
        25: "fem i halv ",
        30: "halv ",
        35: "fem över halv ",
        40: "tjugo i ",
        45: "kvart i ",
        50: "tio i ",
        55: "fem i "
        }

hours_to_words = {
        1: "ett",
        2: "två",
        3: "tre",
        4: "fyra",
        5: "fem",
        6: "sex",
        7: "sju",
        8: "åtta",
        9: "nio",
        10: "tio",
        11: "elva",
        12: "tolv",
        }

def hour_and_minute():
    return datetime.now().strftime('%I %M').split(' ')

def main():
    hour, minute = hour_and_minute()
    hour = int(hour)
    minute = ((int(minute) + 2)//5)*5
    if minute >= 25:
        hour = hour + 1
    if minute >= 60:
        minute = 0 
    if hour > 12:
        hour %= 12 
    hour = hours_to_words[hour]
    minute = minute_to_words[minute]
    print(f'{minute}{hour}')

if __name__ == '__main__':
    main()
