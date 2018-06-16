import math

def get_calories_needed(male, active):
    if male:
        if active:
            return 2400
        else:
            return 2000
    else:
        if active:
            return 2000
        else:
            return 1600

def avg(one, two):
    return (one+two)/2

def total_percent_deviation(percent1, percent2, percent3):
    return math.fabs(percent1) + math.fabs(percent2) + math.fabs(percent3)

def get_from_percent_ideal(percent_ideal, type_cal, total_cal):
    return ((type_cal*100)/total_cal) -percent_ideal

def get_percent_from_ideal_carb(carb_cal, total_cal):
    avg = avg(45,65)
    return get_percent_from_ideal(avg, carb_cal, total_cal)

def get_percent_from_ideal_prot(carb_cal, total_cal):
    avg = avg(10,35)
    return get_percent_from_ideal(avg, carb_cal, total_cal)

def get_percent_from_ideal_fat(carb_cal, total_cal):
    avg = avg(20, 35)
    return get_percent_from_ideal(avg, carb_cal, total_cal)
