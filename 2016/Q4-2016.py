import timeit
start = timeit.default_timer()
MORNING_RUSH_HOUR_BEGIN = 420
MORNING_RUSH_HOUR_END = 600
EVENING_RUSH_HOUR_BEGIN = 900
EVENING_RUSH_HOUR_END = 1140


def check_rush_hour(departure, arrival):
    extra_time = 0
    # Case 1: Arrival time between morning rush hour
    if MORNING_RUSH_HOUR_BEGIN <= arrival <= MORNING_RUSH_HOUR_END:
        # Case 2: Departure time between morning rush hour along with arrival time
        if MORNING_RUSH_HOUR_BEGIN <= departure <= MORNING_RUSH_HOUR_END:
            #extra time has a max value of 120. An alogrithm below is designed to calculate that
            extra_time = int((120 - (MORNING_RUSH_HOUR_END - arrival_time)) / 2)+(MORNING_RUSH_HOUR_END - arrival_time)
        # Case 3: Departure time not between the morning rush hour
        else:
            extra_time = min(arrival-MORNING_RUSH_HOUR_BEGIN, arrival-departure)
    # Case 4: Departure time between rush hour but not the arrival time
    elif MORNING_RUSH_HOUR_BEGIN <= departure <= MORNING_RUSH_HOUR_END:
        extra_time = MORNING_RUSH_HOUR_END-departure
    # The next cases are similar to the previous ones, just for the evening rush hours
    elif EVENING_RUSH_HOUR_BEGIN <= arrival <= EVENING_RUSH_HOUR_END:
        if EVENING_RUSH_HOUR_BEGIN <= departure <= EVENING_RUSH_HOUR_END:
            extra_time = int((120 - (EVENING_RUSH_HOUR_END - arrival_time)) / 2)+(EVENING_RUSH_HOUR_END - arrival_time)
        else:
            extra_time = min(arrival-EVENING_RUSH_HOUR_BEGIN, arrival-departure)
        extra_time = min(arrival-EVENING_RUSH_HOUR_BEGIN, arrival-departure)
    elif EVENING_RUSH_HOUR_BEGIN <= departure_time <= EVENING_RUSH_HOUR_END:
        extra_time = EVENING_RUSH_HOUR_END - departure
    return extra_time


file = open("input", 'r')
departure_time_list = file.readline().split(":")
departure_time = int(departure_time_list[0])*60+int(departure_time_list[1])
arrival_time = departure_time + 120
arrival_time += check_rush_hour(departure_time, arrival_time)
arrival_time = list(divmod(arrival_time, 60))
print("Arrival Time: {:02d}:{:02d}".format(arrival_time[0] % 24, arrival_time[1]))
stop = timeit.default_timer()
print('Total RunTime: ', stop - start)
